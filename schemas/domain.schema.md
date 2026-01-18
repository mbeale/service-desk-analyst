# Domain File Schema

## index.md
Purpose:
- Provide an overview of the domain
- Track open questions and unresolved topics
- Act as a navigation map to leaf files

Required Sections:
1. Scope
   - Define the boundaries of this domain
2. Active Topics
   - List subtopics, entities, or concepts
3. Open Questions
   - List questions that need to be answered

Rules:
- Must not contain unreferenced raw facts
- Should not duplicate information in leaf files
- Only summarize, map, or highlight gaps

---

## Leaf Files
Purpose:
- Store entity- or concept-specific facts and signals

Required Sections:
1. Last Updated
   - ISO date, e.g., 2026-01-18
2. Sources
   - Where the information came from (internal, external, report, interview)
3. Facts
   - Confirmed observations, signals, metrics
4. Assumptions
   - Unverified hypotheses or interpretations
5. Confidence
   - Numeric 0–100, representing certainty

Rules:
- Should be specific and granular
- Cross-reference index.md where applicable
- Avoid repetition across leaf files
