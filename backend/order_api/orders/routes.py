from fastapi import APIRouter, HTTPException
from sqlmodel import select

from order_api import SessionDep
from order_api.models import Order, OrderBase, OrderPublic, Product

orders = APIRouter()


@orders.post("/orders", response_model=OrderPublic, status_code=201)
async def create_order(order: OrderBase, session: SessionDep):
    product_exists = session.exec(select(Product).where(Product.product_id == order.product_id)).first()
    if not product_exists:
        raise HTTPException(status_code=404, detail=f"Product with id {order.product_id} not found")
    if product_exists.quantity < order.quantity:
        raise HTTPException(status_code=400, detail=f"Product with id {order.product_id} is out of stock")

    db_order = Order.model_validate(order)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order
