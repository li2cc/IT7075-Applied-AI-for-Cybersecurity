# IT7075C: Applied Artificial Intelligence for Cybersecurity

Graduate course, School of Information Technology, University of Cincinnati.
Instructor: **Chengcheng Li**. Format: **online, asynchronous** (Canvas). 3 credit hours.

Full policies, dates, and contact details are in the syllabus:
**[IT7075C_Syllabus_Fall2026.pdf](IT7075C_Syllabus_Fall2026.pdf)**.

## Course description

This course explores how artificial intelligence enhances modern **defensive** cybersecurity
practice. Students apply AI-driven tools to identify vulnerabilities, detect attacks, model
threats, and automate security operations, with emphasis on machine learning, deep learning, and
Explainable AI for monitoring, incident response, and digital forensics. It is hands-on and
project-driven: each week pairs a short concept lecture with runnable notebooks, so you read, run,
and modify real code every week. By the end you can design, evaluate, and implement AI-enabled
cybersecurity solutions.

**Textbook (required):** Omar Santos, *Agentic AI for Cybersecurity: Building Autonomous Defenders
and Adversaries* (Addison-Wesley, 2026), ISBN 978-0-13-558986-1. It anchors the RAG, LangChain,
LangGraph, MCP, and Cybersecurity Orchestration modules.

## Learning outcomes

By the end of the course you will be able to:

- conduct security assessments using AI-enhanced tools and methodologies;
- perform threat modeling and map attack surfaces with AI-assisted techniques;
- develop AI and machine-learning models to identify cyber risks and support mitigation;
- evaluate vulnerabilities and design AI-driven mitigation strategies;
- implement AI techniques to automate and improve security operations;
- produce clear reports with analysis and actionable recommendations;
- apply frameworks for AI-based threat intelligence;
- explain and apply principles of Explainable AI in cybersecurity.

## Modules, in course order

The folders are numbered so they sort in teaching order. Each module holds its lecture code under
`code/` (or, for module 8, at the module root), a `requirements.txt` where one is needed, the
lecture deck under `slides/` as `.pptx` and `.pdf`, and the project starter and data under
`assignments/project/`.

| # | Module | Folder | Weeks | Deliverable |
|--:|---|---|:--:|---|
| 1 | Introduction to AI & the AI-for-Cyber landscape | `01_Introduction_to_AI` | 1 | Lab — AI landscape |
| 2 | Tools & Environment | `02_Tools_and_Environment` | 1 | MP1 — Environment setup |
| 3 | LLMs on Local & Cloud | `03_LLMs_Local_and_Cloud` | 1 | MP2 — Running LLMs in different environments |
| 4 | Retrieval-Augmented Generation (RAG) | `04_RAG` | 2 | MP3 — Build & tune a RAG analyst |
| 5 | LangChain | `05_LangChain` | 2 | MP4 — Rebuild your RAG with LangChain |
| 6 | LangGraph | `06_LangGraph` | 2 | MP5 — Alert-triage agent |
| 7 | Model Context Protocol (MCP) | `07_MCP` | 2 | MP6 — Build & audit an MCP server |
| 8 | Cybersecurity Orchestration | `08_Cybersecurity_Orchestration` | 4 | Final project (pairs) |

## Grading

| Component | Points | Weight |
|---|--:|--:|
| Mini-projects MP1–MP6 (100 each) | 600 | 60% |
| Final project — AI Security Analyst (pairs) | 200 | 20% |
| Discussion forums | 100 | 10% |
| Module 1 lab (AI landscape) | 50 | 5% |
| Participation & engagement | 50 | 5% |

The six mini-projects are individual; the final project is a two-person team. Scale: 93%+ A. See the
syllabus for the full scale and the late policy (10% per day, up to three days).

## Schedule (Fall 2026)

| Week | Date | Module / topic | Due |
|--:|---|---|---|
| 1 | Aug 24 | Introduction to AI & the landscape | Module 1 lab; accounts & API-key check |
| 2 | Aug 31 | Tools & Environment | MP1 |
| 3 | Sep 7 | LLMs on Local & Cloud | MP2 |
| 4 | Sep 14 | RAG, part 1: embeddings & vector DBs | Discussion 1 |
| 5 | Sep 21 | RAG, part 2: retrieve → augment → generate | MP3 |
| 6 | Sep 28 | LangChain, part 1: chains, prompts, LCEL | Discussion 2 |
| 7 | Oct 5 | LangChain, part 2: RAG with a framework | MP4 |
| 8 | Oct 12 | LangGraph, part 1: state, nodes, edges | Discussion 3 |
| 9 | Oct 19 | LangGraph, part 2: tool-using agents | MP5 |
| 10 | Oct 26 | MCP, part 1: the protocol & servers | Discussion 4 |
| 11 | Nov 2 | MCP, part 2: client/agent & attack surface | MP6 |
| 12 | Nov 9 | Orchestration, part 1: scoped tooling & recon | Final proposal & pair sign-up; Discussion 5 |
| 13 | Nov 16 | Orchestration, part 2: chain vs. retrieval vs. agent | Final checkpoint — lab & tools working |
| 14 | Nov 23 | Final project build (Thanksgiving 11/26–27) | Discussion 6 |
| 15 | Nov 30 | Final project build; demonstrations | Final report & video |
| Finals | Dec 7 | Demonstrations & reflections | All final deliverables |

## Running the code (on the GPU host)

This repository is meant to run on a GPU host (a Jetstream2 A100 instance): produce notebook
outputs, then push back with those outputs saved.

```bash
# one environment for everything (fastest to try first)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# if module versions conflict in a single environment, install per module instead:
#   pip install -r 04_RAG/requirements.txt        # etc.
```

Most lecture notebooks run offline on a small local embedding model and need no API key. Where a
step calls a hosted model, put the key in a `.env` file at the module root (never commit it;
`.gitignore` excludes `.env`). Run each notebook top to bottom and save it with its outputs before
committing.

**Complete, run these to generate outputs:** every lecture notebook under `*/code/` (for example
`04_RAG/code/rag_pipeline.ipynb`), and `08_Cybersecurity_Orchestration/part2_orchestration_simulated.ipynb`
and `part3_web_pentest_real.ipynb`.

**Templates, not meant to run top to bottom:** the four `*_Starter.ipynb` files under
`assignments/project/` are student assignments with blanks (`____`) and `TODO` markers, and raise
`NameError` until filled in.

## Ethics & scope

All offensive or dual-use activity is restricted to isolated lab VMs, instructor-approved or
explicitly authorized targets, student-created apps, and public datasets. Never scan, test, or
collect data from systems outside the approved scope. Keep API keys and secrets out of the
repository.

Generative-AI tools (ChatGPT, Claude, Copilot) are permitted and encouraged as coding and learning
aids, with disclosure; allowable use varies by assignment, and you are responsible for verifying
anything a model produces. See the syllabus for the full policy.

## Notes

- No instructor material is in this repository: no solution notebooks, grading guides, slide
  sources, or generators.
- `sample.env` files are templates only and contain no real keys.
