# IT7075: Applied AI for Cybersecurity

Course code, lecture notebooks, and project starters. This repository is meant to be
run on a GPU host (a Jetstream2 A100 instance) to produce notebook outputs, then
pushed back with those outputs saved.

## Modules, in course order

1. `01_Introduction_to_AI`
2. `02_Tools_and_Environment`
3. `03_LLMs_Local_and_Cloud`
4. `04_RAG`
5. `05_LangChain`
6. `06_LangGraph`
7. `07_MCP`
8. `08_Cybersecurity_Orchestration`

The folders are numbered so they sort in course order. Each module also has a `slides/`
folder with the lecture deck as `.pptx` and `.pdf`.

Each module holds its lecture code under `code/` (or, for
`Cybersecurity_Orchestration`, at the module root), a `requirements.txt` where one
is needed, and the project starter and data under `assignments/project/`.

## What runs to produce results, and what does not

**Complete, run these to generate outputs:**

- every lecture notebook under `*/code/` (for example `04_RAG/code/rag_pipeline.ipynb`,
  `05_LangChain/code/langchain_basics.ipynb`, `07_MCP/code/mcp_build_server.ipynb`);
- `08_Cybersecurity_Orchestration/part2_orchestration_simulated.ipynb` and
  `part3_web_pentest_real.ipynb`.

**Templates, do not expect these to run top to bottom:** the four
`*_Starter.ipynb` files under `assignments/project/` are student assignments with
blanks (`____`) and `TODO` markers, and will raise `NameError` until a student fills
them in. Leave them as templates; they are here so students can clone and work on
them.

## Running on the VM

```bash
# one environment for everything (fastest to try first)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# if module versions conflict in a single environment, install per module instead:
#   pip install -r 04_RAG/requirements.txt        # etc.
```

Most lecture notebooks run offline on a small local embedding model and need no API
key. Where a step calls a hosted model, put the key in a `.env` file at the module
root (never commit it; `.gitignore` already excludes `.env`). Run each notebook top
to bottom and save it with its outputs before committing.

## Notes

- No instructor material is in this repository: no solution notebooks, grading
  guides, slide sources, or generators.
- `sample.env` files are templates only and contain no real keys.
EOF
