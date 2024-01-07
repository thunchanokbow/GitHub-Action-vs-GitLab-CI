# GitHub Actions

- [Create YAML contents](01-github-actions.md#Create-YAML-contents)
- [Viewing workflows results](01-github-actions.md#Viewing-workflows-results)

You only need a GitHub repository to create and run a GitHub Actions workflow. This guide will show you how to create a workflow that runs some basic tasks.

### Check that this step has been completed before STAR
- Create a repository on GitHub.
- Upload python script.

## Create YAML contents
To create a yaml file, follow these steps:
1. Create a `.github/workflows` directory in your GitHub repository if it does not already exist.
2. In the `.github/workflows` directory, create a file named `ci.yml`.
3. Copy the following YAML contents into `ci.yml` file:
```
name: CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

  workflow_dispatch:  

jobs:
  build:
    runs-on: macos-latest

    steps:
      - uses: actions/checkout@v2

      - name: List all ORIGINAL files
        run: ls

      - name: Install Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install pandas
        run: python -m pip install pandas

      - name: Install openpyxl
        run: python -m pip install openpyxl  

      - name: Run Python Script
        run: python get_time_series.py

      - name: List all NEW files
        run: ls
```
#### Events that trigger the workflow
- When a push is made to the `'master'` branch.
- When a pull request is opened against the `'master'` branch.
- When the workflow is manually triggered.
#### Jobs to be executed
- Job named `'build'`.
- Runs on the latest macOS runner.
- Steps to be executed within the job.<br>
   [  ] Checkout the repository's code.<br>
   [  ] List all files before the job's actions.<br>
   [  ] Set up Python environment.<br>
   [  ] Install required Python libraries.<br>
   [  ] Run the Python script.<br>
   [  ] List all files after the job's actions. <br><br>
For more information about Workflow syntax.[Here](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

4. Click `'Commit changes..'`
