# RUN_NOTES — Composer 2.5

## Bug explanation

`binary_search` should return the index of `target` in a sorted list or `-1`. With inclusive bounds, `left = mid` when `sorted_values[mid] < target` fails to shrink the interval (when `left == mid` the loop never progresses), causing an infinite loop for many missing targets.

## Exact fix

`left = mid + 1`

## Pytest output summary

```
.....                                                                    [100%]
5 passed in 0.01s
```

## Pros and cons

**Pros**

- Ran pytest in the workspace via agent tools; minimal one-line fix.
- Clear explanation tied to loop invariant / infinite-loop symptom.

**Cons**

- Agent workflow adds latency versus inline chat-only answers.
- Easy to over-scope (extra tooling) for a tiny bug if you disable execution.
