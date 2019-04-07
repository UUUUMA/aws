#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.codedeploy import code_deploy
from cloudformation.codedeploy import code_deploy_role

def get_template_codedeploy(config):
    resources = { }

    resources.update(code_deploy.get_template(config))
    resources.update(code_deploy_role.get_template(config))

    return {
        'AWSTemplateFormatVersion': '2010-09-09',
        'Description': f'VPC for { config["system_name"] }',
        'Resources': resources,
    }
