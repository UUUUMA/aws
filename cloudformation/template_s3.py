#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.s3 import deploy_s3
from cloudformation.s3 import bucket_policy

def get_template_s3(config):
    resources = { }

    resources.update(deploy_s3.get_template(config))
    resources.update(bucket_policy.get_template(config))

    return {
        'AWSTemplateFormatVersion': '2010-09-09',
        'Description': f'VPC for { config["system_name"] }',
        'Resources': resources,
    }
