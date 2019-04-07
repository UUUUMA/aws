#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cloudformation.vpc import vpc
from cloudformation.vpc import subnet
from cloudformation.vpc import internet_gateway
from cloudformation.vpc import route
from cloudformation.vpc import security_group

def get_template_vpc(config):
    resources = { }

    resources.update(vpc.get_template(config))
    resources.update(subnet.get_template(config))
    resources.update(internet_gateway.get_template(config))
    resources.update(route.get_template(config))
    resources.update(security_group.get_template(config))

    return {
        'AWSTemplateFormatVersion': '2010-09-09',
        'Description': f'VPC for { config["system_name"] }',
        'Resources': resources,
    }
