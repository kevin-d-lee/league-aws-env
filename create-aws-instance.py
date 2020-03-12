#!/usr/bin/python3
import subprocess
import json
import time

# Create a new EC2 instances from special AMI instance
#    The specialized AMI instance included the installation of AWS CLI and docker
# Pass in the shell script to use when starting the instance
#    This script will log into the AWS container registry and download/run the specialized container
awscmd = [ "aws", "ec2",
           "run-instances",
           "--image-id", "ami-0b41ecd4a5e092f48",
           "--count", "1",
           "--instance-type", "t2.large",
           "--key-name", "test-aws-key",
           "--security-group-ids", "sg-0f1ff8616d62354cb",
           "--user-data", "file://aws-instance-startup.sh" ]

result = subprocess.run(awscmd,stdout=subprocess.PIPE)
parse_result = json.loads(result.stdout)
instance_id = parse_result['Instances'][0]['InstanceId']
print( instance_id )

# Command to figure out the IP address of the newly created EC2 instance
dnscmd = [ "aws", "ec2",
           "describe-instances",
           "--instance-ids", instance_id,
           "--query", "Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName" ]

time.sleep(10)  # delay before looking up DNS public name

dns_result = subprocess.run(dnscmd,stdout=subprocess.PIPE)
dns_result_str = dns_result.stdout

dns_result_str = dns_result_str.decode('ASCII')

dns_result_str = dns_result_str.rstrip() # get rid of newline

dns_result_str = dns_result_str.replace('"', '') # remove quotes from string

print( 'Use this URL to access the IDE Development Environment' )
print( 'http://' + dns_result_str + ':6901' )

