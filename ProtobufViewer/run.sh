#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR
./protoc --python_out=./ -I./pb ./pb/*.proto
PYTHONPATH=${PYTHONPATH}:../ python pb_parse.py
