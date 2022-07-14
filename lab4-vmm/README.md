# Lab4 - Virtual Networking 작업

#### Case 1

- Task 확인

```
ansible-playbook vmm.yml --list-tasks
```

#### Case 2

- Dry-Run 및 작업 수행

```
ansible-playbook vmm.yml --check
ansible-playbook vmm.yml 
```

- ModuleNotFoundError: No module named 'pyVim' 에러 발생 시,

```
pip install pyvmomi
```