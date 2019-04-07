#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_tag

def get_template(config):
    template = { }

    for az, cider_block in config['subnet'].items():
        upper_camel_az = ''.join(map(lambda s: s.capitalize(), az.split('-')))

        template[f'Subnet{ upper_camel_az }'] = {
            'Type': 'AWS::EC2::Subnet',
            'Description': f'Subnet for { config["system_name"] } VPC'
                           + f' at { az } in { config["stage"] }',
            'Properties': {
                'VpcId': { 'Ref': 'VPC' },
                'AvailabilityZone': az,
                'CidrBlock': cider_block,
                'Tags': get_tag(
                    config,
                    f'Subnet',
                    { 'Key': 'AZ', 'Value': az },
                ),
            },
        }

    return template
