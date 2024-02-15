#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install

pip install -r python3 manage.py requirements.txt
# pip install --upgrade pip

python3 manage.py collectstatic --no-input
python3 manage.py migrate