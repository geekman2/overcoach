#!/bin/bash

function error_handler {
	original_message=`git log -1 --pretty=%B`
	error_message=`cat error.log`
	full_message=`echo $original_message \n\n $error_message`
	git commit --amend -m "$full_message"
	
	echo $error_message
	exit 1
}

git add .
git commit -m "$*"
rm -f images/*
#docker build -t overcoach .
docker run -v $PWD:/code overcoach 2> error.log || error_handler()
eog images/*
