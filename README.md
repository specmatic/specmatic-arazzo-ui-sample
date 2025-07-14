# Arazzo UI Sample Project

This project includes below components:
- Backend Services (developed using **FastAPI**, **SQLModel**, and **SQLite**)
  - [**Order API**](./backend/order_api)
  - [**Location API**](./backend/location_api)
- Frontend (built using **Svelte** and **Vite**)
  - [**UI that interacts with the two backend services**](./frontend)

## Diagram of the workflow

TODO

## Running the Project

Execute [`run.py`](./run.py) to get both Front-end and Back-end running.
Please choose appropriate commands below as per your system setup.

```shell
python run.py
```

OR 

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

# Arazzo Specification

## Authoring the specification

As you may already be aware, Arazzo specification helps tie together operations across several OpenAPI specifications into a workflow.
In line with this we have created minimal Arazzo spec [`./workflow/location_order_workflow.arazzo.yaml`](./workflow/location_order_workflow.arazzo.yaml), which lists operations from below OpenAPI specs.
1. [order.yaml](workflow/openapi/order.yaml)
2. [location.yaml](workflow/openapi/location.yaml)

To create a full Arazzo spec from the minimal spec mentioned above, run the Python script located at [`workflow/run.py`](./workflow/run.py) and select the extrapolate option.

Now you will see a full Arazzo spec generated along with the input JSON (TODO: add links for the files).