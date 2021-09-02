#!/usr/bin/env bash

source .venv/bin/activate
FLASK_ENV=development python -m flask run
deactivate
