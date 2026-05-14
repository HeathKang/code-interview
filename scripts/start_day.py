from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def reading_template(today: date) -> str:
    return f"""# Reading Log - {today.isoformat()}

## Article 1
- Source:
- Title:
- Link:
- Summary:
- Why it matters:

## Article 2
- Source:
- Title:
- Link:
- Summary:
- Why it matters:
"""


def leetcode_template(problem_number: str, slug: str, today: date) -> str:
    title = slug.replace("_", " ").title()
    return f'''"""
LeetCode {problem_number} - {title}
Date: {today.isoformat()}
Pattern:
Time:
Space:
Mistakes:
"""


class Solution:
    def solve(self) -> None:
        """Replace with the required LeetCode method signature."""
        raise NotImplementedError
'''


def main() -> None:
    today = date.today()
    month_dir = ROOT / "leetcode" / today.strftime("%Y-%m")
    reading_file = ROOT / "reading" / f"{today.isoformat()}.md"

    ensure_dir(month_dir)
    ensure_dir(ROOT / "reading")
    ensure_dir(ROOT / "notes" / "network")
    ensure_dir(ROOT / "notes" / "database")
    ensure_dir(ROOT / "notes" / "os")

    write_if_missing(reading_file, reading_template(today))

    for filename in ("0000_problem_one.py", "0000_problem_two.py"):
        file_path = month_dir / filename
        write_if_missing(file_path, leetcode_template("0000", filename[:-3], today))

    print(f"Prepared daily scaffold for {today.isoformat()}")
    print(f"- Reading log: {reading_file.relative_to(ROOT)}")
    print(f"- LeetCode directory: {month_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
