# Engineering Reflection


# Engineering Reflection

## 1. What assumptions did you make?

I assumed that the three observed read-only portal endpoints—meter search, energy readings, and geographic coordinates—were sufficient to demonstrate the core API-wrapper approach within the available time. I treated the response structures observed in the authenticated browser session as representative, while documenting that the complete API contract and independent Python authentication remain unverified.

## 2. Which part was the most difficult, and how did you get unstuck?

The most difficult part was understanding how the legacy portal exposed its data without published API documentation. I used the browser's developer tools to inspect network requests made while navigating the portal. This helped me identify the meter search, energy, and geographic endpoints and examine their response structures. I then built a small FastAPI service around the observed operations.

## 3. If you had another day, what would you improve?

I would investigate the portal's network hierarchy and additional read-only operations, verify authentication behavior from an independent Python client, and improve upstream error handling. I would also add tests for invalid inputs, upstream failures, and unexpected response structures. If the portal provides a reliable bulk-data path, I would evaluate it before implementing local indexing or caching.

## 4. What mistake did you make while solving this?

I initially focused on implementing the core endpoints before fully validating the complete upstream API contract and authentication behavior. This means that the current tests demonstrate the wrapper's behavior with mocked responses, but do not establish that every live upstream request will work independently of the browser session.

## 5. If you were reviewing your own submission, what would you criticise?

The implementation covers only three observed upstream operations, and the portal's network hierarchy and other sections remain unexplored. Upstream error handling could be more precise, and live integration tests have not been established. The documentation identifies these limitations, but I would prioritise validating authentication, documenting error behavior, and testing against the live portal in a controlled, read-only manner.



