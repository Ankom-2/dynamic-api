========================================================================================================================================
Folders and files information:

├── app  # Contains the main application files.
│   ├── __init__.py   # this file makes "app" a "Python package"
│   ├── main.py       # Initializes the FastAPI application.
│   ├── crud
│   │   ├── __init__.py
│   │   ├── crud.py  # Defines CRUD operations for /api/execute-formula.
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── schema.py  # Defines schemas for InputVar, Formulas and Payloads.
│   └── utils
│       ├── __init__.py
│       ├── utility.py  # Defines functions for formula executions and other helper utilities.
│       └── validation.py      # Defines functions for validation.
├── tests
│   ├── __init__.py
│   ├── test_main.py
│
├── requirements.txt
├── .gitignore
└── README.md


========================================================================================================================================
**How the application Works:**

- The code creates a FastAPI application.
- It defines an endpoint that listens for POST requests to "/api/execute-formula.
- When a request arrives, the execute_formula function is called.
- The function processes the payload data (assumed to contain formula information) and executes the formula using the run_formula function.
- The result is returned as the API response.
- The Uvicorn server starts, making the API endpoint accessible.

========================================================================================================================================
**HOW TO RUN THE APPLICATION:**

**Prerequisites:**
Python: Ensure you have Python 3.6 or later installed on your system. You can download it from https://www.python.org/downloads/.

PIP: pip is the package installer for Python. It's usually included with Python installations. You can check if pip is installed by running python -m pip --version in your terminal. If not, installation instructions are available at https://pip.pypa.io/en/stable/installation/.

Setting Up the Environment:
Install Dependencies:
- Open your terminal or command prompt and navigate to the directory containing your project's requirements.txt file. Use the cd command to change directories if needed. Then, run the following command to install all the required dependencies listed in the file:

**Bash**
"pip install -r requirements.txt"
Use code with caution.

This command instructs pip to read the requirements.txt file and install the specified packages and their dependencies. The installation process may take some time depending on the number and size of the packages.

**Running the Application:**
Once the dependencies are installed, navigate to the directory containing the main application file (main.py in your example). Then, execute the following command to start the FastAPI application:
Bash
"python ./main.py"

This command runs the Python script and initiates the FastAPI application. You should see some output in your terminal indicating the server is starting and listening on a specific port (usually 8000 by default).

Accessing the Application:

API Endpoint:
The application should be accessible in your web browser at the following URL:

http://127.0.0.1:8000/
Replace 127.0.0.1 with your machine's IP address if you want to access the application from another device on the same network.

Swagger UI:
FastAPI provides a built-in Swagger UI for interactive exploration and testing of your API endpoints. You can access the Swagger UI at:

http://127.0.0.1:8000/docs
This interface will display the API documentation, allowing you to view available endpoints, their parameters, and expected responses.

Additional Notes:

If you encounter any errors during the installation or startup process, refer to the error messages for more information. These messages can often provide clues about the issue.
You can stop the application running in your terminal by pressing ctrl+c.
By following these steps, you should be able to successfully run and access your FastAPI application.


========================================================================================================================================
SAMPLE INPUTES TO TEST THE APPLICATION:
INPUT 1:
{
  "data": [
    {
      "id": 1,
      "fieldA": 10
    },
    {
      "id": 2,
      "fieldA": 20
    }
  ],
  "formulas": [
    {
      "outputVar": "result",
      "expression": "fieldA + 10",
      "inputs": [
        {
          "varName": "fieldA",
          "varType": "number"
        }
      ]
    }
  ]
}

OUTPUT 1:
{
  "results": {
    "result": [
      20,
      30
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully."
}

=======================================================
INPUT 2:
{
  "data": [
    {
      "id": 1,
      "fieldA": 10,
      "fieldB": 2
    },
    {
      "id": 2,
      "fieldA": 20,
      "fieldB": 3
    }
  ],
  "formulas": [
    {
      "outputVar": "sumResult",
      "expression": "fieldA + fieldB",
      "inputs": [
        {
          "varName": "fieldA",
          "varType": "number"
        },
        {
          "varName": "fieldB",
          "varType": "number"
        }
      ]
    },
    {
      "outputVar": "finalResult",
      "expression": "sumResult * 2 + fieldA",
      "inputs": [
        {
          "varName": "sumResult",
          "varType": "number"
        },
        {
          "varName": "fieldA",
          "varType": "number"
        }
      ]
    }
  ]
}

OUTPUT 2:
{
  "results": {
    "sumResult": [
      12,
      23
    ],
    "finalResult": [
      32,
      63
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully with variable-based chaining."
}

=========================================================
INPUT 3:
{
  "data": [
    {
      "id": 1,
      "product": "Laptop",
      "unitPrice": "1000 USD",
      "quantity": 5,
      "discount": "10%"
    },
    {
      "id": 2,
      "product": "Smartphone",
      "unitPrice": "500 USD",
      "quantity": 10,
      "discount": "5%"
    },
    {
      "id": 3,
      "product": "Tablet",
      "unitPrice": "300 USD",
      "quantity": 15,
      "discount": "0%"
    }
  ],
  "formulas": [
    {
      "outputVar": "revenue",
      "expression": "((unitPrice * quantity) - (unitPrice * quantity * (discount / 100)))",
      "inputs": [
        {
          "varName": "unitPrice",
          "varType": "currency"
        },
        {
          "varName": "quantity",
          "varType": "number"
        },
        {
          "varName": "discount",
          "varType": "percentage"
        }
      ]
    }
  ]
}

OUTPUT 3:
{
  "results": {
    "revenue": [
      4500,
      4750,
      4500
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully."
}
