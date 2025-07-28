## Task Overview
A logistics company’s FastAPI backend for order management currently has duplicated, scattered business rule validations. You are tasked to refactor the service, centralizing order creation validations and enforcing consistent, structured error responses for business rules like item restrictions and quantity limits. 

## Guidance  
- The system is an order management API built with FastAPI and Pydantic, relying on Docker for deployment.
- A modular architecture, using routers, Pydantic models, and dependency injection, is preferred.
- All business rule validations for order creation must be centralized and chainable to ensure ease of future evolution and uniformity of enforcement.
- Validation errors should be returned in a structured, field-specific manner suitable for frontend consumption.
- The validators must be applied to all endpoints that create orders, regardless of route.
- Dockerization is essential for reproducibility.

## Objectives
- Centralize business rule checks for order creation (quantity limits, restricted items, at a minimum), using Pydantic models and/or FastAPI dependency injection.
- Ensure at least two distinct business rules are consistently validated for all order creation API endpoints.
- Structure error responses so that they are field-specific and detailed.
- Uniformly apply your validators to order creation endpoints using routers.
- Maintain code modularity and extensibility with a clear separation of validation logic, routing, and business models.
- Provide a containerized solution ready for reproducible deployment.

## How to Verify
- Attempt to create orders that violate individual or multiple business rules, and observe that error responses are uniform, field-specific, and detailed.
- Validate that all order creation endpoints enforce the same business rules regardless of endpoint path or source.
- Review code structure to confirm validators are not scattered in each route but are centralized and modular.
- Ensure the solution builds and runs successfully using Docker, confirming reproducibility and maintainability.