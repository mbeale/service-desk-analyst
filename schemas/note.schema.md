# Note Classification Schema

## Register Entries
Each entry must be classified as one of:
- Fact: a verified observation or metric
- Assumption: an unverified belief or hypothesis
- Inference: a conclusion drawn from facts or assumptions

Metadata:
- Date of capture
- Source (if known)
- Optional context tags (domain, topic)

Rules:
- Each entry must be short and self-contained
- Do not edit or summarize raw entries in the register
- Each bullet/entry is treated as a unit for classification

---

## Merged Notes
When a register entry is merged into a domain file, it must include:

Required Fields:
1. Date
   - When the fact was observed or captured
2. Source
   - Internal, external, report, interview, etc.
3. Confidence (0–100)
   - AI-provided or human-adjusted
4. Assumptions / Inferences
   - Explicitly list anything inferred

Rules:
- Preserve original register content
- Add context to clarify meaning and source
- Cross-reference leaf file location in index.md if applicable
- Avoid ambiguous statements
