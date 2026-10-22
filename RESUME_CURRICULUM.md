# Resume Defense Curriculum (from P_AIML_Engineer_2.docx)

Goal: be able to defend every line of the target resume in an interview.

## Lesson format (permanent rule, from Oct 22)
1. Teach from scratch (plain English, analogy, example, define every term)
2. Model answers for every interview question, shown BEFORE asking
3. Cumulative recap of ALL concepts covered so far
4. Mock interview (answer from memory)
5. Follow-up probes, then grade

Daily slot: one 30-45 min "Resume Lesson" block, alongside the normal Python/SQL/DSA work.

## Modules (ordered by how likely interviewers ask + what each one depends on)

| # | Module | Resume lines it defends | Weeks |
|---|---|---|---|
| R1 | LLM basics: tokens, context window, temperature, prompts, embeddings, cosine similarity | Summary, every LLM bullet | 2 |
| R2 | RAG core: chunking, metadata, vector DBs (FAISS vs Pinecone vs Azure AI Search), top-k, prompt building, citations | HCL RAG, Perplexity RAG, Accenture semantic search | 2-3 |
| R3 | Search quality: BM25, hybrid search, rank fusion, bi-encoder vs cross-encoder reranking, query expansion, metadata filtering; Recall@k, MRR, nDCG | Perplexity Recall@10 +15%, HCL relevance +25% | 3 |
| R4 | LLM evaluation: RAGAS, DeepEval, LangSmith, MLflow, A/B tests, human preference eval, guardrails, hallucination checks | Perplexity grounded +14%, HCL MLflow/guardrails | 4 |
| R5 | Agents and tools: function calling, structured outputs, tool orchestration, LangChain vs LangGraph vs LlamaIndex, multi-agent, MCP, GraphRAG / knowledge graphs | Perplexity bullets 1, 3, 4; HCL bullet 3 | 5-6 |
| R6 | Backend: FastAPI, Pydantic, REST vs gRPC, AsyncIO, auth, PostgreSQL, Redis, Kafka, Snowflake | Perplexity 6-7, HCL 4, Accenture 4 | 6-7 |
| R7 | Classic ML: train/test, logistic regression, random forest, XGBoost, feature engineering, tuning, ROC-AUC, precision, recall, F1 | Intern bullets, Accenture 2 | 7-9 |
| R8 | Latency and cost: caching, parallel retrieval, model routing, p95, token management | Perplexity p95 -25%, HCL 2-3 s latency | 9 |
| R9 | Cloud and deploy: Docker, Kubernetes (EKS/AKS), Helm, Terraform, CI/CD, AWS (EC2, S3, Lambda, SageMaker, CloudWatch), Azure (OpenAI, AI Search, ML, Monitor), Ray | Perplexity 8, HCL 5, Accenture 5-6 | 10-11 |
| R10 | Deep learning / NLP: neural nets, transformers, BERT, fine-tuning for classification / intent / NER / similarity, PyTorch vs TensorFlow | Accenture 1-2 | 11-13 |
| R11 | LLM fine-tuning: LoRA, QLoRA, PEFT | HCL 7 | 13 |
| R12 | Data pipelines: Airflow, PySpark, SQL ingestion | HCL 8 | 14 |

Hands-on proof: Projects 1-3 and the Capstone (RAG + agents + FastAPI + Docker + CI) are built to cover R2-R9 for real.

## Fix before the next application (concrete risks)
1. File count: in the RAG walkthrough you said "1,100+ files"; the resume says "100K+ source files" and "50+ repositories". Use the true number everywhere (resume, rag-pipeline.md, spoken answer).
2. "RLHF": RLHF means training a model with reinforcement learning on human preference data. Comparing prompts with human feedback is human preference evaluation. Rename it unless a model was actually trained that way.
3. Location: header says "CA" and Perplexity says "CA, USA". Use the true location (Chicago, IL; "Remote" if the role was remote). Mark Perplexity as (Contract).
4. Add: "U.S. Permanent Resident, no sponsorship required."
5. Prepare a one-line answer for the Oct 2022 - Jun 2023 gap.
6. Every tool in the skills section is a possible question. Until a module is done, that tool is a risk.
