
```markdown
# MSP Mode Capabilities & Architecture

## Tenant Architecture
- **Structure**: Hub-and-spoke model. The MSP account acts as the parent, with client accounts functioning as separate, fully licensed tenants.
- **Isolation**: Strict tenant isolation; no direct access or data leakage between client accounts.
- **Federation**: MSP accounts provide a unified view of incidents and service requests across all client tenants.

## Licensing & Limits
- **Advanced Plan**: Limit of 15 client accounts.
- **Premier Plan**: Unlimited client accounts.
- **Attachment**: Existing SWSD ITSM accounts *cannot* be attached to an MSP account; clients must be created new.

## Role Management
- **Admins**: MSP Administrators inherit the Administrator role in all client accounts.
- **Agents**: MSP Agents are added to client accounts with *no defined role* by default to ensure least-privilege access.

## Configuration Syncing
- **Direction**: One-way sync from MSP to Client.
- **Scope**: Groups and Queues created in the MSP account automatically sync to all client accounts.
- **Locking**: Synced items cannot be modified at the client level.
- **Deletion**: Deleting a Group/Queue in the MSP account removes it from all clients.

## Current Limitations
- **ESM**: Enterprise Service Management is not supported on client accounts.
- **Mobile**: The Service Desk mobile app does not support MSP client accounts.
```
