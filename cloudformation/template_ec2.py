#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.ec2 import ec2
from cloudformation.ec2 import ec2_role

def get_template_ec2(config):
    resources = { }

    resources.update(ec2.get_template(config))
    resources.update(ec2_role.get_template(config))

    return {
        'AWSTemplateFormatVersion': '2010-09-09',
        'Description': f'VPC for { config["system_name"] }',
        'Resources': resources,
    }
