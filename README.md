# Python Testing Lab: TDD (Test-Driven Development)

This repository was forked from [johnxu21/tdd](https://github.com/johnxu21/tdd), which contains starter code for TDD exercises.

I have completed the Python Testing Lab from Prof. John Businge (johnxu21) in CS472-1001 Spring 2024.

## Completed Files

In this repository, you will find my completed implementation in the following files:

- `src/counter.py`
- `tests/test_counter.py`

## GitHub Workflow: CI Workflow

I have implemented a GitHub workflow named "CI workflow." This workflow is triggered on push or pull-request events on the main branch and performs the following tasks:

1. **Checkout:** Checks out the current main branch files so the workflow can access them.
2. **Install Dependencies:** Installs dependencies from `requirements.txt`, which exists in the repository.
3. **Lint with Flake8:** Verifies that the style and syntax of files adhere to Flake8 guidelines.
4. **Run Unit Tests with Nose:** Executes "nosetests" to validate the correctness of test files and their coverage.

This workflow ensures that the codebase is consistent, well-styled, and the tests provide sufficient coverage.

Feel free to explore the code and reach out if you have any questions!
