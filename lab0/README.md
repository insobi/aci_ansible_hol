# Lab0

## dCloud 접속 가이드
- [VSCode_dCloud_접속가이드_202110.pdf](./VSCode_dCloud_접속가이드_202110.pdf) 참고

<br>

## dCloud VM - Ansible Upgrade
```
VERSION_ANSIBLE=2.9.13 
VERSION_ANSIBLE_ACI=2.0.0 

yes | pip uninstall ansible
pip install ansible==${VERSION_ANSIBLE}

ansible-galaxy collection install cisco.aci:==${VERSION_ANSIBLE_ACI} 

pip install openpyxl pandas paramiko
```