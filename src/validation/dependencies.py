from fastapi import Request
from src.models.order import OrderCreateRequest
from src.validation.business_rules import check_quantity_limits, check_restricted_items

def order_validators(order: OrderCreateRequest, request: Request):
    errors = {}
    quantity_result = check_quantity_limits(order)
    restricted_result = check_restricted_items(order)

    if quantity_result.get("items"):
        errors.setdefault("items", []).extend(quantity_result["items"])
    if restricted_result.get("items"):
        errors.setdefault("items", []).extend(restricted_result["items"])

    if errors:
        return {"detail": "Order validation failed", "fields": errors}
    return None
