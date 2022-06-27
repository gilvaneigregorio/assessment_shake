Gilvanei Gregório
# Shake Assessment
## Technologies
* Python
* FastAPI
* SQLLite
* OpenAPI
All dependencies in requirements.txt

## Description
To develop this assessment I used FastAPI and the basics libs I use put together.

I created 2 routers, Auth router with needed endpoints to Login and SignUp, using OAth2, JWT, and SQLite. The point
in using SQLite as the database, is use a production-ready, database and authentication method, instead of using 
a simple authentication method that doesn't available inserts new users.

For Currency, Currency Router with the endpoints required in the assessment document, List all available 
Currencies and Convert values. I was confused about whether you are waiting for a currency conversion implementation or using an external
service. I used an external service in the endpoint. In order
to grant the same inputs and output, I used ABC to create an interface, which works as a contract between the 
implementations and follows DIP by SOLID Principles.

Still, about the controller pattern, I used CurrencyDataAPI as the currency service, it has a 100 request per month limit in the free plan, which I selected. 
The API raises an exception if you pass this limit.
I made everything very lean, and for this assessment, I decided for do not to implement a service pattern.

I put all the environments in an external file as 12 factor says, .env, if for some reason it's not available for you,
you can fix it by creating a .env on the root of the project and past these lines.
APP_PORT=8042
CURRENCY_DATA_API_KEY=lW7B5ZUHNxxm39YsjKlc5SZ9gQLvgF1O
DATABASE_URI=sqlite:///shake.db
>> **I'm puting it here, just to ensure everything will works properly**

I'm also committing a basic database file(shake.db) which contains already one user registered. You can use him to access
the protectd endpoins.
USERNAME=user@example.com
PASSWORD=string

>> **In case of any question, please contact me gilvaneigregorio92@gmail.com**

### Run Test
Go to the root of the project and run
```TODO```

### Run Project
Go to the root of the project and run
```pip install -r requirements.txt```
```cd src```
```python main.py```

### Link API Documentation
After run the project, this link become available for watch the endpoints, paths, parameters and run tests.
http://127.0.0.1:8042/docs

### Configuration files
* .env
