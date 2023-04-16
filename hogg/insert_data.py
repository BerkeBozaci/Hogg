from app import create_app, db
from app.models import SalesOrder, Stock, BOM

app = create_app()

with app.app_context():
    # Insert sample data for SalesOrder
    sales_orders = [
        SalesOrder(code='model_s', total=200, shipped=30, order_no='PO-001'),
        SalesOrder(code='model_s', total=100, shipped=0, order_no='PO-002'),
        SalesOrder(code='semi', total=10, shipped=1, order_no='PO-003'),
        SalesOrder(code='semi', total=4, shipped=0, order_no='PO-004'),
    ]
    db.session.add_all(sales_orders)

    # Insert sample data for Stock
    stocks = [
        Stock(code='glass', quantity=200, unit='cm2'),
        Stock(code='seat', quantity=3, unit='pieces'),
        Stock(code='big_left_mirror', quantity=1, unit='pieces'),
        Stock(code='big_right_mirror', quantity=2, unit='pieces'),
        Stock(code='wheel', quantity=4, unit='pieces'),
        Stock(code='right_mirror_holder', quantity=1, unit='pieces'),
    ]
    db.session.add_all(stocks)

    # Insert sample data for BOM
    boms_data = [
        ('my_model_s', 'wheel', 4, 'pieces'),
        ('my_model_s', 'steering_wheel', 1, 'pieces'),
        ('my_model_s', 'seat', 4, 'pieces'),
        ('my_model_s', 'right_mirror', 1, 'pieces'),
        ('my_model_s', 'left_mirror', 1, 'pieces'),
        ('my_model_s', 'mid_mirror', 1, 'pieces'),
        ('my_semi', 'wheel', 8, 'pieces'),
        ('my_semi', 'steering_wheel', 1, 'pieces'),
        ('my_semi', 'seat', 1, 'pieces'),
        ('my_semi', 'big_left_mirror', 1, 'pieces'),
        ('my_semi', 'big_right_mirror', 1, 'pieces'),
        ('my_semi', 'lcd_monitor', 2, 'pieces'),
        ('left_mirror', 'glass', 100, 'cm2'),
        ('left_mirror', 'left_mirror_holder', 1, 'pieces'),
        ('right_mirror', 'glass', 100, 'cm2'),
        ('right_mirror', 'right_mirror_holder', 1, 'pieces'),
        ('mid_mirror', 'glass', 200, 'cm2'),
        ('mid_mirror', 'mid_mirror_holder', 1, 'pieces'),
        ('big_left_mirror', 'glass', 300, 'cm2'),
        ('big_left_mirror', 'big_left_mirror_holder', 1, 'pieces'),
        ('big_left_mirror', 'camera', 1, 'pieces'),
        ('big_right_mirror', 'glass', 300, 'cm2'),
        ('big_right_mirror', 'big_right_mirror_holder', 1, 'pieces'),
        ('big_right_mirror', 'camera', 1, 'pieces'),
        ('left_mirror_holder', 'polymer', 1.5, 'kg'),
        ('right_mirror_holder', 'polymer', 1.5, 'kg'),
        ('mid_mirror_holder', 'polymer', 2, 'kg'),
        ('big_left_mirror_holder', 'polymer', 5, 'kg'),
        ('big_right_mirror_holder', 'polymer', 5, 'kg'),
    ]
    boms = [BOM(product_code=p_code, raw_code=r_code, quantity=quantity, unit=unit) for p_code, r_code, quantity, unit in boms_data]
    db.session.add_all(boms)

    db.session.commit()

print("Sample data inserted successfully.")
