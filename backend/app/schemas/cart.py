from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    quantity: int = Field(..., gt=0, description="The quantity of the product in the cart")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="The ID of the cart item to update")
    quantity: int = Field(..., gt=0, description="The new quantity of the product in the cart")

class CartItem(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    name : str = Field(..., description="The name of the product")
    price : float = Field(..., description="The price of the product")
    quantity: int = Field(..., description="The quantity of the product in the cart")
    subtotal: float = Field(...,description="The subtotal for this cart item (price * quantity)")
    image_url: Optional[str] = Field(None, description="The URL of the product image")


class CartResponse(BaseModel):
    items : list[CartItem] = Field(..., description="List of items in the cart")
    total: float = Field(..., description="Total price of all items in the cart")
    items_count: int = Field(..., description="Total number of items in the cart")