
# Incident Management

## Classification & Routing
- **Hierarchy**: Incidents, service requests, changes, and solutions are classified using a two-level hierarchy (Category > Subcategory).
- **Auto-Routing**: Categorization drives the automatic routing of tickets to default assignees (users or queues) or default groups.
- **Dropbox Emails**: Specific categories can be mapped to unique email addresses (e.g., `NetworkHelp@domain.com`) to automatically assign category, priority, and assignee upon receipt.
  - **Configuration**: Managed under `Setup > Service Desk > Categories`.
  - **Aliases**: Can use system defaults, custom subdomains (`{account}.samanage.com`), or verified custom domains.
- **Maintenance**:
  - Renaming a category retroactively updates historical tickets.
  - Deleting a category removes it from active selection but preserves historical data for reporting.
  - Visibility can be restricted via Roles and Permissions.

## Service Level Agreements (SLA)
- **Targets**: SLAs define target times (e.g., "Time to Assign", "Time to Resolve") based on defined Business Hours.
- **Breach Actions**: On breach, the system can automatically change priority, re-assign the ticket, send notifications, or add tags.
- **Behavior**: SLA timers start at incident creation and do not restart if the ticket is recategorized.

## Incident States
- Standard states include: New, Assigned, In Progress, Awaiting User, Resolved, Closed.
- **Forwarded**: A specific state used in ESM environments when a ticket is transferred to another Service Provider (an irreversible action).

## Features
- **Response Templates**:
  - Available to Advanced/Premier plans.
  - **Global Templates**: Created by Admins.
  - **Personal Templates**: Created by Agents.
  - Supports variables (e.g., `{{requester_full_name}}`).
- **Chat**: Agents can handle multiple simultaneous sessions and convert chat logs directly into incidents.
- **Satisfaction Surveys**: Triggered exclusively when an incident moves to the "Resolved" state.
