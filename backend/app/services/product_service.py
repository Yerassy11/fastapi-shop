from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories.product_repository import ProductRepository
from ..schemas.product import ProductCreate, ProductResponse,ProductListResponse
from ..repositories.categoty_repository import CategoryRepository

class ProductService:
    def __init__(self, db: Session):
        self.db = db
        self.product_repository = ProductRepository(self.db)
        self.category_repository = CategoryRepository(self.db)

    def get_all_products(self) -> list[ProductResponse]:
        products = self.product_repository.get_all()
        product_responses = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=product_responses, total=len(product_responses), page=1, size=len(product_responses))

    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return ProductResponse.model_validate(product)

    def get_products_by_category(self, category_id: int) -> list[ProductResponse]:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        products = self.product_repository.get_by_category(category_id)
        product_responses = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=product_responses, total=len(product_responses), page=1, size=len(product_responses))

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.category_repository.get_by_id(product_data.category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category not found")
        product = self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)

    
