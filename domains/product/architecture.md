# Product Architecture

## Metadata
- **Last Updated:** 2026-01-18
- **Sources:** Internal Engineering Docs
- **Confidence:** 100

## Overview
SolarWinds Service Desk is a multi-tenant SaaS application designed for IT Service Management (ITSM).

## Tech Stack
- **Frontend:** [Placeholder: React/Angular/Vue]
- **Backend:** [Placeholder: Ruby on Rails/Node.js/Python]
- **Database:** [Placeholder: PostgreSQL/MySQL]
- **Infrastructure:** [Placeholder: AWS/Azure]

## Key Components
1. **API Gateway:** Handles incoming requests and routing.
2. **Worker Queues:** Asynchronous job processing (emails, reports).
3. **Search Engine:** Indexing for tickets and assets (e.g., Elasticsearch).

## Facts
- The system supports SAML 2.0 for SSO.
- Data is encrypted at rest and in transit.

## Assumptions
- We assume the current database sharding strategy will support growth for the next 12 months.
