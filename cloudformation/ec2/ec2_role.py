#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_resource_name

def get_template(config):
    template = { }

    bucket_name = get_resource_name(config, 'Deploy').lower()

    template['EC2Profile'] = {
        'Type': 'AWS::IAM::InstanceProfile',
        'Properties': {
            'Roles': [
                { 'Ref': 'EC2Role' },
            ],
        },
    }

    template['EC2Role'] = {
        'Type': 'AWS::IAM::Role',
        'Properties': {
            'RoleName': get_resource_name(config, 'EC2Role'),
            'AssumeRolePolicyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Sid': '1',
                        'Effect': 'Allow',
                        'Principal': {
                            'Service': [
                                'ec2.amazonaws.com',
                            ],
                        },
                        'Action': 'sts:AssumeRole',
                    },
                ],
            },
            'Policies': [
                {
                    'PolicyName': 'GetS3Object',
                    'PolicyDocument': {
                        'Statement': [
                            {
                                'Effect': 'Allow',
                                'Action': [
                                    's3:Get*',
                                    's3:List*',
                                    's3:DeleteObject'
                                ],
                                'Resource': [
                                    f'arn:aws:s3:::{ bucket_name }',
                                    f'arn:aws:s3:::{ bucket_name }/*',
                                ],
                            },
                        ],
                    },
                },
                {
                    'PolicyName': 'initializeSSMAgent',
                    'PolicyDocument': {
                        'Statement': [
                            {
                                'Effect': 'Allow',
                                'Action': [
                                    'ssm:UpdateInstanceInformation',
                                    'ssm:ListAssociations',
                                    'ssm:ListInstanceAssociations',
                                    'ssmmessages:CreateControlChannel',
                                    'ec2messages:GetMessages',
                                ],
                                'Resource': '*',
                            },
                        ],
                    },
                },
            ],
        },
    }

    return template
