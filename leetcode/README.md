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
| Constant-space DP | Build each state from a fixed number of previous states | Previous one or two DP values | Initialize base cases, then scan forward | `0070 Climbing Stairs` |
| Sliding window | Maintain a contiguous range that satisfies a constraint | Left and right boundaries plus window statistics | Two pointers over one array | Longest substring without repeating characters |
| Two pointers | Use two indices to coordinate positions | Two moving indices, sometimes with extra counts | `i` and `j` moving independently | Two Sum II, container-style problems |
| Slow/fast pointers | Move one pointer one step and another two steps to find linked-list structure | Slow pointer, fast pointer, and sometimes previous/cut point | `while fast and fast.next`, then advance `slow` and `fast.next.next` | `0148 Sort List`, linked-list cycle problems |
| Recursive DFS | Query each subtree, then combine the child answers at the current node | Return value from each recursive call | Base case for empty node, then recurse left/right | `0104 Maximum Depth of Binary Tree` |
| Right-first DFS | Visit the preferred side first, then record the first node seen at each depth | Current depth plus result length | Recursive traversal with depth state | `0199 Binary Tree Right Side View` |
| Level-order BFS | Process one tree level at a time so level boundaries are explicit | Queue of nodes in the current frontier | `while queue`, snapshot `level_size`, scan that many nodes | `0199 Binary Tree Right Side View` |
| BST inorder traversal | Use the BST property that inorder visits values in sorted order | Previous inorder value plus best answer so far | Left subtree, current node, right subtree | `0530 Minimum Absolute Difference in BST` |
| Recursive DFS with index map | Rebuild a tree by taking the root from one traversal and splitting left/right ranges in inorder | Traversal boundaries plus value-to-index map | Root from preorder first or postorder last, then recurse on child ranges | `0105` / `0106` build tree |

Quick rule of thumb:

- If you only need a running summary of the past, it is usually one-pass greedy.
- If you only need the farthest reachable position, it is usually greedy reachability.
- If you need to count jumps while expanding reach by layers, it is usually greedy layer expansion.
- If you need to reset a candidate start when a cumulative balance goes negative, it is usually running tank balance.
- If you need to combine left and right context, it is usually prefix and suffix accumulation.
- If each answer depends only on the previous one or two answers, it is usually constant-space DP.
- If you need a contiguous segment that stays valid, it is usually sliding window.
- If the problem is about coordinating two positions, it is usually two pointers.
- If a linked-list problem needs the middle, cycle detection, or a split point, it is usually slow/fast pointers. For merge sort, start `fast = head.next` so `slow` stops at the left half's tail before cutting.
- If you query a tree recursively, first define what each subtree should return, handle the empty-node base case, then combine the left and right answers at the current node.
- DFS key point: choose traversal order deliberately. For right-side view, visit right before left and append only when `depth == len(result)`.
- BFS key point: freeze `level_size = len(queue)` before each level. For right-side view, append the last node processed in that level.
- BST key point: inorder traversal produces sorted values, so ordered comparisons only need the previous visited node.
- If you build a tree from inorder plus preorder/postorder, use preorder's first value or postorder's last value as the root, find that root in inorder, then use the left/right subtree size to calculate both child traversal ranges.

## DP Template

Use this checklist before writing dynamic programming code:

- `State`: define what `dp[i]` means in one sentence.
- `Transition`: write how the current answer comes from previous answers.
- `Base cases`: fill the smallest valid inputs first.
- `Order`: choose the loop order so required previous states already exist.
- `Answer`: return the state that represents the full problem.

For one-dimensional DP:

```python
def solve(nums):
    if not nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = initial_value

    for i in range(1, len(nums)):
        dp[i] = transition_from_previous_states

    return dp[-1]
```

For top-down DP with memoization:

```python
def solve(n):
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]

        if i == base_case:
            return base_value

        memo[i] = transition_from_smaller_states
        return memo[i]

    return dp(n)
```

For constant-space DP:

```python
def solve(n):
    if n <= 2:
        return n

    prev2 = 1
    prev1 = 2

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

DP key point: do not start from code. First name the state and recurrence; the code is just base cases plus either memoization or loop order.
