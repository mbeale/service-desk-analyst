
```markdown
# Enterprise Service Management (ESM)

## Overview
ESM allows a single Service Desk account to support multiple distinct service providers (e.g., IT, HR, Facilities) with strict data segregation. This feature transforms the platform from a single-tenant ITSM tool into a multi-departmental service platform.

## Licensing
*   **Availability**: Restricted to **Advanced** and **Premier** subscription plans.

## Architecture: Organization vs. Service Provider
The data model splits configuration into two levels:
1.  **Organization Level**: Global settings, Users, and Groups. Managed centrally.
2.  **Service Provider Level**: Specific resources, Roles, and Permissions.

## User Management
*   **Centralized**: Users and Groups are defined at the Organization level.
*   **Contextual**: Roles and permissions are applied within each specific Service Provider.

## Migration Behavior
When enabling ESM on an existing single-tenant instance, the system automatically creates a default **"IT Service Provider"**. All legacy data and history are moved to this provider to ensure continuity.

## UX Considerations
*   **Virtual Agent**: Requires users to select a specific Service Provider context before the workflow can proceed with assistance.
```

```markdown
## Service Provider Administration
- **Access Control**: Only Organization Administrators can create, enable, or disable service providers.
- **Creation Templates**:
    - **Blank**: Default settings only.
    - **Sample**: Includes generic incidents and service catalog items.
    - **Specific**: Pre-configured templates for HR or Facilities.
- **Configuration Constraints**:
    - **URL Prefix**: Limited to 10 alphanumeric characters (A-Z, 0-9).
    - **Limits**: Subscription plans may enforce a cap on the number of active service providers.
- **Management Features**:
    - **Duplication**: Existing service providers can be cloned to replicate configurations.
    - **Inter-Service Operations**: Tickets can be forwarded between service providers (requires enablement).
```

```markdown
## Migration Mechanics
**Transition from Standard ITSM to ESM**
- **Irreversibility**: The conversion process is permanent; accounts cannot revert to single-tenant ITSM mode.
- **Downtime**: Migration requires system downtime, typically <4 hours, but up to 12 hours for accounts with large datasets.

### Architectural Impact
- **Hierarchy Shift**: A new "Organization" entity is created above the service providers.
  - **URLs**: The legacy ITSM URL becomes the URL for the specific IT Service Provider. A new Organization URL is generated (e.g., `org-acme.samanage.com`).
  - **User Management**: SSO, User Provisioning, and MFA settings are elevated to the Organization level.
  - **Governance**: (Inference) This centralization implies a shift in governance, potentially reducing administrative autonomy for individual service providers compared to the standalone model.

### Technical Requirements & Risks
- **Custom Domains**: specific DNS records (`org.domain.com`) and multi-domain/wildcard certificates are required.
- **Integrations**: Hardcoded references to `field_id` in API integrations may break; scripts must be updated to use field names.
- **Re-authentication**: Users of integrated tools (Slack, MS Teams) may require re-authentication post-migration.
```
