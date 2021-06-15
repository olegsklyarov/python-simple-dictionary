#!/usr/bin/env bash

python3 -m vnev .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
