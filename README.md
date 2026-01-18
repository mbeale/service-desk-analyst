# Knowledge Base Workflow

This repository uses a CLI tool (`cli/know`) to manage the knowledge lifecycle, from capturing raw notes to structuring them into domain files.

## 1. Capture
**Goal:** Quickly record raw information or extract facts from external sources.

**Short Note:**
```bash
./cli/know capture "Met with Client X. They mentioned competitor Y is offering feature Z at half our price."
```

**URL (Extract facts from a website):**
```bash
./cli/know capture "https://www.competitor-y.com/pricing"
```

**Local File (Extract facts from a document):**
```bash
./cli/know capture "./meeting-notes/client-x-interview.txt"
```

- **Action:** 
    - For short notes: Formats the note into a structured entry.
    - For URLs/Files: Scrapes/Reads the content and uses the LLM to extract only relevant facts, assumptions, and inferences.
- **Output:** Appends to `register.md`.

## 2. Classify
**Goal:** Process the inbox and decide where information belongs.

```bash
./cli/know classify
```
- **Action:** 
    1. Archives the current `register.md` to `outputs/register_archive/`.
    2. Analyzes the notes using the LLM.
    3. Generates a **Merge Proposal** in `outputs/merges/pending/`.
    4. Resets `register.md` for new notes.

## 3. Merge
**Goal:** Apply the classification proposal to the knowledge base.

**Review First:**
Check the generated file in `outputs/merges/pending/` to ensure the content and target file are correct.

**Apply:**
```bash
./cli/know merge merge_20260118123045.md
```
- **Action:**
    1. Extracts the "Proposed Insert" content.
    2. Appends it to the "Target File" (e.g., `domains/competitors/index.md`).
    3. Moves the proposal file to `outputs/merges/processed/`.

*Alternative (Manual):*
If you prefer to copy-paste manually, you can use `./cli/know approve <filename>` to just mark the file as processed after you are done.

## 4. Question
**Goal:** Retrieve answers from the knowledge base.

```bash
./cli/know question "What are our key advantages over Competitor Y?"
```
- **Action:** Scans all files in `domains/` and uses the LLM to answer your question based strictly on the documented facts.

## Directory Structure
- `cli/`: Scripts and prompts.
- `domains/`: The structured knowledge base (Business, Competitors, etc.).
- `register.md`: The inbox for new, unprocessed notes.
- `outputs/`:
    - `merges/`: Tracks pending and processed changes.
    - `register_archive/`: History of raw notes.
