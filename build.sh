#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install

pip install -r python manage.py requirements.txt
# pip install --upgrade pip

python manage.py collectstatic --no-input
python manage.py migrate