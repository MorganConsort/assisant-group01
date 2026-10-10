# Study Assistant — starter

A starter repository for the CSC10014 Smart Virtual Assistant project.

## Setup
Prerequisites: Python 3.10+, Git

    git clone https://github.com/MorganConsort/lab01-group04.git
    cd lab01-group04
    python -m venv .venv
    #Windows:   source .venv/Scripts.activate #Macs/Linux: source .venv/bin.activate 
    python -m pip install -- upgrade pip
    pip install -r requirements.txt
    pip install - e.

## Run
    python -m assistant "where is the library?"
    # -> Library: room B.201, open Mon-Sat: 07:00-20:00

## Test

    pytest-q #-> 4 passed

## Project structure

TODO
