#!/bin/bash

error() {
	local original_message=`git log -1 --pretty=%B`
	local error_message="$2"
	local full_message=`echo $original_message \n\n $error_message`
	git commit --amend -m "$full_message"
	
	echo $error_message
	exit 1
}

git add .
git commit -m "$*"
rm -f images/*
#docker build -t overcoach .
trap docker run -v $PWD:/code overcoach 0
eog images/*
