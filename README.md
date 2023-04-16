# Flask Purchasing Advice Web Application #
This is a Flask web application that calculates and displays purchasing advice based on sales orders, current stock levels, and bills of materials (BOMs).

## Requirements ##
To run this web application, you will need the following:

* Python 3.7 or higher
* Flask
* Flask SQLalchemy
* PostgreSQL
* Docker

## Installation ##
### 1. Clone the Repository ###
Clone this repository to your local machine using the following command:


`git clone https://github.com/[USERNAME]/[REPOSITORY-NAME].git`

### 2. Set Up a Virtual Environment (Optional) ###
You can set up a virtual environment for this project by running the following commands in the project directory:


`python3 -m venv venv`
<br> `source venv/bin/activate`
### 3. Install Dependencies ###
Install the required Python packages by running the following command in the project directory:

`pip install -r requirements.txt`
### 4. Set Up the Database ###
Create a PostgreSQL database named hogg_db and a user named postgres with the password postgres. You can use any other username and password, but be sure to update the SQLALCHEMY_DATABASE_URI value in the config.py file accordingly.

Then, create the required tables in the database by running the following command:


`flask db upgrade`

### 5. Insert Sample Data ###
Insert sample data into the database by running the following command:


`python insert_data.py`
### 6. Start the Application ###
You can start the application by running the following command in the project directory:


`python run.py`
Alternatively, you can build and run the Docker image by running the following commands in the project directory:


`docker build -t [DOCKER-IMAGE-NAME] .`
<br>`docker run -p 5000:5000 [DOCKER-IMAGE-NAME]`
## Usage ##
Once the application is running, you can access it by visiting http://127.0.0.1:5000 in your web browser. The main page will display a table of purchasing advice based on the sample data in the database.
