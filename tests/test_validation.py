import pytest
from src.models.order import OrderCreateRequest, OrderItem
from src.validation.business_rules import check_quantity_limits, check_restricted_items

def test_quantity_limit_rejection():
    order = OrderCreateRequest(customer_id="C1", items=[OrderItem(item_id="A", quantity=150)])
    errors = check_quantity_limits(order)
    assert "items" in errors
    assert len(errors["items"]) == 1
    assert "exceeds limit" in errors["items"][0]["error"]

def test_restricted_item_rejection():
    order = OrderCreateRequest(customer_id="C2", items=[OrderItem(item_id="HAZMAT01", quantity=1)])
    errors = check_restricted_items(order)
    assert "items" in errors
    assert len(errors["items"]) == 1
    assert "restricted" in errors["items"][0]["error"]
