# Plan: Pseudo-RAG for Questioning

## Goal
Implement a two-stage retrieval process to limit the context sent to the LLM during questioning, improving performance and accuracy.

## Workflow

### 1. Retrieval Phase (Semantic Vector Search)
- **Action**: Use a local Python script to perform semantic search across the knowledge base.
- **Mechanism**: Use `sentence-transformers` (specifically the `all-MiniLM-L6-v2` model) to generate dense vector embeddings for all markdown files.
- **Benefit**: Matches query intent rather than just keywords (e.g., "pricing" matches "cost").

### 2. Context Assembly
...

## Implementation (Python Search Script)

This script `cli/search.py` performs semantic retrieval using local embeddings.

```python
#!/usr/bin/env python3
import sys
import os
try:
    from sklearn.neighbors import NearestNeighbors
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Error: Required libraries not installed.")
    print("Run: pip install sentence-transformers scikit-learn")
    sys.exit(1)

SEARCH_DIRS = ["domains", "lessons"]

def load_documents():
    file_paths, contents = [], []
    for d in SEARCH_DIRS:
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read()
                        if text.strip():
                            file_paths.append(path)
                            contents.append(text)
    return file_paths, contents

def main():
    query = " ".join(sys.argv[1:])
    files, documents = load_documents()
    if not documents: sys.exit(0)

    # Load local AI model (downloads once to ~/.cache/torch)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate Semantic Embeddings
    doc_vectors = model.encode(documents)
    query_vector = model.encode([query])

    k = min(3, len(files))
    knn = NearestNeighbors(n_neighbors=k, metric='cosine')
    knn.fit(doc_vectors)

    distances, indices = knn.kneighbors(query_vector)

    for i, idx in enumerate(indices[0]):
        if distances[0][i] < 0.6: # Semantic similarity threshold
            print(files[idx])

if __name__ == "__main__":
    main()
```

## Benefits
...
