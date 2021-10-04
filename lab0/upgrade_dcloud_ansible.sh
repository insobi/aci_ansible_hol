#!/bin/bash

VERSION_ANSIBLE=2.9.13 
VERSION_ANSIBLE_ACI=2.0.0 

yes | pip uninstall ansible
pip install ansible==${VERSION_ANSIBLE}

ansible-galaxy collection install cisco.aci:==${VERSION_ANSIBLE_ACI} 

pip install openpyxl pandas paramiko