#!/bin/bash

# Run flake8 to check for linting issues
echo "Running Flake8..."
flake8 --exclude=venv

# Run black to automatically format the code
echo "Running Black..."
black --exclude 'venv' .

# Check for modified files (files that are different from the last commit)
echo "Checking for modified files..."
git diff --name-only

# Check if there are uncommitted changes (modified files)
if [ ! -z "$(git diff --name-only)" ]; then
    echo "Unstaged changes detected. Consider adding files before committing."
    echo "To add them, use 'git add <file>' or 'git add .'"
else
    echo "No changes detected."
fi