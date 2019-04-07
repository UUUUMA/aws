#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cloudformation.util.util import get_tag
from cloudformation.util.util import get_resource_name

def get_template(config):
    template = { }

    bucket_name = get_resource_name(config, 'Deploy').lower()

    template['CodeDeployRole'] = {
        'Type': 'AWS::IAM::Role',
        'Properties': {
            'RoleName': get_resource_name(config, 'CodeDeployRole'),
            'AssumeRolePolicyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Sid': '1',
                        'Effect': 'Allow',
                        'Principal': {
                            'Service': [
                                'codedeploy.amazonaws.com',
                            ],
                        },
                        'Action': 'sts:AssumeRole',
                    },
                ],
            },
            'ManagedPolicyArns': [
                'arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole',
            ],
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
                # {
                #     'PolicyName': 'PermissionForEC2',
                #     'PolicyDocument': {
                #         'Statement': [
                #             {
                #                 'Effect': 'Allow',
                #                 'Action': [
                #                     'ec2:DescribeInstances',
                #                     'ec2:DescribeInstanceStatus',
                #                     'ec2:TerminateInstances',
                #                     'tag:GetTags',
                #                     'tag:GetResources',
                #                 ],
                #                 'Resource': [
                #                     '*'
                #                 ],
                #             },
                #         ],
                #     },
                # },
            ],
        },
    }

    return template
