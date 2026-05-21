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
| Running tank balance | Track cumulative gain/loss and reset when the balance goes negative | Total balance and current tank | Single loop with reset on failure | `0134 Gas Station` |
| Prefix and suffix accumulation | Combine information from left and right passes | Prefix value and suffix value | Two linear passes | `0238 Product of Array Except Self` |
| Sliding window | Maintain a contiguous range that satisfies a constraint | Left and right boundaries plus window statistics | Two pointers over one array | Longest substring without repeating characters |
| Two pointers | Use two indices to coordinate positions | Two moving indices, sometimes with extra counts | `i` and `j` moving independently | Two Sum II, container-style problems |
| Recursive DFS | Query each subtree, then combine the child answers at the current node | Return value from each recursive call | Base case for empty node, then recurse left/right | `0104 Maximum Depth of Binary Tree` |

Quick rule of thumb:

- If you only need a running summary of the past, it is usually one-pass greedy.
- If you only need the farthest reachable position, it is usually greedy reachability.
- If you need to count jumps while expanding reach by layers, it is usually greedy layer expansion.
- If you need to reset a candidate start when a cumulative balance goes negative, it is usually running tank balance.
- If you need to combine left and right context, it is usually prefix and suffix accumulation.
- If you need a contiguous segment that stays valid, it is usually sliding window.
- If the problem is about coordinating two positions, it is usually two pointers.
- If you query a tree recursively, first define what each subtree should return, handle the empty-node base case, then combine the left and right answers at the current node.
