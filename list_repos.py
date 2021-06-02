#!/bin/python
#
# list_repos.py - for list all repos
#
# Created by Bensuperpc(Bensuperpc@gmail.com) 02 June 2021
# Updated by Bensuperpc(Bensuperpc@gmail.com) 02 June 2021
# 
#
# Released into the Public domain with MIT licence
# https://opensource.org/licenses/MIT
#
# Written with Visual Studio code 1.55.2 and python 3.9.5
# Updated with Visual Studio code 1.55.2 and python 3.9.5
# Script compatibility : Windows, Linux, Mac
# Script requirement : python 3.5 and above
#
# ==============================================================================
from github import Github

# using an access token : https://github.com/settings/tokens
g = Github()
with open('private.key') as f:
    g = Github(f.readline().strip())
    
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

for repo in g.get_user().get_repos():
    print(repo.name)
