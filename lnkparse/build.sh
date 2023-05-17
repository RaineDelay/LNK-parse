#!/usr/bin/env bash

black *.py
isort --profile black *.py
flake8 *.py
