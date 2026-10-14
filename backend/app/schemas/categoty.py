from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the category")
    slug: str = Field(..., min_length=5, max_length=100,
                      description="The slug of the category")

class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique ID of the category")

    class Config:
        form_attributes = True
    