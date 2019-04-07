#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cloudformation.util.util import get_tag
from cloudformation.util.util import get_resource_name
from cloudformation.util.util import get_stack_resources

def get_template(config):
    template = { }

    vpc_stack_name = f'{ config["system_name"].upper() }-VPC'

    security_group_id = [
        get_stack_resources(
            vpc_stack_name,
            'SecurityGroup'
        )['PhysicalResourceId']
    ]

    template['EC2'] = {
        'Type': 'AWS::EC2::Instance',
        'Description': f'EC2 for { config["system_name"] }'
                       + f' in { config["stage"] }',
        'Properties': {
            'InstanceType': config['ec2']['instance_type'],
            'ImageId': config['ec2']['image_id'],
            'IamInstanceProfile': { 'Ref': 'EC2Profile' },
            'SecurityGroupIds': security_group_id,
            'SubnetId': config['ec2']['subnet_id'],
            'Monitoring': True,
            'UserData': {
                'Fn::Base64': {
                    'Fn::Sub': '\n'.join([
                        '#!/bin/bash -ex',
                        'yum -y install ruby',
                        # codedeploy
                        'cd /tmp',
                        'wget https://aws-codedeploy-${AWS::Region}.s3.amazonaws.com/latest/install',
                        'chmod +x ./install',
                        './install auto',
                        # cloudwatch logs
                        'yum -y install awslogs',
                        'systemctl start awslogsd.service',
                    ]),
                },
            },
            'KeyName': 'uma',
            'Tags': get_tag(config, 'EC2'),
        },
    }

    template['EIP'] = {
        'Type': 'AWS::EC2::EIP',
        'Description': f'EIP for { config["system_name"] } EC2'
                       + f' in { config["stage"] }',
        'Properties': {
            'InstanceId': { 'Ref': 'EC2' },
        },
    }

    return template
