#!/bin/bash

# Update repositories
sudo apt-get update

# Install pip
sudo apt install -y python-pip

# Install Flask
pip install Flask

# Install psutil to get system information
pip install psutil

# Run Python file
python mystatus.py