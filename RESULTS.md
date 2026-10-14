# CHALLENGE 2: Benchmark Cursor’s Models

**Event:** [Global Hack Week: Hacktoberfest](https://www.mlh.com/events/global-hack-week-open-source-90)  
**Challenge:** [Benchmark Cursor’s Models](https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11d25-134c-17e5-e22c-8af278534580/submissions/new)  
**Fixed prompt:** [PROMPT.md](./PROMPT.md) (identical for every run)

## Summary

| Model | Bug found? | Fix | Tests | pytest | Pros (short) | Cons (short) |
| --- | --- | --- | --- | --- | --- | --- |
| **Composer 2.5** | Yes | `left = mid + 1` | 5 cases | Pass | Agent runs pytest; minimal diff | Heavier agent loop |
| **Grok 4.7** | Yes | `left = mid + 1` | 5 cases | Pass | Strong loop-invariant explanation | Extra assertions beyond minimum |
| **GPT-5.4** | Yes | `left = mid + 1` | 5 cases | Pass | Fast, focused tests | More harness overhead in agent mode |

All three models converged on the **same correct one-line fix** for the intentional bug in `sample_snippet.py`. Outputs live under `runs/composer`, `runs/grok`, and `runs/gpt` (each with `RUN_NOTES.md`).

## The prompt (verbatim)

```
Read sample_snippet.py in this project.

1. Explain what binary_search is supposed to do and where the bug is.
2. Fix the bug with the smallest correct change.
3. Add test_binary_search.py with pytest cases: empty list, single element (found/missing), two elements, and a longer list including a missing value.
4. Run pytest and confirm tests pass.
```

## Run 1 — Composer 2.5

See [runs/composer/RUN_NOTES.md](./runs/composer/RUN_NOTES.md).

**Pros:** Executes tests in-repo; explains infinite-loop symptom clearly.  
**Cons:** Slower/costlier than a lightweight chat-only model for a one-line fix.

## Run 2 — Grok 4.7

See [runs/grok/RUN_NOTES.md](./runs/grok/RUN_NOTES.md).

**Pros:** Precise inclusive-bounds reasoning; tests passed on first run.  
**Cons:** Test file includes a few extra assertions (helpful but not minimal).

## Run 3 — GPT-5.4

See [runs/gpt/RUN_NOTES.md](./runs/gpt/RUN_NOTES.md).

**Pros:** Quick diagnosis; clean edge-case coverage.  
**Cons:** Without agent mode you must run pytest manually to verify.

## Takeaway

For **debug + verify** in a real folder, use **Composer** or another agent-capable model. For **explain-only**, a faster model may suffice. For this task, **quality was similar** once each model understood binary-search bounds—the differentiator was **tool use** (running pytest) and **verbosity**, not the fix itself.

## MLH submission

Screenshot: [screenshots/mlh-benchmark.png](./screenshots/mlh-benchmark.png)
