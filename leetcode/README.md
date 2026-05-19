# LeetCode Notes

Store solutions by month using filenames in the form:

`leetcode/YYYY-MM/0121_best_time_to_buy_and_sell_stock.py`

At the top of each file, keep four short fields:

- `Pattern`
- `Time`
- `Space`
- `Mistakes`

This keeps each solution useful for review without turning every file into a long essay.

Use [top_interview_150.md](/home/heath/projects/code-interview/leetcode/top_interview_150.md) as the main priority list. Pick a problem there first, then save your solution under the monthly directory.

## Review Template
When a solution is reviewed and rewritten, prefer this fixed structure inside the file:

- `Original Code`: a short commented copy of the first attempt
- `Key Point`: the core pattern or invariant
- `Better Version`: the improved executable solution

Keep the notes short so they help with future review without turning each file into a full editorial.

## Pattern Glossary

Use these labels when describing the technique behind a solution:

| Pattern | Core idea | State kept | Typical shape | Example use |
|---|---|---|---|---|
| One-pass greedy scan | Make the best local choice while scanning once | A small summary value such as a running minimum or maximum | Single loop | `0121 Best Time to Buy and Sell Stock` |
| Greedy reachability | Track the farthest position reachable so far | Farthest reachable index | Single loop with a fail-fast check | `0055 Jump Game` |
| Greedy layer expansion | Expand the current reachable range one jump at a time | Current layer end and farthest next reach | Single loop with layer boundary updates | `0045 Jump Game II` |
| Sliding window | Maintain a contiguous range that satisfies a constraint | Left and right boundaries plus window statistics | Two pointers over one array | Longest substring without repeating characters |
| Two pointers | Use two indices to coordinate positions | Two moving indices, sometimes with extra counts | `i` and `j` moving independently | Two Sum II, container-style problems |

Quick rule of thumb:

- If you only need a running summary of the past, it is usually one-pass greedy.
- If you only need the farthest reachable position, it is usually greedy reachability.
- If you need to count jumps while expanding reach by layers, it is usually greedy layer expansion.
- If you need a contiguous segment that stays valid, it is usually sliding window.
- If the problem is about coordinating two positions, it is usually two pointers.
