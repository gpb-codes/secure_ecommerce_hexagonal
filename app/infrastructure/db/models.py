from sqlalchemy import Column, String, Numeric, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductModel(Base):
    __tablename__= "products"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    active = Column(Boolean, default=True)
