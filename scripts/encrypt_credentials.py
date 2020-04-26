"""Script to encrypts credentials for Travis CI."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-27 09:07:04
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-27 09:34:23

from os.path import dirname, realpath
from os import walk, system

OS_COMMAND = 'cd {} & travis encrypt {}={} --add env.global'

repo = dirname(dirname(realpath(__file__)))

for root, _, files in walk(repo):
    for file in files:
        if file.endswith('.creds'):
            with open(root + '/' + file) as f:
                cred = f.read()
            system(OS_COMMAND.format(repo, file.split('.')[0], cred))
