#!/usr/bin/env bash

if [ ! -d ".venv" ];
then
    if [ ! -f "requirements.txt" ]; then
        echo "This is not the root of the Repository. (Or requirements.txt missing...) Aborting...";
        exit 1;
    fi;
    
    echo "Creating Virtual Environment...";

    if [ ! "$(command -v python3)" ]; then
        echo "Python3 not present. Aborting...";
        exit 1;
    fi

    echo "Running command : python3 -m venv .venv";

    python3 -m venv .venv;

    echo "Setting Up Virtual Environment complete...";
    
else
    echo "Virtual Environment exists. Skipping installation.";
fi;

sleep 1;

if [ ! "$(command -v .venv/bin/python)" ]; then 
    echo "Venv incorrectly installed, please check and manually delete the .venv directory...Aborting...";
    exit 1;
fi

echo "Running command : .venv/bin/python -m pip install -r requirements.txt";

.venv/bin/python -m pip install -r requirements.txt

echo "Setting up python complete...";

sleep 3;
