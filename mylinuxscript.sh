#!/bin/bash

# Install Flask
pip install Flask

# Run Python file
mystatus.py

# Go to https:$publicIp/status
curl https:$publicIp/status