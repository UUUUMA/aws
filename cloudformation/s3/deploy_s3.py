#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cloudformation.util.util import get_tag
from cloudformation.util.util import get_resource_name

def get_template(config):
    template = { }

    template['DeployS3'] = {
        'Type': 'AWS::S3::Bucket',
        'Description': f'S3 Bucket for { config["system_name"] } deploy'
                       + f' in { config["stage"] }',
        'Properties': {
            'BucketName': get_resource_name(config, 'Deploy').lower(),
            'AccessControl': 'Private',
            'Tags': get_tag(config, 'DeployS3'),
        },
    }

    return template
