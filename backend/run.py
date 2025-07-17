import pathlib
import signal
import subprocess
import sys
from time import sleep

from sqlmodel import Session, SQLModel, create_engine

from location_api.models import User
from order_api.models import Product

BASE_DIR = pathlib.Path(__file__).parent
ORDER_DB_PATH = BASE_DIR / "order.db"
LOC_DB_PATH = BASE_DIR / "location.db"
order_engine = create_engine(f"sqlite:///{ORDER_DB_PATH}", connect_args={"check_same_thread": False})
location_engine = create_engine(f"sqlite:///{LOC_DB_PATH}", connect_args={"check_same_thread": False})
engines = [order_engine, location_engine]


def initialize_database():
    for engine in engines:
        SQLModel.metadata.create_all(engine)

    products = [
        Product(id = 1, name="Phone", price=999, quantity=500, shipping_zone="A"),
        Product(id = 2, name="TWS", price=499, quantity=1000, shipping_zone="A"),
    ]

    users = [
        User(id = 1, email="specmatic@test.com", password="specmatic", shipping_zone="A", country="IN", region="HYD"),  # noqa: S106
        User(id = 2, email="another@user.com", password="user", shipping_zone="B", country="IN", region="DEL"),  # noqa: S106
    ]

    with Session(order_engine) as session:
        session.add_all(products)
        session.commit()

    with Session(location_engine) as session:
        session.add_all(users)
        session.commit()


def remove_databases():
    for engine in engines:
        engine.dispose()

    for db_path in [ORDER_DB_PATH, LOC_DB_PATH]:
        db_path.unlink(missing_ok=True)


def terminate_processes(processes):
    for process in processes:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

    sleep(1)
    remove_databases()


def handle_shutdown(signum, frame):
    terminate_processes(active_processes)
    sys.exit(0)


if __name__ == "__main__":
    remove_databases()
    initialize_database()
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    services = {
        "UUID Service": [
            sys.executable, "-m", "uvicorn", "location_api:app", "--host", "127.0.0.1", "--port", "5000"
        ],
        "Order Service": [
            sys.executable, "-m", "uvicorn", "order_api:app", "--host", "127.0.0.1", "--port", "3000"
        ],
    }

    active_processes = [subprocess.Popen(command, cwd=BASE_DIR) for command in services.values()]  # noqa: S603
    try:
        for process in active_processes:
            process.wait()
    except KeyboardInterrupt:
        handle_shutdown(None, None)
