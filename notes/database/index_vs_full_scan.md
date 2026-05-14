# Index vs Full Scan

- What it is: An index narrows the search space; a full scan reads every row or page.
- Why it matters: Many query optimization questions reduce to whether the database can avoid scanning the full dataset.
- Interview answer: Indexes speed selective lookups but add write cost and storage overhead.
- Common confusion: An index is not always beneficial; low-selectivity predicates may still lead the optimizer to scan.
