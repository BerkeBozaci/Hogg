Purchasing Advice Web App
This is a simple Flask web application that calculates purchasing advice based on sales orders, available stock, and bill of materials (BOM). The app displays the purchasing advice in a table format, which can be styled using Bootstrap.

Dependencies
To run the app, you will need to have the following dependencies installed:

Python 3
PostgreSQL
virtualenv (optional, but recommended)
You can install Python 3 and PostgreSQL from their respective official websites. To install virtualenv, you can use pip:

sh
Copy code
pip install virtualenv
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-username/purchasing-advice-web-app.git
cd purchasing-advice-web-app
Create a virtual environment (optional, but recommended):

sh
Copy code
virtualenv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
Install the Python dependencies:

sh
Copy code
pip install -r requirements.txt
Create a PostgreSQL database:

sh
Copy code
createdb hogg_db
Initialize the database:

sh
Copy code
python manage.py db upgrade
python insert_data.py
The insert_data.py script will populate the database with some sample data.

Run the app:

sh
Copy code
python run.py
Open a web browser and go to http://127.0.0.1:5000/ to see the app.

Usage
The app displays a table with the purchasing advice based on the available data. The purchasing advice shows which raw materials should be purchased to fulfill the sales orders based on the BOM and available stock.

You can customize the sales orders, stock, and BOM data by modifying the insert_data.py script. You can also customize the styling of the app by modifying the main.css file.

Docker
Alternatively, you can run the app using Docker. To do so, follow these steps:

Build the Docker image:

sh
Copy code
docker build -t purchasing-advice-web-app .
Run the Docker container:

sh
Copy code
docker run -p 5000:5000 purchasing-advice-web-app
Open a web browser and go to http://localhost:5000/ to see the app.
