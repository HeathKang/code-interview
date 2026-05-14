# Repository Guidelines

## Project Structure & Module Organization
This repository is currently an empty scaffold. Add application code under `src/`, place automated tests in `tests/`, and keep static assets in `assets/` if the project needs images, fixtures, or sample data. Store project-level configuration at the repository root, for example `package.json`, `pyproject.toml`, or `Makefile`.

Keep modules small and focused. Mirror the `src/` layout inside `tests/` where practical so contributors can quickly locate coverage for a given feature.

## Build, Test, and Development Commands
No build or test tooling is configured yet. When introducing tooling, prefer a small, predictable command surface and document it in this file and the main README.

Examples:
- `make test` runs the full automated test suite.
- `make lint` runs formatting and static checks.
- `make dev` starts the local development entry point.

If you add language-specific commands such as `npm test` or `pytest`, keep them wrapped in a stable top-level script or `Makefile` target.

## Coding Style & Naming Conventions
Use consistent 4-space indentation unless the adopted language ecosystem strongly prefers otherwise. Name files and modules by purpose using lowercase, with `kebab-case` for frontend assets and `snake_case` for Python-style modules. Use `PascalCase` for classes and `camelCase` only where required by the language or framework.

Adopt an automated formatter and linter as soon as the first language/toolchain is chosen. Do not mix styles within the same directory tree.

## Testing Guidelines
Place tests in `tests/` and name them after the unit under test, such as `tests/test_parser.py` or `tests/auth.spec.ts`. Add at least one automated test for each non-trivial feature or bug fix. Prefer fast, isolated tests over broad end-to-end coverage until the project architecture is established.

## Commit & Pull Request Guidelines
There is no Git history in this workspace yet, so follow a simple standard: write short, imperative commit subjects like `Add API client skeleton` or `Fix input validation`.

Pull requests should include:
- a brief description of the change,
- the reason for the change,
- test evidence or a note explaining why tests were not added,
- screenshots or sample output when UI or CLI behavior changes.

## Agent-Specific Notes
Before adding new directories or tooling, update this guide so future contributors can follow the same structure and commands.

For reviewed LeetCode solutions, use a fixed comment template so each file is easy to revisit:
- `Original Code`: preserve the user's original attempt in a short commented block.
- `Key Point`: summarize the main algorithm idea or invariant, such as two pointers, binary search, or DP state.
- `Better Version`: keep the corrected or more canonical implementation as the executable code.

Keep these review notes concise and optimized for later self-review, not long-form tutorials.
