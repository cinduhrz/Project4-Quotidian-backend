#!/usr/bin/env bash

# exit on error
set -o errexit

# Install dependencies
pip install -r dependencies.txt

# run migrations in case any hadn't been run yet
python manage.py migrate