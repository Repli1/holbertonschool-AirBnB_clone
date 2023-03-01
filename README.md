# Description

A console for testing that manipulates object instances and saves/loads them to/from a json file. It will help us in a future school project.


# Requirements

>Python language interpreter.

# Examples/Testing
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Creates a new instance of a class, saves it, and prints the id
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) create State
bb920463-bbd2-4d75-8b1d-a647a0245946
(hbnb) update State bb920463-bbd2-4d75-8b1d-a647a0245946 name Utah
(hbnb) create State
c897ecb9-a07a-448e-9771-8b32865750ea
(hbnb) update State c897ecb9-a07a-448e-9771-8b32865750ea name Ohio
(hbnb) create City
b732b73b-1874-4a43-9405-7700d017504b
(hbnb) update City b732b73b-1874-4a43-9405-7700d017504b name Portland
(hbnb) show State c897ecb9-a07a-448e-9771-8b32865750ea
[State] (c897ecb9-a07a-448e-9771-8b32865750ea) {'id': 'c897ecb9-a07a-448e-9771-8b32865750ea', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391576), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391590), 'name': 'Ohio'}
(hbnb) all State
["[State] (bb920463-bbd2-4d75-8b1d-a647a0245946) {'id': 'bb920463-bbd2-4d75-8b1d-a647a0245946', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269146), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269160), 'name': 'Utah'}", "[State] (c897ecb9-a07a-448e-9771-8b32865750ea) {'id': 'c897ecb9-a07a-448e-9771-8b32865750ea', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391576), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391590), 'name': 'Ohio'}"]
(hbnb) all
["[State] (bb920463-bbd2-4d75-8b1d-a647a0245946) {'id': 'bb920463-bbd2-4d75-8b1d-a647a0245946', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269146), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269160), 'name': 'Utah'}", "[State] (c897ecb9-a07a-448e-9771-8b32865750ea) {'id': 'c897ecb9-a07a-448e-9771-8b32865750ea', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391576), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 45, 391590), 'name': 'Ohio'}", "[City] (b732b73b-1874-4a43-9405-7700d017504b) {'id': 'b732b73b-1874-4a43-9405-7700d017504b', 'created_at': datetime.datetime(2023, 2, 28, 17, 18, 4, 230459), 'updated_at': datetime.datetime(2023, 2, 28, 17, 18, 4, 230472), 'name': 'Portland'}"]
(hbnb) destroy State c897ecb9-a07a-448e-9771-8b32865750ea
Object deleted
(hbnb) all
["[State] (bb920463-bbd2-4d75-8b1d-a647a0245946) {'id': 'bb920463-bbd2-4d75-8b1d-a647a0245946', 'created_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269146), 'updated_at': datetime.datetime(2023, 2, 28, 17, 17, 28, 269160), 'name': 'Utah'}", "[City] (b732b73b-1874-4a43-9405-7700d017504b) {'id': 'b732b73b-1874-4a43-9405-7700d017504b', 'created_at': datetime.datetime(2023, 2, 28, 17, 18, 4, 230459), 'updated_at': datetime.datetime(2023, 2, 28, 17, 18, 4, 230472), 'name': 'Portland'}"]
(hbnb) quit
$
```
