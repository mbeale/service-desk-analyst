
# Platform Customization

## Custom Forms
- **Purpose**: Serve as location identifiers and containers for displaying custom fields.
- **Logic**: Supports conditional behavior (hide, display, require fields) based on values selected within the same form.
- **ESM Ownership**:
  - Organization Administrators can take ownership of a Service Provider's form to make it a global standard.
  - **Irreversible**: Transferring ownership to the Org level cannot be undone, though data remains isolated in the Provider account.

## Custom Fields
- **Scopes**:
  - **Global**: Application-wide availability.
  - **Service Catalog**: Restricted to specific items.
- **Search & Filter**:
  - Restricted to Text, Text Area, and Dropdown types.
  - Attachments cannot be searched or filtered.
  - **Latency**: Indexing for new filterable/searchable fields occurs nightly.

## Dynamic Form Rules
- Used to conditionally display specific custom forms across different modules (Incidents, Changes, Assets) based on rule logic.
