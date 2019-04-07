#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cloudformation.util.util import get_tag
from cloudformation.util.util import get_resource_name

def get_template(config):
    template = { }

    application_name = get_resource_name(config, 'CodeDeploy').upper()
    group_name = get_resource_name(config, 'DeploymentGroup').upper()
    bucket_name = get_resource_name(config, 'Deploy').lower()

    template['CodeDeploy'] = {
        'Type': 'AWS::CodeDeploy::Application',
        'Description': f'Code deploy for { config["system_name"] } ec2'
                       + f' in { config["stage"] }',
        'Properties': {
            'ApplicationName': application_name,
            'ComputePlatform': 'Server',
        },
    }

    template['DeploymentGroup'] = {
        'Type': 'AWS::CodeDeploy::DeploymentGroup',
        'Description': f'Deployment group for { config["system_name"] } ec2'
                       + f' in { config["stage"] }',
        'DependsOn': 'CodeDeployRole',
        'Properties': {
            'ApplicationName': application_name,
            'DeploymentGroupName': group_name,
            'Deployment': {
                'Revision': {
                    'RevisionType': 'S3',
                    'S3Location': {
                        'Bucket': bucket_name,
                        'BundleType': 'zip',
                        'Key': 'src.zip',
                    },
                },
            },
            'ServiceRoleArn': { 'Fn::GetAtt': ['CodeDeployRole', 'Arn'] },
            'Ec2TagFilters': get_tag_filters(config),
        },
    }


    return template

def get_tag_filters(config):
    tags = get_tag(config, 'EC2')

    for tag in tags:
        tag.update({ 'Type': 'KEY_AND_VALUE' })

    return tags
