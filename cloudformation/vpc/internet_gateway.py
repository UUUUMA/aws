#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_tag

def get_template(config):
    template = { }

    template['InternetGeteway'] = {
        'Type': 'AWS::EC2::InternetGateway',
        'Description': 'InternetGateway for VPC',
        'Properties': {
            'Tags': get_tag(config, 'InternetGateway'),
        },
    }

    template['InternetGetewayAttachment'] = {
        'Type': 'AWS::EC2::VPCGatewayAttachment',
        'Description': 'InternetGateway attach to VPC',
        'Properties': {
            'VpcId': { 'Ref': 'VPC' },
            'InternetGatewayId': { 'Ref': 'InternetGeteway' },
        },
    }

    return template
