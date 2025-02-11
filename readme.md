
## How the Application Works

- The application creates a FastAPI instance.
- It defines an endpoint that listens for POST requests to `/api/execute-formula`.
- When a request arrives, the `execute_formula` function processes the payload data and executes the formula using the `run_formula` function.
- The result is returned as the API response.
- The Uvicorn server starts, making the API endpoint accessible.

## How to Run the Application

### Prerequisites

- **Python**: Ensure you have Python 3.6 or later installed. [Download Python](https://www.python.org/downloads/).
- **PIP**: Ensure pip is installed. Check with `python -m pip --version`. [Install pip](https://pip.pypa.io/en/stable/installation/).

### Setting Up the Environment

1. **Install Dependencies**:
   - Open your terminal and navigate to the project directory.
   - Run the following command to install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

### Running the Application

1. **Start the FastAPI Application**:
   - Navigate to the directory containing `main.py`.
   - Run the following command:

     ```bash
     python ./main.py
     ```

   - The server should start, and you will see output indicating it is listening on port 8000.

### Accessing the Application

- **API Endpoint**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Additional Notes

- If you encounter errors, refer to the error messages for more information.
- Stop the application by pressing `Ctrl+C` in the terminal.

## Sample Inputs to Test the Application

### Input 1

```json
{
  "data": [
    { "id": 1, "fieldA": 10 },
    { "id": 2, "fieldA": 20 }
  ],
  "formulas": [
    {
      "outputVar": "result",
      "expression": "fieldA + 10",
      "inputs": [
        { "varName": "fieldA", "varType": "number" }
      ]
    }
  ]
}
```
### Output 1
```
{
  "results": { "result": [20, 30] },
  "status": "success",
  "message": "The formulas were executed successfully."
}
```

### Input 2
```
{
  "data": [
    { "id": 1, "fieldA": 10, "fieldB": 2 },
    { "id": 2, "fieldA": 20, "fieldB": 3 }
  ],
  "formulas": [
    {
      "outputVar": "sumResult",
      "expression": "fieldA + fieldB",
      "inputs": [
        { "varName": "fieldA", "varType": "number" },
        { "varName": "fieldB", "varType": "number" }
      ]
    },
    {
      "outputVar": "finalResult",
      "expression": "sumResult * 2 + fieldA",
      "inputs": [
        { "varName": "sumResult", "varType": "number" },
        { "varName": "fieldA", "varType": "number" }
      ]
    }
  ]
}
```

### Output 2
```
{
  "results": {
    "sumResult": [12, 23],
    "finalResult": [32, 63]
  },
  "status": "success",
  "message": "The formulas were executed successfully with variable-based chaining."
}
```

### Input 3

```
{
  "data": [
    { "id": 1, "product": "Laptop", "unitPrice": "1000 USD", "quantity": 5, "discount": "10%" },
    { "id": 2, "product": "Smartphone", "unitPrice": "500 USD", "quantity": 10, "discount": "5%" },
    { "id": 3, "product": "Tablet", "unitPrice": "300 USD", "quantity": 15, "discount": "0%" }
  ],
  "formulas": [
    {
      "outputVar": "revenue",
      "expression": "((unitPrice * quantity) - (unitPrice * quantity * (discount / 100)))",
      "inputs": [
        { "varName": "unitPrice", "varType": "currency" },
        { "varName": "quantity", "varType": "number" },
        { "varName": "discount", "varType": "percentage" }
      ]
    }
  ]
}
```

### Output 3
```
{
  "results": { "revenue": [4500, 4750, 4500] },
  "status": "success",
  "message": "The formulas were executed successfully."
}
```
