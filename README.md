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

## Arazzo Specification

### Authoring the specification

As you may already be aware, Arazzo specification helps tie together operations across several OpenAPI specifications into a workflow.<br>
In line with this we have created minimal Arazzo spec [`location_order_workflow.arazzo.yaml`](./workflow/location_order_workflow.arazzo.yaml), which lists operations from below OpenAPI specs.

1. [order.yaml](workflow/openapi/order.yaml)
2. [location.yaml](workflow/openapi/location.yaml)

To generate a complete Arazzo specification from the aforementioned minimal specification,
execute the Python script found at [`workflow/run.py`](./workflow/run.py) and select the extrapolate option. 

Upon running this script, you will find two new files created in the [`/workflow/output`](./workflow/output) directory:
1. **Extrapolated Specification:** [`location_order_workflow.arazzo_extrapolated.arazzo.yaml`](./workflow/output/location_order_workflow.arazzo_extrapolated.arazzo.yaml)
2. **Generated Inputs File:** [`location_order_workflow.arazzo_extrapolated.arazzo_input.json`](./workflow/output/location_order_workflow.arazzo_extrapolated.arazzo_input.json)

### Validating the Specification

Execute the Python script found at [`workflow/run.py`](./workflow/run.py) and choose the validate option.<br>
This will verify that all parameters, request bodies, schemas, outputs, and actions are accurately defined in accordance with the OpenAPI specifications.<br>
This will also run a loop-test with mocked openApi servers using `specmatic` and generate a full HTML Report at [`workflow/build/reports/specmatic/html/index.html`](./workflow/build/reports/specmatic/html/index.html).

### Modifying Specification Inputs

The generated inputs file located at [`location_order_workflow.arazzo_extrapolated.arazzo_input.json`](./workflow/output/location_order_workflow.arazzo_extrapolated.arazzo_input.json) can be adjusted to align with the dummy data utilized in the backend services. We can introduce additional combinations to encompass all scenarios. 

For instance, the products array being empty or containing one or more products is contingent upon the user and can be represented as follows:

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

### Running the Workflow
To initiate the backend services, first activate the virtual environment and execute the Python script found at [`backend/run.py`](./backend/run.py). <br>
After that, run the Python script located at [`workflow/run.py`](./workflow/run.py) and choose the test option. <br>
This action will initiate the Arazzo Workflow Test and produce an HTML report at [`workflow/build/reports/specmatic/html/index.html`](./workflow/build/reports/specmatic/html/index.html).

### Running the Mock

Execute the Python script located at [`workflow/run.py`](./workflow/run.py) and select the mock option. <br>
Subsequently, start the frontend by running the command `npm run dev -- --open` in the [`frontend`](./frontend/) directory. <br>
When you log in with `specmatic@test.com`, you should see a list of products, while logging in with `another@user.com` will display an empty list.