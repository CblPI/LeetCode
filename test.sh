#!/bin/sh

python -m pytest -W ignore::DeprecationWarning --cov-config=.coveragerc ./tests --cov=tasks -vv --cov-report=term-missing
