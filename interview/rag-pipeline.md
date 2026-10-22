# RAG Pipeline: HCLTech Bullet Defense

## Walkthrough (~80 sec)
It was an internal code-search assistant for developers: ask a question, get an answer pointing to the exact files.

**Offline (indexing):** Indexed the team's code files and docs (CONFIRM COUNT: said 1,100+ aloud, resume says 100K+; use the true one everywhere). Chunked code by function/class using AST parsing (e.g. tree-sitter) so each chunk is a complete unit. Tagged chunks with metadata: repo, file path, language, date. Embedded and stored in a vector index (FAISS for prototyping and offline evals; production store: confirm). Daily refresh from new commits.

**Online (query):** Embed the question (bi-encoder) -> retrieve top ~20-50 -> rerank with a cross-encoder -> top 5 into the prompt -> LLM answers with citations to files.

**Design choice:** Added a reranker. Vector search is fast but rough; the cross-encoder reads question + chunk together and orders results far more accurately. With prompt tuning, improved recall@5 on a fixed test set by ~25%.

## Probe: Why rerank instead of retrieving top 5 directly?
A bi-encoder embeds question and chunk separately: fast but rough, so the right chunk is often in the top 50 but not the top 5. A cross-encoder reads them together: much more accurate, but slow and costly (one model run per pair), so it can't scan every chunk. Two stages: cheap retrieval for top ~50, then the reranker picks the best 5. Small latency cost, much better relevance.

## Probe: Why chunk by function, not fixed token size?
Fixed size cuts mid-function, so neither half makes sense alone and the LLM explains incomplete code. Function/class chunks keep the full logic and line up with metadata (function name, file path). Trade-off: very long functions still need splitting; tiny ones may need surrounding class context added.

## Open: confirm file count, vector store, embedding model, top-k, metric.
