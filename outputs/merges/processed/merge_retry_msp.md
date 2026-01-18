## Entry ID: R-2026-01-18-02

### Classification
Domains: Market, Business, Product
Target File: domains/market/msp_segment_analysis.md (New)

### Content Type
- Fact: yes
- Assumption: yes
- Inference: yes

### Confidence
95

### Proposed Insert
```markdown
# MSP Segment Analysis

## Market Characteristics
- **Sales Model:** Primarily B2B2B (reselling services) rather than internal IT operations [Assumption].
- **Sales Cycle:** Rapid 2-8 weeks driven by Product-Led Growth (PLG), significantly faster than the 6-18 month enterprise cycle.
- **Marketing Channels:** Decisions driven by peer communities (Reddit, Slack) and referrals rather than analyst reports (Gartner/Forrester).

## Architectural Requirements
- **Multi-Tenancy:** True multi-tenant architecture is non-negotiable for strict data isolation and per-tenant customization.
- **Integrations:**
  - Stack centers on RMM and PSA integrations.
  - ITSM layer must sync ticketing and billing data bidirectionally.
  - Legacy integration is a primary barrier for 31% of MSPs (often requires 15-25 custom connectors).
- **Provisioning:** Critical need for template-based tenant provisioning to reduce setup time from weeks to minutes.

## Pricing Preferences
- **Preferred Model:** Per-technician ($70-250/month).
- **Avoided Model:** Per-endpoint pricing.
  - *Reasoning:* Per-endpoint models punish growth and erode margins for asset-heavy clients [Inference].
```

### Conflicts Detected
- None
