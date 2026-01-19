
```markdown
# Power BI Integration

## Overview
SolarWinds Service Desk integrates with Microsoft Power BI to enable advanced reporting, data visualization, and long-term trend analysis. This functionality is delivered through a specific Connector (V113) and pre-built Dashboard templates.

## Connector Capabilities (V113)
The "SolarWinds Service Desk" connector enables the incremental import of data using Token Authentication.
- **Supported Records:** Incidents and Assets (Computers, Mobile, Network Devices, Printers, Software).
- **Filtering:** Optimized using `RangeStart` and `RangeEnd` parameters against `updated_at` (Server Time Zone). Note that Server Time Zone may differ from the Account Time Zone.
- **Custom Fields:** Ingestion is possible by defining a `CustomFieldNames` parameter with a comma-separated list of field names.
- **Data Access:** Exposes "API Only" fields (e.g., internal IDs) not visible in the standard UI.

## Dashboard Templates
Two methods exist for setting up visualization:
1. **Microsoft AppSource:** A plug-and-play app.
2. **Power BI Desktop (.pbix):** A customizable file.

**Standard KPIs:**
- CSAT and SLA scores
- MTTR (Mean Time To Resolve)
- Open ticket age
- Asset status metrics (e.g., % Operational vs. Broken)

## Authentication & Security
- **Connector:** Uses Token Authentication.
- **Dashboard Templates:** Requires a JSON Web Token (JWT) generated from the Service Desk User Profile.
  - **Constraint:** This token expires every 24 hours and must be manually refreshed.

## Limitations & Constraints
- **Latency:** The connector is not real-time; it requires scheduled or manual refreshes.
- **Rate Limiting:** Full data refreshes (>1 year) are limited to once per 24 hours per user if Incremental Refresh is not configured.
- **Dashboard Template Limits:** The default templates do not support custom fields, incremental web refresh, or mobile layouts.
- **Migration:** Upgrading from the BETA connector requires manually updating Power Query to `SolarWindsServiceDesk.ContentsV113` to access historical data beyond the last month.
```
