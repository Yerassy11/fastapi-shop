from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .categoty import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100,
                      description="The name of the product")

    description: Optional[str] = Field(None, max_length=300,
                                            description="The description of the product")

    price: float = Field(..., gt=0, description="The price of the product")

    category_id: int = Field(..., description="The ID of the category the product belongs to")

    image_url : Optional[str] = Field(None, description="The URL of the product image")


class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id : int = Field(..., description="Unique ID of the product")

    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=300)

    price: float = Field(..., gt=0)

    category_id : int
    image_url : Optional[str] = Field(None, description="The URL of the product image")

    created_at: datetime
    category: CategoryResponse = Field(..., description="The category the product belongs to")

    class Config:
        form_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(..., description="List of products")
    total: int = Field(..., description="Total number of products")
    page: int = Field(..., description="Current page number")
    size: int = Field(..., description="Number of products per page")

    class Config:
        form_attributes = True