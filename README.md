# Python Testing Lab: tdd (test-driven development)
This repo was forked from johnxu21/tdd which contains starter code for TDD exercises

I have completed the Python Testing Lab from Prof. John Businge (johnxu21) in CS472-1001 Spring 2024

In this repository are my completed src/counter.py and tests/test_counter.py files
Also, I have implemented a GitHub workflow called "CI workflow" which when on push or pull-request on the main branch will do 4 things: 
    Checkout - Checks out the current main branch file sos the workflow can access them
    Install dependencies - Installs dependencies from requirements.txt which exists in the repository
    Lint with flake8 - Verifies that the style and syntax of files is proper to flake8 guidelines
    Run unit tests with nose - Runs "nosetests" to display the validity of test files and their coverage