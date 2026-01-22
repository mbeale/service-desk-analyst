
```markdown
# ESM - Security Operations Requirements

## Market Analysis
Security departments (Physical and InfoSec) require distinct service management workflows that prioritize confidentiality and rapid response. The core value of Security ESM is the ability to segregate sensitive data from general IT visibility while leveraging a shared service management infrastructure.

## Key Requirements

### Request Types
Common service catalog items for Security include:
- **Physical Access**: New badge requests, modification of access levels, visitor registration.
- **Incident Reporting**: Lost badge reporting, theft reporting, suspicious activity logs.
- **Background Checks**: Initiation and status tracking for new hires or contractors.
- **Audit Evidence**: Collection requests for compliance audits (SOC2, ISO).

### Security & Confidentiality (Critical)
Security operations demand the highest level of data isolation:
- **Segregation of Duties**: IT administrators must not have inherent access to Security tickets or data.
- **Chain of Custody**: Immutable logging of all evidence handling and ticket interactions.
- **Invisibility**: Sensitive incident categories must be hidden from general service portal views.

### Workflows & Procedures
- **"Break-Glass" Protocols**: Emergency workflows that bypass standard approval chains during critical threats.
- **After-Hours Escalation**: Distinct routing paths for incidents occurring outside business hours (e.g., routing to GSOC or on-call security officer).
- **Incident Response**: Triage workflows that immediately categorize and assign based on threat severity.

### Essential Integrations
- **PACS (Physical Access Control Systems)**: Integration with systems like Lenel, AMAG, or HID for automated badge provisioning.
- **Video Surveillance**: Linkage to CCTV footage storage or timestamps.
- **HRIS**: Verification of employment status for access rights.
```
