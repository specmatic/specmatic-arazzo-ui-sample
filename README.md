[![Visual API Workflow Mocking and Testing with Specmatic and Arazzo API Specifications](https://img.youtube.com/vi/jrkFKh37_N0/hqdefault.jpg)](https://youtu.be/jrkFKh37_N0)

# Arazzo UI Sample Project

This project includes below components:
- Backend Services (developed using **FastAPI**, **SQLModel**, and **SQLite**)
  - [**Order API**](./backend/order_api)
  - [**Location API**](./backend/location_api)
- Frontend (built using **Svelte** and **Vite**)
  - [**UI that interacts with the two backend services**](./frontend)

## Architecture / Flow

![Diagram](./assets/flow.svg)

## Running the Project

Execute [`run.py`](./run.py) to get both Front-end and Back-end running.
Please choose appropriate commands below as per your system setup.

For Windows:
```shell
python run.py
```

For Unix:
```shell
python3 run.py
```

### What does `run.py` do?

1. In the [`backend`](./backend/) directory:
   1. Creates a `venv` virtual environment.
   2. Installs Python dependencies from [`requirements.txt`](./backend/requirements.txt).
   3. Starts both the [`order_api`](./backend/order_api/) and [`location_api`](./backend/location_api/) microservices.
   4. Populates the database with dummy data.

2. In the [`frontend`](./frontend/) directory:
   1. Installs the frontend dependencies specified in [`package.json`](./frontend/package.json).
   2. Launches the frontend application in development mode using Vite.
   3. Opens the frontend in a web browser.

### Verify the setup
1. In the [UI](http://localhost:5173) please use username as `specmatic@test.com` and password as `specmatic`. This should show you a couple of products.
2. Now you can log out and try again with username as `another@user.com` and password as `user`. This shows you an empty list.

### Input for backend workflow testing

```json
{
    "PlaceOrder": {
        "DEFAULT": {
            "GetUserDetails": {
                "email": "specmatic@test.com",
                "password": "specmatic",
                "internalToken": "API-TOKEN"
            }
        },
        "RetrieveProducts.IsArrayEmpty": {
            "$failureMessage": "Expected not to find any products for another@user, as they belong to B Zone",
            "GetUserDetails": {
                "email": "another@user.com",
                "password": "user"
            }
        }
    }
}
```