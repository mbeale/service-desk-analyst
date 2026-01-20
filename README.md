# Knowledge Base Workflow

This repository uses a CLI tool (`cli/know`) to manage the knowledge lifecycle, from capturing raw notes to structuring them into domain files.

## LLM Selection

By default, the CLI uses **Gemini**. To use **Claude** (with web search enabled), add the `--claude` flag before any command:

```bash
./cli/know --claude question "What is the current ITSM market size?"
./cli/know --claude capture "https://competitor.com/pricing"
./cli/know --claude challenge "We should raise prices by 20%"
```

**When to use Claude:**
- Questions requiring current web data (market sizes, competitor updates)
- Capturing content from URLs that need deeper analysis
- Any task where web search would improve accuracy

**Note:** Claude commands take longer due to web search. For quick local-only queries, use the default Gemini.

## 1. Capture
**Goal:** Quickly record raw information or extract facts from external sources.

**Short Note:**
```bash
# IMPORTANT: Use single quotes ('') if your note contains dollar signs ($) 
# to prevent Bash from expanding them as variables.
./cli/know capture 'Met with Client X. ARR is $43.5M.'
```

**URL (Extract facts from a website):**
```bash
./cli/know capture "https://www.competitor-y.com/pricing"
```

**Batch URLs (Consolidate facts from multiple sites):**
Create a text file `urls.txt` with one URL per line:
```
https://site1.com/feature-a
https://site2.com/feature-b
```
Then run:
```bash
./cli/know capture urls.txt
```

**Auto-Merge (Capture, Classify, and Merge in one step):**
```bash
./cli/know capture --auto-merge "https://documentation.solarwinds.com/new-feature"
# or
./cli/know capture -a "Quick fact about feature X"
```

**Local File (Extract facts from a document):**
```bash
./cli/know capture "./meeting-notes/client-x-interview.txt"
```
*Note: PDF files are not supported directly. Please convert to text first.*

- **Action:** 
    - Scrapes/Reads content and uses the LLM to extract only relevant facts, assumptions, and inferences.
    - Appends the structured entry to `register.md`.
    - Displays the captured note in the terminal.

## 2. Classify
**Goal:** Process the inbox and decide where information belongs.

```bash
./cli/know classify
```
- **Action:** 
    1. Archives the current `register.md`.
    2. Analyzes notes against the **Domain Map** (`index.md` files).
    3. Generates a **Merge Proposal** in `outputs/merges/pending/`.
    4. Displays the proposal for review.

## 3. Merge
**Goal:** Apply the classification proposal to the knowledge base.

**Single File:**
```bash
./cli/know merge merge_20260118123045.md
```

**Merge All Pending:**
```bash
./cli/know merge --all
```

- **Action:**
    1. Extracts content from the proposal.
    2. Appends it to the target file (creating it if necessary).
    3. Automatically updates the parent `index.md` if a new file is created.
    4. Moves the proposal to `outputs/merges/processed/`.

## 4. Question

**Goal:** Retrieve high-confidence answers from the knowledge base.



**Ad-hoc Question:**

```bash

./cli/know question "What are our key advantages over Freshworks?"

```

- **Action:** Scans all domain and lesson files and answers to stdout.



**Structured & Saved Answer:**

```bash

./cli/know question --save "What is the TAM for ITSM?"

```

- **Action:** 

    - Generates a detailed report with Confidence Score, Missing Information analysis, and Sources.

    - Saves the result to `outputs/answers/A-YYYYMMDD-HHMMSS.md`.



**Refresh Answer:**

```bash

./cli/know refresh outputs/answers/A-20260119-120000.md

```

- **Action:** 

    - Re-runs the original question against the latest knowledge base (including new lessons).

    - Shows a `diff` between the old and new answer.

    - Prompts to overwrite the file.



## 5. Learn



**Goal:** Incorporate corrections, decisions, or insights into future answers.







```bash



./cli/know learn "Correction: Feature X is not available on the Mobile app, despite what the marketing brief says."



```



- **Action:** 



    - Formats the input into a structured Lesson Record.



    - Saves to `lessons/answers/L-YYYYMMDD-HHMMSS.md`.



    - **Impact:** Future `question` and `refresh` calls will include this lesson as high-priority context.







## 6. Garden



**Goal:** Maintain the health and hygiene of the knowledge base.







```bash



./cli/know garden



```



- **Action:** Audits the `domains/` and `lessons/` directories for:



    - **Stale Files:** Content not updated in >60 days.



    - **Empty Files:** Placeholders with no content.



    - **Orphaned Files:** Leaf files that are not linked in their parent `index.md`.







## 7. Challenge (Devil's Advocate)



**Goal:** Stress-test a new idea or proposal against the established knowledge base.







```bash



./cli/know challenge "We should switch our pricing model to Per-Asset."



```



- **Action:** 



    - Acts as a "Hostile Critic."



    - Cross-references the proposal against Competitors, Market Trends, and Lessons.



    - Outputs a list of **Critical Flaws**, **Weak Assumptions**, and **Missing Defenses**.



## 8. Debate (Adversarial Collaboration)

**Goal:** Get a higher-quality answer through multi-model critique and synthesis.

The debate command runs a 3-round adversarial collaboration between Gemini and Claude:

**Default (Gemini first):**
```bash
./cli/know debate "What pricing model should we use for the MSP segment?"
```
- Round 1: Gemini answers the question
- Round 2: Claude critiques (5 issues: assumptions, missing info, reasoning) and rewrites
- Round 3: Gemini critiques Claude's rewrite and produces final answer

**With --claude (Claude first):**
```bash
./cli/know --claude debate "What pricing model should we use for the MSP segment?"
```
- Round 1: Claude answers (with web search)
- Round 2: Gemini critiques and rewrites
- Round 3: Claude critiques Gemini's rewrite and produces final answer

**Save output to file:**
```bash
./cli/know debate "Your question here" > debate_output.md
```

- **Action:**
    - Each model critiques the previous answer for unstated assumptions, missing information, and logical gaps.
    - The final answer incorporates multiple rounds of refinement.
    - All 3 rounds are printed to stdout for transparency.


## Directory Structure



- `cli/`: Scripts and prompts.

- `domains/`: The structured knowledge base (Business, Competitors, etc.).

- `lessons/`: Corrections and strategic decisions that override older context.

- `register.md`: The inbox for new, unprocessed notes.

- `outputs/`:

    - `answers/`: Saved structured answers.

    - `merges/`: Tracks pending and processed changes.

    - `register_archive/`: History of raw notes.
