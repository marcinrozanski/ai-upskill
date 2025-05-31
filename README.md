# ⛵ AI Infrastructure Upskill Journey  
*A hands-on path to upskill in private AI*

---

## About this repository

It is designed to work on a Windows 11 PC with Docker installed.
For now I'm using a 2018 Dell Inspirion 5370 laptop with 32GB RAM, i5 CPU , 1TB SSD, but without a GPU. However, it feels that a hardware upgrade is due!

This repo mirrors the five practical stages we mapped out together:

| Stage | Folder | What you build by the end |
|-------|--------|---------------------------|
| **1. Vector & RAG fundamentals** | `stage01_rag/` | A local Retrieval-Augmented-Generation playground (Qdrant + FastAPI + CPU-only Llama/Φ-3) |
| **2. LLMOps tool-chain** | `stage02_llmops/` | Phoenix tracing, Weights & Biases artefact store, guard-railed prompts, canary release workflows |
| **3. GPU-aware Kubernetes & FinOps** | `stage03_gpu_finops/` | K8s GPU quotas, Flash-Attention benchmarks, live $/token dashboards |
| **4. Secure-by-Design AI patterns** | `stage04_security/` | Vault-backed secrets, IaC policy gates, red-team prompt scripts, ISO 27001 sample controls |
| **5. Hybrid / on-device AI** | `stage05_edge/` | Multi-GPU or Apple-Silicon edge cluster running portable GGUF workloads |

Each stage is self-contained: you can clone only that folder and run it, or progress sequentially to layer skills.

---

## Quick start (Stage 1)

```bash
git clone https://github.com/marcinrozanski/ai-upskill.git
cd ai-upskill/stage01_rag/week1
```

Full per stage instructions live in each sub directory’s README.

## Licence

MIT for all code in this repo. Embedded models and third-party assets keep their original licences, check each model card or tool.

## WARNING
* Code in this repo comes with no warranty.
* Use it at your own risk.
* Do not use this code in production.
* Most of the code in this repo is AI generated.