
# Runbooks

## Overview
Runbooks are structured, automated workflows designed to guide agents through complex incident resolution.
- **Availability**: Exclusive to Premier plan customers.
- **Execution**: Runbooks must be manually started and stopped by an agent; they do not trigger automatically.
  - Stopping a runbook resets the workflow to the beginning.
  - Only one runbook can be attached to an incident at a time.

## GenAI Generation
Runbooks can be generated via GenAI using three methods:
1. File upload (Word/PDF).
2. Free text prompts.
3. Existing solution articles.

> **Warning**: Deleting the source file used to generate a runbook will also delete the runbook record itself.

## Configuration
- **Permissions**: Creation is restricted to Administrators (`Setup > Service Desk`).
- **Logic**: Custom fields can be marked as mandatory within a runbook step and used to drive conditional branching.
- **ESM**: Service Providers can maintain their own specific runbook libraries.
