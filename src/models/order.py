from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    item_id: str = Field(..., description="Unique item ID")
    quantity: int = Field(..., gt=0, description="Requested quantity, must be positive")

class OrderCreateRequest(BaseModel):
    customer_id: str = Field(..., description="ID of the customer placing the order")
    items: List[OrderItem]

class ErrorResponse(BaseModel):
    detail: str
    fields: dict
