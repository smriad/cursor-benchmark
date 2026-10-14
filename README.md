# Cursor model benchmark (GHW Hacktoberfest)

Minimal repo for **[CHALLENGE 2: Benchmark Cursor’s Models](https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11d25-134c-17e5-e22c-8af278534580)** — same prompt, up to three different Cursor models.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## How to benchmark

1. **Reset the bug** (optional, for a fair re-run): change `left = mid + 1` back to `left = mid` in `sample_snippet.py` and delete `test_binary_search.py`.
2. Open **New Chat**, pick a **model**, paste the prompt from [PROMPT.md](./PROMPT.md).
3. Repeat in **new chats** with two other models (e.g. Grok 4.7, GPT-5.4, Claude Sonnet).
4. Write pros/cons in [RESULTS.md](./RESULTS.md) and take a **screenshot** for MLH.

## Results

Full write-up: [RESULTS.md](./RESULTS.md). Per-model artifacts: `runs/composer`, `runs/grok`, `runs/gpt`.

## Submit

[Create submission](https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11d25-134c-17e5-e22c-8af278534580/submissions/new) with your description + screenshot (`screenshots/mlh-benchmark.png`).
