from flask import Blueprint, render_template
from app import db
from app.models import SalesOrder, Stock, BOM

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sales_orders = SalesOrder.query.all()
    stocks = Stock.query.all()
    boms = BOM.query.all()

    purchasing_advice = calculate_purchasing_advice(sales_orders, stocks, boms)
    print("Purchasing advice:", purchasing_advice)
    return render_template('index.html', purchasing_advice=purchasing_advice)

def calculate_purchasing_advice(sales_orders, stocks, boms):
    sales_order_demand = {}
    stock_quantities = {}
    bom_requirements = {}
    purchasing_advice = []

    # Calculate the total demand for each product
    for order in sales_orders:
        if order.code not in sales_order_demand:
            sales_order_demand[order.code] = order.total - order.shipped
        else:
            sales_order_demand[order.code] += order.total - order.shipped

    # Store stock quantities in a dictionary
    for stock in stocks:
        stock_quantities[stock.code] = stock.quantity

    # Store BOM requirements in a dictionary
    for bom in boms:
        if bom.product_code not in bom_requirements:
            bom_requirements[bom.product_code] = [(bom.raw_code, bom.quantity)]
        else:
            bom_requirements[bom.product_code].append((bom.raw_code, bom.quantity))

    # Calculate the required raw materials
    raw_material_demand = {}
    for product_code, demand in sales_order_demand.items():
        if product_code in bom_requirements:
            for raw_code, quantity in bom_requirements[product_code]:
                if raw_code not in raw_material_demand:
                    raw_material_demand[raw_code] = demand * quantity
                else:
                    raw_material_demand[raw_code] += demand * quantity

    # Calculate the purchasing advice based on the demand and stock
    for raw_code, demand in raw_material_demand.items():
        stock = stock_quantities.get(raw_code, 0)
        purchase_quantity = demand - stock

        if purchase_quantity > 0:
            unit = "pieces"  # You can adjust the unit based on your requirements
            advice = {"code": raw_code, "quantity": purchase_quantity, "unit": unit}
            purchasing_advice.append(advice)
    return purchasing_advice
