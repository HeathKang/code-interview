# Code Interview Practice Repo

This repository is a daily interview practice workspace centered on three habits:

- solve `2` LeetCode problems per day,
- review `2` short CS knowledge cards,
- read `1-2` current tech or AI articles.

The structure is intentionally simple so the maintenance cost stays low.

## Workflow
Run the daily scaffold script before you start:

```bash
python3 scripts/start_day.py
```

That creates today's reading note and two empty LeetCode stubs under the current month.

Suggested daily cadence:

1. Solve one new problem.
2. Re-solve one old problem or a same-pattern variant.
3. Add two short notes under `notes/`.
4. Read and summarize one or two articles in `reading/YYYY-MM-DD.md`.
5. Update `progress.md`.

## Layout
- `leetcode/`: Python solutions and short per-problem notes.
- `notes/`: short review cards for networks, databases, and operating systems.
- `reading/`: daily article logs with links and takeaways.
- `scripts/`: helper scripts for creating daily scaffolds.
- `progress.md`: daily checklist and weekly review log.

## Naming
- LeetCode files: `leetcode/YYYY-MM/0001_two_sum.py`
- Knowledge notes: `notes/network/tcp_vs_udp.md`
- Reading logs: `reading/YYYY-MM-DD.md`

## Sources
Good default reading sources:

- `https://news.ycombinator.com/`
- `https://simonwillison.net/`
- `https://www.infoq.com/`
- engineering blogs from OpenAI, Anthropic, Cloudflare, Stripe, and database vendors
