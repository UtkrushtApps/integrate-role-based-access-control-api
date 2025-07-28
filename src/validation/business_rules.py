from src.models.order import OrderCreateRequest

def check_quantity_limits(order: OrderCreateRequest) -> dict:
    errors = {}
    max_quantity = 100  # business rule: no item may exceed this
    for item in order.items:
        if item.quantity > max_quantity:
            errors.setdefault("items", []).append({
                "item_id": item.item_id,
                "quantity": item.quantity,
                "error": f"Quantity {item.quantity} exceeds limit {max_quantity}"
            })
    return errors

def check_restricted_items(order: OrderCreateRequest) -> dict:
    errors = {}
    restricted = {"HAZMAT01", "PROHIBITED02"}
    for item in order.items:
        if item.item_id in restricted:
            errors.setdefault("items", []).append({
                "item_id": item.item_id,
                "error": f"Item {item.item_id} is restricted and cannot be ordered."
            })
    return errors
