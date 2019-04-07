#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_tag

def get_template(config):
    template = { }

    template['SecurityGroup'] = {
        'Type': 'AWS::EC2::SecurityGroup',
        'Description': f'SecurityGroup in { config["stage"] }',
        'Properties': {
            'GroupDescription': 'Simple Group for EC2',
            'VpcId': { 'Ref': 'VPC' },
            'SecurityGroupIngress': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                },
                {
                    'CidrIp': '0.0.0.0/0',
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                },
            ],
            'Tags': get_tag(config, 'SecurityGroup'),
        },
    }

    return template
