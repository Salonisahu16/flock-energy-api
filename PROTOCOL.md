# Flock Energy Portal — Protocol Notes

## 1. Overview

The Flock Energy portal exposes HTTP endpoints for meter search, energy readings, and geographic coordinates.

The endpoints documented here were observed through the browser's developer tools while accessing the portal.

Base URL:

`https://urja-ops.flockenergy.tech`

## 2. Authentication

The browser sends a session cookie named:

`__Secure-better-auth.session_token`

This suggests cookie-based session authentication. Successful authentication from an independent Python client has not yet been verified.

Session cookie values must be treated as secrets and must never be committed to source control.

## 3. Discovered Endpoints

### 3.1 Search meters

**Method:** GET

**Path:** `/portal/meters/search`

Observed query parameters:

* `q`: Search query; an empty value was observed.
* `page`: Page number; page `1` was observed.

**Observed response structure:**

The response contains a `data` array. Each observed meter object contains:

* `meterId`
* `serialNo`
* `make`
* `phaseType`
* `installStatus`
* `dtCode`

Observed installation status examples include `Installed`, `Decommissioned`, and `Faulty`.

### 3.2 Retrieve energy readings

**Method:** GET

**Path:** `/portal/meters/{meter_id}/energy`

An example meter ID observed during inspection was `J100001`.

Each observed reading contains:

* `timestamp`
* `kwh`
* `kvah`
* `voltR`

The timestamp was observed in `DD/MM/YYYY HH:MM` format.

The numeric readings were returned as strings in the inspected response.

### 3.3 Retrieve geographic coordinates

**Method:** GET

**Path:** `/portal/meters/{meter_id}/geo`

The observed response contains a `data` object with:

* `latitude`
* `longitude`

Both coordinate values were returned as strings.

## 4. Observed HTTP Behavior

The three endpoints above returned HTTP `200 OK` in the authenticated browser session during inspection.

This does not establish that unauthenticated requests succeed or that the same behavior has been verified from an independent HTTP client.

## 5. Limitations and Unknowns

The following details have not been fully verified:

* Authentication behavior outside the browser.
* Pagination metadata and the total number of meters.
* Search matching rules and accepted query formats.
* Error response schemas.
* Rate limits and retry behavior.
* The complete API surface of the Ops Desk, Transformer, and Ultra Major Ops sections.

These items should be verified before treating them as supported protocol behavior.
