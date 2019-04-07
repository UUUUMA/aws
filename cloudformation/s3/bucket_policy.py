#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.util.util import get_resource_name

def get_template(config):
    template = { }

    bucket_name = get_resource_name(config, 'Deploy').lower()

    template['BucketPolicy'] = {
        'Type': 'AWS::S3::BucketPolicy',
        'DependsOn': 'DeployS3',
        'Properties': {
            'Bucket': bucket_name,
            'PolicyDocument': {
                'Statement': [
                    {
                        'Effect': 'Allow',
                        'Principal': {
                            'AWS': {'Ref': 'AWS::AccountId'},
                        },
                        'Action': [
                            's3:ListBucket',
                        ],
                        'Resource': {'Fn::Sub': 'arn:aws:s3:::${DeployS3}'},
                    },
                    {
                        'Effect': 'Allow',
                        'Principal': {
                            'AWS': {'Ref': 'AWS::AccountId'},
                        },
                        'Action': [
                            's3:GetObject',
                            's3:PutObject',
                            's3:DeleteObject',
                        ],
                        'Resource': {'Fn::Sub': 'arn:aws:s3:::${DeployS3}/*'},
                    }
                ],
            },
        },
    }

    return template
