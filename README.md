[![Python application test with Github Actions](https://github.com/Akash265/DevOps/actions/workflows/devops.yml/badge.svg)](https://github.com/Akash265/DevOps/actions/workflows/devops.yml)
[![Python application test with Github Actions](https://codebuild.eu-north-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiMm5TdzkzTFQ4ZHd3aUlWcWVIaVpmdDVsV0c5Slh4eU9JVUk4aENJWDFtSWxkMkVEeWtHTnorMThSRlJmR1hKSWdINXpjQXFyRmV4eUp3T0VYSTdFQWp3PSIsIml2UGFyYW1ldGVyU3BlYyI6ImF1d0tVWk56VTRxbkQ5bjQiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
# DevOps

### Steps:

1. Create a virtual environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
2. Create empty files: `Makefile`, `requirements.txt`, `Dockerfile`, `main.py`, `mylib/__init__.py`
3. Populate the `Makefile`
4. Setup continuous integration i.e. check the code for issues like lint errors.
5. Build cli using python Fire library `./cli-fire.py --help` to test logic
