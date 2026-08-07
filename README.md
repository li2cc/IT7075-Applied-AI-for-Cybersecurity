# IT7075: Applied AI for Cybersecurity

Course code, lecture notebooks, and project starters. This repository is meant to be
run on a GPU host (a Jetstream2 A100 instance) to produce notebook outputs, then
pushed back with those outputs saved.

## Modules, in course order

1. `Introduction_to_AI`
2. `Tools_and_Environment`
3. `LLMs_Local_and_Cloud`
4. `RAG`
5. `LangChain`
6. `LangGraph`
7. `MCP`
8. `Cybersecurity_Orchestration`

Each module holds its lecture code under `code/` (or, for
`Cybersecurity_Orchestration`, at the module root), a `requirements.txt` where one
is needed, and the project starter and data under `assignments/project/`.

## What runs to produce results, and what does not

**Complete, run these to generate outputs:**

- every lecture notebook under `*/code/` (for example `RAG/code/rag_pipeline.ipynb`,
  `LangChain/code/langchain_basics.ipynb`, `MCP/code/mcp_build_server.ipynb`);
- `Cybersecurity_Orchestration/part2_orchestration_simulated.ipynb` and
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
#   pip install -r RAG/requirements.txt        # etc.
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
