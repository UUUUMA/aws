#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3

def get_resource_name(config, service_name):
    return '-'.join([
        config["system_id"],
        config["system_name"],
        service_name
    ]).upper()

def get_tag(config, service_name, *additional):
    tags = [
        {
            'Key': 'ID',
            'Value': config['system_id'].upper()
        },
        {
            'Key': 'Name',
            'Value': get_resource_name(config, service_name)
        },
        {
            'Key': 'Service',
            'Value': service_name
        },
    ]

    if len(additional) > 0:
        tags.extend(additional)

    return tags

def get_stack_resources(stack_name, logical_resource_id):
    client = boto3.client('cloudformation')

    response = client.describe_stack_resources(
        StackName = stack_name,
        LogicalResourceId = logical_resource_id
    )

    return response['StackResources'][0]
