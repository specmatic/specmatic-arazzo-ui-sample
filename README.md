# Arazzo UI Sample Project

This project includes two microservices and a frontend web application:
- [**Order API**](./backend/order_api)
- [**Location API**](./backend/location_api)
- [**Frontend Application**](./frontend)

All services are developed using **FastAPI**, **SQLModel**, and **SQLite** as the database system. The frontend is constructed using **Svelte** and **Vite**.

## Running the Project

The entire setup and execution of services, along with the frontend, can be automated by running [`run.py`](./run.py). This script will:

1. In the [`backend`](./backend/) directory:
   1. Create a `venv` virtual environment.
   2. Install Python dependencies from [`requirements.txt`](./backend/requirements.txt).
   3. Start both the [`order_api`](./backend/order_api/) and [`location_api`](./backend/location_api/) microservices.
   4. Populate the database with dummy data.

2. In the [`frontend`](./frontend/) directory:
   1. Install the frontend dependencies specified in [`package.json`](./frontend/package.json).
   2. Launch the frontend application in development mode using Vite.
   3. Open the frontend in a web browser.

## Arazzo Specification

The Minimal Arazzo Specification is available at [`./workflow/location_order_workflow.arazzo.yaml`](./workflow/location_order_workflow.arazzo.yaml), which includes the essential components for extrapolation. 
To execute operations based on this specification, run the Python script located at [`workflow/run.py`](./workflow/run.py), which will provide you with a menu of options.
