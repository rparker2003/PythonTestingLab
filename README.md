# Python Testing Lab: TDD (Test-Driven Development)

## Overview:
This repository is a fork of [johnxu21/tdd](https://github.com/johnxu21/tdd), serving as part of the Python Testing Lab 
focusing on Test-Driven Development (TDD). This lab explores the principles of TDD, where test cases are authored before 
the actual code, promoting robust software development practices.

The repository was split into two labs which can be found on John Businge's website:
- [Dynamic Analysis](https://johnxu21.github.io/teaching/CS472/Timetable/dynamic_analysis/?) - Task 5
- [CI - Using GitHub Actions - Setting up workflow](https://johnxu21.github.io/teaching/CS472/Timetable/CI/?) - All Tasks


## Completed Files
- **.github/workflows/workflow.yml:** This file contains the configuration for a GitHub workflow named "CI workflow." This workflow automates various tasks such as dependency installation, linting, and running unit tests upon code changes to ensure code consistency and correctness.
- **src/counter.py:** This file contains the implementation of a simple counter application following REST API guidelines. The implementation includes endpoints for creating counters and handling duplicate counter names.
- **tests/test_counter.py:** This file houses the test cases written to validate the functionality of the counter application. Test cases cover scenarios such as creating a counter, handling duplicate counters, and verifying HTTP status codes.


## Validation Process:
1. **Understanding Requirements:** Initially, we reviewed the requirements provided for the lab, which outlined the functionality expected from the counter application.
2. **Writing Test Cases:** Following TDD principles, we wrote test cases in the `test_counter.py` file to validate different aspects of the counter application, such as creating counters and handling duplicates.
3. **Implementing Code:** With test cases in place, we proceeded to implement the code necessary to make those tests pass. This involved creating the `counter.py` file and defining endpoints and logic to fulfill the specified requirements.
4. **Running Tests:** After implementing the code, we ran the test suite using `nosetests` to verify the correctness of our implementation. Tests were executed to ensure that the application functions as expected and returns the correct HTTP status codes.
5. **Refactoring:** Throughout the process, we refactored the code to improve readability, maintainability, and efficiency. This included extracting common functionality into reusable functions and enhancing error handling.


## Github Workflow: CI Workflow
To automate the validation process and ensure code quality, we implemented a GitHub workflow named "CI workflow." This workflow is triggered on push or pull-request events on the main branch and performs the following tasks:
- **Checkout:** Checks out the current main branch files to access the codebase.
- **Install Dependencies:** Installs necessary dependencies from `requirements.txt`.
- **Lint with Flake8:** Verifies code style and syntax adherence using Flake8.
- **Run Unit Tests with Nose:** Executes test cases using `nosetests` to validate functionality and coverage.


## Conclusion:
Following the TDD approach and leveraging automated testing with GitHub workflows ensured that the counter application met the specified requirements, adhered to coding standards, and maintained robust test coverage. This lab provided valuable hands-on experience in TDD methodologies and CI/CD practices, enhancing our software development and quality assurance skills.

Feel free to explore the code and reach out with any questions or feedback!
