# Contributing to rag-eval-kit

First off, thank you for considering contributing to `rag-eval-kit`! Your help is appreciated.

Following these guidelines helps maintainers and the community understand your contribution and integrate it smoothly.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to mizokuiam@github.com.

## How Can I Contribute?

There are many ways to contribute, from reporting bugs to writing code or improving documentation.

### Reporting Bugs

*   **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/Mizokuiam/rag-eval-kit/issues).
*   If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/Mizokuiam/rag-eval-kit/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample or an executable test case** demonstrating the expected behavior that is not occurring.
*   Use the "Bug Report" template if available.

### Suggesting Enhancements

*   Open a new issue using the "Feature Request" template.
*   Clearly describe the enhancement, why it's needed, and potential implementation ideas.

### Pull Requests

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally: `git clone git@github.com:YOUR_USERNAME/rag-eval-kit.git`
3.  **Create a virtual environment** and install dependencies:
    ```bash
    cd rag-eval-kit
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt -r requirements-dev.txt
    ```
4.  **Create a branch** for local development: `git checkout -b name-of-your-bugfix-or-feature` (Use a descriptive name).
5.  **Make your changes** locally.
6.  **Write tests** that show your fix is effective or your feature works (if applicable).
7.  **Ensure code style and linting:** Run linters before committing.
    ```bash
    black .
    isort .
    flake8 .
    # mypy . # If using mypy
    ```
8.  **Commit your changes:** Use clear and descriptive commit messages. `git commit -m "feat: Add new metric for X"` or `git commit -m "fix: Resolve issue Y in Z"`
9.  **Push your branch** to GitHub: `git push origin name-of-your-bugfix-or-feature`
10. **Open a Pull Request:** Go to the `rag-eval-kit` repository on GitHub and open a PR from your fork's branch to the `main` branch of the original repository.
11. **Fill out the PR template:** Provide a clear description of the changes, link related issues, and check the checklist items.
12. **Address review comments:** Maintainers may ask for changes. Make the required updates.
13. **Update the CHANGELOG:** Add an entry under the `[Unreleased]` section describing your change.

## Development Setup Notes

*   Use a virtual environment to isolate dependencies.
*   Install both `requirements.txt` and `requirements-dev.txt`.
*   Follow the code style enforced by `black` and `flake8`. Consider using `pre-commit` hooks for automation.

Thank you for your contribution!