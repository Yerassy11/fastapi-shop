from sqlalchemy.orm import Session
from typing import Dict
from ..repositories.product_repository import ProductRepository
from ..schemas.cart import CartResponse, CartItem, \
                           CartItemCreate, CartItemUpdate
from fastapi import HTTPException, status

class CartService:
    def __init__(self, db: Session):
        self.db = db
        self.product_repository = ProductRepository(self.db)

    def add_to_cart(self,cart_data:dict[int,int],item:CartItemCreate) ->Dict[int,int] | CartResponse:
        product = self.product_repository.get_by_id(item.product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        if item.product_id in cart_data:
            cart_data[item.product_id] += item.quantity
        else:
            cart_data[item.product_id] = item.quantity

        return cart_data

    def update_cart_item(self, cart_data: dict[int, int], item: CartItemUpdate) -> Dict[int, int] | CartResponse:
        if item.product_id not in cart_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not in cart")

        if item.quantity <= 0:
            del cart_data[item.product_id]
        else:
            cart_data[item.product_id] = item.quantity

        return cart_data

    def remove_from_cart(self,cart_data:dict[int,int],product_id:int) -> Dict[int,int] | CartResponse:
        if product_id not in cart_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not in cart")
        del cart_data[product_id]
        return cart_data

    def get_cart_items(self, cart_data: dict[int, int]) -> CartResponse:
        if not cart_data:
            return CartResponse(items=[], total_price=0.0)
        product_ids = list(cart_data.keys())
        products = self.product_repository.get_multiple_by_ids(product_ids)

        product_dict = {product.id: product for product in products}

        cart_items = []
        total_price = 0.0
        total_items = 0

        for product_id, quantity in cart_data.items():
            if product_id in product_dict:
                product = product_dict[product_id]
                sub_total = product.price * quantity
                cart_items.append(CartItem(product_id=product.id, name=product.name, price=product.price, quantity=quantity, sub_total=sub_total,image_url=product.image_url))
                total_price += sub_total
                total_items += quantity

        return CartResponse(items=cart_items, total_price=round(total_price), items_count=total_items)