#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os.path as path
from importlib import import_module
from time import sleep

root_dir = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.append(root_dir)

import yaml
import boto3

def get_config(env):
    common_config = { }
    env_config = { }

    # get config (common and env)
    with open(path.join('config', 'common.yml')) as f:
        common_config = yaml.load(f)

    with open(path.join('config', f'{ env }.yml')) as f:
        env_config = yaml.load(f)

    common_config.update(env_config)

    return common_config

def create_template(config, suffix):
    get_template = getattr(
        import_module(f'cloudformation.template_{ suffix }'),
        f'get_template_{ suffix }'
    )

    template = get_template(config)

    dest_path = path.join('cloudformation', 'dest')

    with open(path.join(dest_path, f'template_{ suffix }.yaml'), 'w') as f:
        f.write(yaml.dump(template, default_flow_style=False))

def exec_template(suffix):
    cloudformation_client = boto3.client('cloudformation')

    dest_file = path.abspath(path.join(
        'cloudformation',
        'dest',
        f'template_{ suffix }.yaml'
    ))

    template_body = ''
    with open(dest_file) as f:
        template_body = f.read()

    print(template_body)

    try:
        cloudformation_client.create_stack(
            StackName = f'uma-example-{ suffix }'.upper(),
            TemplateBody = template_body,
            Capabilities = ['CAPABILITY_NAMED_IAM'],
        )
    except:
        cloudformation_client.update_stack(
            StackName = f'uma-example-{ suffix }'.upper(),
            TemplateBody = template_body,
            Capabilities = ['CAPABILITY_NAMED_IAM'],
        )

if __name__ == '__main__':
    args = sys.argv

    if not len(args) == 3:
        raise Exception(f'arguments must be 3 (given { len(args) } arguments)')

    config = get_config(args[1])
    create_template(config, args[2])
    exec_template(args[2])
