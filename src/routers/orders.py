from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.models.order import OrderCreateRequest, ErrorResponse
from src.validation.dependencies import order_validators

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/create")
async def create_order(
    order: OrderCreateRequest,
    validation_result=Depends(order_validators)
):
    if validation_result:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=validation_result
        )
    # Order creation logic should go here
    return {"status": "success", "order": order.dict()}

@router.post("/express-create")
async def express_create_order(
    order: OrderCreateRequest,
    validation_result=Depends(order_validators)
):
    if validation_result:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=validation_result
        )
    # Express order creation logic should go here
    return {"status": "success", "order": order.dict()}
