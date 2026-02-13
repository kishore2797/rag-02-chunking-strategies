# ✂️ RAG Tutorial 02 — Chunking Strategies

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-2_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: [01 — Document Loading](https://github.com/kishore2797/rag-01-document-loading) | Next: [03 — Embedding Models](https://github.com/kishore2797/rag-03-embedding-models)

---

## 🌍 Real-World Scenario

> Your company's support docs total 10,000 pages. Users ask questions like "How do I reset my password?" The answer is in a 3-sentence paragraph buried in a 40-page admin guide. **If your chunks are too big** (whole pages), the LLM gets too much noise. **If too small** (individual sentences), it loses context like "the admin guide requires 2FA." Choosing the right chunking strategy is the difference between a useful answer and a hallucinated one.

---

## 🏗️ What You'll Build

An interactive explorer that lets you compare **4 chunking strategies** side-by-side on any text. Visualize chunk boundaries, measure quality metrics, and run retrieval simulations to see how chunking impacts search results.

```
Input text ──→ 4 Strategies in parallel
                ├── Fixed-size (500 chars)
                ├── Recursive character
                ├── Semantic (sentence)
                └── Semantic (paragraph)
              ──→ Compare: size distribution, completeness, retrieval quality
```

## 🔑 Key Concepts

- **Fixed-size chunking**: split every N characters/tokens — simple but breaks mid-sentence
- **Recursive splitting**: split by paragraphs → sentences → characters (LangChain-style)
- **Semantic chunking**: respect sentence/paragraph boundaries for coherent chunks
- **Overlap**: duplicate text at boundaries prevents information loss
- **Quality metrics**: sentence completeness, paragraph preservation, size variance

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · LangChain text splitters · NLTK |
| Frontend | React 19 · Vite · Tailwind CSS · Recharts |

## 📁 Project Structure

```
rag-02-chunking-strategies/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── chunkers/
│   │   │   ├── fixed_size.py
│   │   │   ├── recursive.py
│   │   │   └── semantic.py
│   │   ├── metrics/           # Quality scoring
│   │   └── api/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   │       ├── ChunkVisualizer.jsx
│   │       ├── MetricsPanel.jsx
│   │       └── ComparisonView.jsx
│   └── package.json
└── README.md
```

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — paste text, select strategies, and compare results.

## 📦 Example

A minimal runnable example is in the `example/` folder:

```bash
cd example
python example.py
```

It demonstrates fixed-size and recursive (paragraph/sentence) chunking on sample text.

## 📖 What You'll Learn

1. How chunk size affects retrieval precision and recall
2. Why overlap matters at chunk boundaries
3. Which strategy works best for which document type
4. How to measure chunk quality objectively
5. The chunk size vs. LLM context trade-off

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- Concepts from [Tutorial 01](https://github.com/kishore2797/rag-01-document-loading) (document loading)

## ✏️ Exercises

1. **Your own document**: Paste a real document (work email, blog post, research paper) and compare all 4 strategies — which produces the most coherent chunks?
2. **Tune overlap**: Set overlap to 0, 50, 100, 200 on the same text. At what point does overlap stop improving retrieval?
3. **Token-based chunking**: Modify the fixed-size chunker to count **tokens** (using `tiktoken`) instead of characters. Does it change results?
4. **Custom separator**: Add a chunker that splits on Markdown headings (`## `) for structured docs
5. **Benchmark**: Use 10 queries against the same document with each strategy. Which strategy returns the best chunk most often?

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Chunks cut mid-sentence | Using fixed-size without overlap | Add 10–20% overlap, or switch to recursive/semantic |
| Chunks are all wildly different sizes | Semantic chunking on poorly formatted text | Add a min/max chunk size constraint as a post-processing step |
| "Empty" chunks with only whitespace | Double newlines or formatting artifacts in source | Add a filter: discard chunks with < N meaningful characters |
| Retrieval works great on docs, fails on code | Code has different structure than prose | Use language-aware splitters (e.g., split on function boundaries) |

## 📚 Further Reading

- [Five Levels of Chunking Strategies](https://github.com/FullStackRetrieval-com/RetrievalTutorials) — Greg Kamradt's visual guide
- [LangChain Text Splitters](https://python.langchain.com/docs/how_to/#text-splitters) — All built-in splitter types
- [Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/) — Pinecone's practical guide
- [Evaluating Chunking Methods](https://research.trychroma.com/evaluating-chunking) — Chroma's research on chunk quality

## ➡️ Next Steps

Now that you can split text into quality chunks, head to **[Tutorial 03 — Embedding Models](https://github.com/kishore2797/rag-03-embedding-models)** to learn how to convert those chunks into searchable vectors.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>
