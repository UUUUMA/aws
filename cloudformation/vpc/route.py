#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_tag

def get_template(config):
    template = { }

    template['RouteTable'] = {
        'Type': 'AWS::EC2::RouteTable',
        'Description': f'RouteTable for { config["system_name"] }'
                       + f' in { config["stage"] }',
        'Properties': {
            'VpcId': { 'Ref': 'VPC' },
            'Tags': get_tag(config, 'RouteTable'),
        },
    }

    template['Route'] = {
        'Type': 'AWS::EC2::Route',
        'DependsOn': 'InternetGetewayAttachment',
        'Description': f'Route for { config["system_name"] }'
                       + f' in { config["stage"] }',
        'Properties': {
            'RouteTableId': { 'Ref': 'RouteTable' },
            'DestinationCidrBlock': config['route']['cider_block'],
            'GatewayId': { 'Ref': 'InternetGeteway' },
        },
    }

    for az, cider_block in config['subnet'].items():
        upper_camel_az = ''.join(map(lambda s: s.capitalize(), az.split('-')))

        template[f'SubnetRouteTableAssociation{ upper_camel_az }'] = {
            'Type': 'AWS::EC2::SubnetRouteTableAssociation',
            'Description': 'Associate subnet route'
                           + f' table for { config["system_name"] }'
                           + f' at { az } in { config["stage"] }',
            'Properties': {
                'SubnetId': { 'Ref': f'Subnet{ upper_camel_az }' },
                'RouteTableId': { 'Ref': 'RouteTable' },
            },
        }

    return template
