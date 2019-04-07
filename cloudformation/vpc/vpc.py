#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_tag

def get_template(config):
    template = { }

    template['VPC'] = {
        'Type': 'AWS::EC2::VPC',
        'Description': f'VPC for { config["system_name"] }'
                       + f' in { config["stage"] }',
        'Properties': {
            'CidrBlock': config['vpc']['cider_block'],
            'Tags': get_tag(config, 'VPC'),
        },
    }

    return template
