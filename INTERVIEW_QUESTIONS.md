# Interview Questions + My Best Answers

## Tell me about yourself (7/10, Oct 15) — 60–90s
So, I'm an AI/ML engineer with about five years of experience. Right now I'm working with Perplexity on their research and retrieval systems: a pipeline that breaks complex questions into smaller searches and combines the results into one cited answer. Most of my focus there has been retrieval quality and evaluation: finding the right sources and measuring whether answers are grounded. Before that, I spent about a year and a half at HCLTech on a RAG-based developer assistant that helped engineers search and understand code across dozens of repositories. Going back a bit, I started at Accenture, first as an intern and then as an ML engineer, mainly on NLP models and semantic search for an enterprise knowledge platform. Alongside that, I'm finishing my CS degree at UIC, graduating May 2027. What I really enjoy is turning messy information into answers people can trust, and honestly that's a big reason this role caught my attention.

## How did you measure groundedness? (8/10, Oct 15)
Grounded means every claim in the answer is supported by the retrieved sources. We measured it on a fixed evaluation set of real questions using RAGAS and DeepEval, mainly the faithfulness score: it splits an answer into claims and checks each against the sources (8 of 10 supported = 0.8). We also checked citation accuracy. Since automatic judges can be wrong, people reviewed samples side by side. Nothing shipped unless it beat the baseline offline and held up in an A/B test. That loop improved grounded-answer quality by about 14%.
Prepare next: "14% from what to what? Relative or absolute?"

## Contains Duplicate complexity
O(n) time (each element once, set lookup O(1) average via hashing), O(n) space. Brute force = nested loops, O(n^2) time, O(1) space. Trade memory for speed; return early on first duplicate.
