#!/bin/bash

# configure the aws cli
aws configure set aws_access_key_id XXXX
aws configure set aws_secret_access_key XXXX
aws configure set default.region us-west-2

# Log ingto aws ecr
sudo $(aws ecr get-login --region us-west-2 --no-include-email)

# Run the devenv docker container
sudo docker run -d -p 5901:5901 -p 6901:6901  302871019511.dkr.ecr.us-west-2.amazonaws.com/league/devenv:PROD
