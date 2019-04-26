#!/bin/bash

if [[ "$1" == "start-jupyter" ]]; then

    if [[ -d env ]]; then
        env/bin/pip install --upgrade pip
        env/bin/pip install -r requirements.txt
    else
        python3 -m venv env
        env/bin/pip install --upgrade pip
        env/bin/pip install -r requirements.txt
    fi

    env/bin/jupyter notebook .
fi

if [[ "$1" == "simple-start" ]]; then
    env/bin/jupyter notebook .
fi