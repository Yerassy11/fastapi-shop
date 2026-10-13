from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id=Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url = Column(String)
    created_at = Column(String, default=datetime.utcnow().isoformat( ))

    category = relationship("Category", back_populates="products")


    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"