# Task Manager CLI

## Description
A CLI tool to add, categorize, complete, and delete tasks. Data persists between sessions in a local JSON file.

## Requirements
Python 3.12.9

## Installation
`git clone https://github.com/fermx3/cli_task_manager && cd cli_task_manager`

## Usage
### Add a task
`python main.py add "Buy groceries" --category shopping`

### List tasks
`python main.py list`

### Mark task as completed
`python main.py complete xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### Delete task
`python main.py delete xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

## Output Example
```

[ ] Tarea 1
2026-04-03
id: 80fa69c4-c7f7-4cfa-8f49-e691d85b6c11

[X] Tarea 2
2026-04-03 · Main
id: 2bd9c459-76c1-43e3-b1fd-70f3ed7e147e

[ ] Tarea 3
2026-04-03
id: 270d215e-ffce-4e01-aa6c-a7d0d7e80b1f

[ ] Tarea 4
2026-04-03
id: 909724a7-d952-4af2-8cc6-6c1c9994285e

[ ] Tarea 5
2026-04-03
id: c0825e7d-9182-46f1-8da8-bc735f4b69a5

[ ] TEST
2026-04-05 · Shopping
id: c1ea072e-600d-4e35-9c5d-e12e66840a2e
```
