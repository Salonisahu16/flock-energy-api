# Engineering Reflection

## 1. What I Built

I built a Python API client and a FastAPI wrapper for three observed Flock Energy portal operations: meter search, energy readings, and geographic coordinates.

I used HTTPX for HTTP requests and Pydantic models to validate and normalize upstream responses.

## 2. Key Design Decisions

* **HTTPX:** Used to make HTTP requests to the upstream portal.
* **FastAPI:** Used to expose the operations through REST endpoints.
* **Pydantic:** Used to validate response structures and convert numeric strings into numeric values.
* **Environment variables:** Used to keep session credentials outside the source code.
* **Pytest:** Used to test the wrapper with mocked upstream methods.

## 3. Assumptions

The implementation is based on endpoints and response fields observed in the authenticated browser session.

I assumed the observed response structures are representative of the responses returned by those endpoints. However, the complete upstream API contract and independent Python authentication have not been verified.

## 4. Trade-offs

Given the limited implementation time, I prioritized three read-only operations that could be observed and documented with confidence.

I did not attempt to reproduce the entire portal or infer undocumented endpoints. This limited the scope but reduced unsupported assumptions.

## 5. Testing

The current test suite covers the health endpoint, meter search, energy readings, and geographic coordinates.

Upstream methods are mocked in the tests. Therefore, the tests validate the wrapper's expected behavior but do not prove that live upstream requests will always succeed.

## 6. Limitations

* Independent Python authentication has not been verified.
* Pagination metadata and search matching rules are not fully documented.
* Rate limits and retry behavior are unknown.
* Upstream error response formats have not been fully investigated.
* Additional portal sections have not been fully explored.

## 7. Future Improvements

* Improve upstream HTTP error handling.
* Add tests for missing fields, invalid meter IDs, and upstream failures.
* Verify authentication and unauthorized-response behavior.
* Confirm pagination behavior and document error response formats.
* Investigate additional endpoints if the assignment requires broader coverage.

## 8. Key Learning

This exercise reinforced the importance of separating observed facts from assumptions, keeping credentials out of source control, validating external API responses, and documenting unknowns rather than inventing undocumented behavior.
