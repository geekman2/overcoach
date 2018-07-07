#!/bin/bash

git add .
git commit -m "$*"
rm -f images/*
#docker build -t overcoach .
docker run -v $PWD:/code overcoach 
eog images/*
