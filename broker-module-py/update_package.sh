#!/bin/bash

echo "Starting upload..."
rm -rf build
rm -rf dist
rm -rf brokerstream.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*
echo "Done."
