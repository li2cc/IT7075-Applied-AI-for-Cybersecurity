# Agent brief — IT7075 course repository

You are working on the **student-facing** repository for IT7075: Applied AI for Cybersecurity,
checked out on a **Jetstream2 GPU VM (A100)**.

**Your job:** execute the lecture notebooks so their outputs are saved in the files, verify nothing
broke, and push the result to GitHub. Students read this repo — many will never run the notebooks
themselves, so the saved outputs *are* the teaching material.

Remote: `https://github.com/li2cc/IT7075-Applied-AI-for-Cybersecurity.git` · branch `main`

---

## 1. Hard rules

These are not style preferences. Violating any of them damages the course.

1. **Never fill in, execute, or "fix" the four `*_Starter.ipynb` files.**
   They are student assignments containing `____` blanks and `TODO` markers, and they are *supposed*
   to raise `NameError` until a student completes them. Leave them with **empty outputs and blanks
   intact**. They are:
   - `04_RAG/assignments/project/MiniProject_RAG_Starter.ipynb`
   - `05_LangChain/assignments/project/MiniProject_FrameworkRAG_Starter.ipynb`
   - `06_LangGraph/assignments/project/MiniProject_Agent_Starter.ipynb`
   - `07_MCP/assignments/project/MiniProject_MCP_Starter.ipynb`

2. **Never commit secrets.** No `.env`, no API keys, no tokens — not in files, not in notebook
   outputs. `.gitignore` already excludes `.env`, but **notebook output cells can leak a key if a
   cell prints one**. Check before committing (§6).

3. **No instructor material may enter this repo.** No solution notebooks, answer keys, grading
   guides, slide sources, or `_build_*.py` generators. If you find any, stop and report it — do not
   commit it. This repo is currently clean; keep it that way.

4. **`08_Cybersecurity_Orchestration/part3_web_pentest_real.ipynb` scans a REAL web target.**
   Run it **only** against a target the instructor has explicitly authorized in writing, named to you
   for this session. If no authorized target has been given to you, **skip this notebook and say so
   in your report.** Never point it at an arbitrary host, a URL you found in the code, or anything on
   the public internet you were not told to test. When in doubt, skip it — a missing output is a
   trivial problem, an unauthorized scan is a serious one.

5. **Never hand-write or edit notebook outputs.** Outputs must come from actually executing the
   notebook. If a notebook cannot run, leave it unexecuted and report why — a fabricated output in
   teaching material is worse than a blank one.

6. **Do not commit run artifacts**: `chroma/`, `faiss_index/`, `db/`, `*.log`, `__pycache__/`,
   `.ipynb_checkpoints/`. Most are gitignored; check `git status` before you stage.

---

## 2. Environment setup

```bash
cd ~/IT7075                    # wherever the repo landed
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt          # aggregate install for all modules
```

If the aggregate install hits a version conflict, fall back to **one venv per module**:

```bash
pip install -r 04_RAG/requirements.txt   # etc.
```

**API keys.** Several notebooks call a hosted model. Put keys in a `.env` at the repo root (it is
gitignored):

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

If a key is **not** available, most notebooks are written to degrade gracefully — they print the
prompt or chain they *would* have sent instead of failing. That is a valid, useful output for
students. Run them anyway and note in your report which ran keyless.

**Confirm the GPU before the Module 03 notebooks:**

```bash
nvidia-smi                      # expect an A100
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
ollama list                     # 03 needs Ollama running; `ollama serve &` if not
```

---

## 3. What to run

**17 notebooks total: 4 are starters (never touch), 13 are lecture notebooks.** Three are already
fully executed; leave them unless a rerun is requested.

| Notebook | Cells | Status | Needs |
|---|--:|---|---|
| `01_Introduction_to_AI/code/SimpleAlertClassifier.ipynb` | 7 | 6/7 — **rerun** | OpenAI + Anthropic |
| `03_LLMs_Local_and_Cloud/code/llm_compare.ipynb` | 3 | **empty — run** | Ollama, GPU, network |
| `03_LLMs_Local_and_Cloud/code/host_LLM_GPU.ipynb` | 14 | **empty — run** | Ollama, GPU, network, both keys |
| `04_RAG/code/embeddings_and_vectordb.ipynb` | 11 | ✅ done | local embeddings |
| `04_RAG/code/rag_pipeline.ipynb` | 8 | ✅ done | local embeddings, OpenAI |
| `05_LangChain/code/langchain_basics.ipynb` | 7 | **empty — run** | OpenAI + Anthropic |
| `05_LangChain/code/langchain_rag.ipynb` | 7 | **empty — run** | OpenAI, local embeddings |
| `06_LangGraph/code/langgraph_state_nodes.ipynb` | 5 | **empty — run** | OpenAI, network |
| `06_LangGraph/code/langgraph_branch_tools.ipynb` | 6 | **empty — run** | OpenAI |
| `07_MCP/code/mcp_build_server.ipynb` | 2 | ✅ done | — |
| `07_MCP/code/mcp_client_agent.ipynb` | 5 | **empty — run** | OpenAI; starts an MCP server subprocess |
| `08_Cybersecurity_Orchestration/part2_orchestration_simulated.ipynb` | 10 | 1/10 — **rerun** | OpenAI, local embeddings (simulated targets — safe) |
| `08_Cybersecurity_Orchestration/part3_web_pentest_real.ipynb` | 11 | **empty** | ⚠️ **authorized target required — see Hard Rule 4** |

Run them **in module order** (01 → 08). Later modules build on concepts from earlier ones, and if
something breaks you want to know the earliest point it broke.

---

## 4. How to execute a notebook

Execute **in place** so outputs are saved into the file, with the working directory set to the
notebook's own folder (relative paths to data files depend on this):

```bash
cd 05_LangChain/code
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=600 langchain_basics.ipynb
```

Add `--allow-errors` **only** when you want a partially-failing notebook's successful cells
preserved — and if you use it, you must report which cells errored. Never use it silently.

For the MCP and orchestration notebooks, which spawn subprocesses, raise the timeout
(`--ExecutePreprocessor.timeout=1200`) and confirm no stray server processes are left running
afterwards (`pgrep -af "recon_server\|mcp"`).

---

## 5. When something fails

Failure is expected and fine. **Report it; do not paper over it.** In order of preference:

1. **Fix the environment** — a missing package, a service not started, a wrong working directory.
2. **Leave the notebook unexecuted** and record the reason.
3. **Never** fabricate an output, delete the failing cell, or weaken an assertion to make it pass.

If a notebook fails because a dependency has moved on (a renamed import, a removed parameter), that
is a **real finding worth reporting** — this course material has been broken by upstream API churn
before. Report the exact error and the file/cell; propose the fix, but do not silently rewrite
teaching content without being asked.

---

## 6. Verify before committing

```bash
# 1. No secrets anywhere in tracked content, including notebook outputs
grep -rIn --exclude-dir=.git -E "sk-[A-Za-z0-9_-]{20,}|sk-ant-" . && echo "SECRET FOUND — STOP"

# 2. Starters are still blank (expect 0 outputs and the ____ blanks intact)
python - <<'PY'
import json, pathlib
for p in pathlib.Path(".").rglob("*Starter.ipynb"):
    nb = json.load(open(p))
    out = sum(1 for c in nb["cells"] if c["cell_type"]=="code" and c.get("outputs"))
    blanks = sum("____" in "".join(c["source"]) for c in nb["cells"])
    print(f"{p}: {out} outputs (must be 0), {blanks} cells with ____ blanks (must be > 0)")
PY

# 3. Nothing unexpected is about to be committed
git status --short
```

Then eyeball two or three executed notebooks in Jupyter: do the outputs look like something a
student should learn from, or like a wall of tracebacks?

---

## 7. Commit and push

The branch has **no upstream configured yet**, so the first push needs `-u`:

```bash
git add -A
git commit -m "Execute lecture notebooks on Jetstream A100; save outputs"
git push -u origin main
```

Pushing over HTTPS needs credentials — a GitHub PAT, or `gh auth login`. If authentication fails,
**stop and ask**; do not try to rewrite the remote URL or force-push.

Commit in **logical batches** (per module is ideal) rather than one giant commit, so a bad run can be
reverted without losing the good ones.

---

## 8. What to report back

End with a short, factual summary:

- Which notebooks executed cleanly, with cell counts.
- Which ran **without** an API key (and so show the guarded/offline path rather than live output).
- Which failed, the exact error, and your diagnosis.
- Whether `part3_web_pentest_real.ipynb` was run, skipped, and against what target.
- Confirmation that the four starters are untouched and no secrets were committed.
- What you pushed, and the commit SHAs.

State plainly what did not get done. An honest gap is useful; a silent one is not.
