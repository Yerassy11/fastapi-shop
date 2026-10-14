from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session  
from ..database import get_db
from typing import List
from ..schemas.cart import CartResponse,CartItemCreate,CartItemUpdate
from ..services.cart_service import  CartService
from pydantic import BaseModel

router=APIRouter(
    prefix="api/cart",
    tags=["cart"]
)

class AddToCartRequest(BaseModel):
    product_id:int
    quantity:int
    cart: dict[int,int] = {}

class UpdateCartRequest(BaseModel):
    product_id:int
    quantity:int
    cart: dict[int,int]

class RemoveFromCartRequest(BaseModel):
    cart: dict[int,int]

@router.post("/add",status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest,db: Session = Depends(get_db)):
    service = CartService(db)
    return service.add_to_cart(request.cart,request.product_id,request.quantity)


@router.post("",status_code=status.HTTP_200_OK)
def get_cart(cart_dats:dict[int,int] ,db: Session = Depends(get_db)):
    service = CartService(db)
    return service.get_cart_items(cart_dats)


@router.put("/update",status_code=status.HTTP_200_OK)
def update_cart_item(request:UpdateCartRequest,db: Session = Depends(get_db)):
    service = CartService(db)
    updated_cart = service.update_cart_item(request.cart,request.product_id,request.quantity)
    return {"cart":updated_cart}


@router.delete("/remove/product_id",status_code=status.HTTP_200_OK)
def remove_from_cart(product_id: int,request:RemoveFromCartRequest,db: Session = Depends(get_db)):
    service = CartService(db)
    updated_cart = service.remove_from_cart(request.cart,product_id)
    return {"cart":updated_cart}