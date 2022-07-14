# Lab1 - Access Policy 작업

#### Case 1

- Task 확인

```
ansible-playbook access_policy.yml --list-tasks
```

#### Case 2

- 설정별 task 확인

```
ansible-playbook access_policy.yml --list-tasks --tags vlan_pool
ansible-playbook access_policy.yml --list-tasks --tags domain
ansible-playbook access_policy.yml --list-tasks --tags policy_group
ansible-playbook access_policy.yml --list-tasks --tags interface_profile
ansible-playbook access_policy.yml --list-tasks --tags interface_profile,policy_cdp
```

#### Case 3

- Access Policy 작업 수행 전, vlan pool, domain 작업에 대한 Dry-Run 수행

```
ansible-playbook access_policy.yml --tags vlan_pool --check
ansible-playbook access_policy.yml --tags domain --check
```

- Vlan Pool 작업 수행

```
ansible-playbook access_policy.yml --tags vlan_pool
#ansible-playbook access_policy.yml --tags vlan_pool --check
```

- Access Policy 작업 Dry-Run 및 작업 수행

```
ansible-playbook access_policy.yml --check
ansible-playbook access_policy.yml
```