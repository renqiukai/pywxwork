# Repository Guidelines

## Project Structure & Module Organization

`pywxwork/` contains the installable Python package for WeCom server APIs. Shared HTTP behavior lives in `pywxwork/base.py`, token handling in `pywxwork/token.py`, and API groups are organized by domain: `contact/`, `customer/`, `externalcontact/`, `message/`, `webhook/`, `invoice/`, and `calendar/`.

Top-level `test_*.py` files are integration examples and smoke tests. `setup.py` defines package metadata and dependencies. `README.md` documents usage examples. `publish.sh` and `publish.bat` are release helpers.

## Build, Test, and Development Commands

- `python -m pip install -e .` installs the package in editable mode for local development.
- `python -m pip install requests loguru pytest twine` installs runtime and dev tools.
- `python -m pytest` runs top-level `test_*.py` tests. Many tests call real WeCom APIs, so provide valid local credentials first.
- `python setup.py sdist build` builds source and build artifacts.
- `sh publish.sh` rebuilds and uploads `dist/*` with `twine`; use only for an intentional PyPI release.

## Coding Style & Naming Conventions

Use Python 3 with 4-space indentation. Follow the existing wrapper style: one class per API resource, lowercase module and class names matching current patterns (`user`, `department`, `webHook`), and methods named after WeCom API actions. Route HTTP calls through `base.request(...)`.

Prefer explicit dictionaries for `params` and `json` payloads. Use `loguru.logger` for error logging. Add short docstrings when arguments or WeCom behavior are not obvious.

## Testing Guidelines

Name tests `test_*.py` so `pytest` can discover them. For new API wrappers, include a smoke test or example for the method signature and expected response shape. Avoid hardcoded production credentials, tokens, customer IDs, or phone numbers; read them from ignored local config or environment variables.

When a test requires live WeCom access, make that dependency clear and keep assertions focused on stable fields such as `errcode`.

## Commit & Pull Request Guidelines

Recent history uses concise messages such as `feat: ...`, `docs: ...`, and plain imperative summaries. Prefer `type: summary` for new commits, for example `feat: add ticket API wrapper` or `fix: preserve access_token params`.

Pull requests should describe the changed API area, list affected modules, mention live API testing, and link the relevant WeCom documentation page when adding or changing endpoints.

## Security & Configuration Tips

Do not commit `token.conf`, real corp secrets, access tokens, or generated `.DS_Store` files. Treat `test.py` and other integration scripts as local examples unless they have been sanitized.
