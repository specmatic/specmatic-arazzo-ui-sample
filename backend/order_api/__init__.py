from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from pydantic import ValidationError
from sqlmodel import Session, SQLModel, create_engine

from order_api.config import Config

config = Config()  # pyright: ignore[reportCallIssue]
connect_args = {"check_same_thread": False}
engine = create_engine(config.ORDER_DATABASE_URI, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield


SessionDep = Annotated[Session, Depends(get_session)]
api_key_auth = APIKeyHeader(name="clientToken", scheme_name="ApiKeyAuth")
app = FastAPI(lifespan=lifespan, dependencies=[Depends(api_key_auth)])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
@app.exception_handler(RequestValidationError)
def handle_validation_error(_, e: "RequestValidationError|ValidationError"):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Bad Request",
            "message": str(e),
        },
    )


@app.exception_handler(HTTPException)
def http_error_handler(_, e: "HTTPException"):
    return JSONResponse(
        status_code=e.status_code,
        content={
            "error": e.__class__.__name__,
            "message": e.detail,
        },
    )


from .orders.routes import orders  # noqa: E402
from .products.routes import products  # noqa: E402

app.include_router(products)
app.include_router(orders)
