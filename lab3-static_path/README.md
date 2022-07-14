# Lab3 - Static Port 작업

#### Case 1

- Task 확인

```
ansible-playbook static_port.yml --list-tasks
```

#### Case 2

- Static Port 작업 수행

```
ansible-playbook static_port.yml
```

#### Case 3 

- GUI에서 EPG 1개를 삭제 후, Static Port 작업 다시 수행

```
ansible-playbook static_port.yml
```