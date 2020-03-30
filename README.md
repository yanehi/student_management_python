[![Build Status](https://travis-ci.com/yanehi/student_management_python.svg?branch=master)](https://travis-ci.com/yanehi/student_management_python)
[![Coverage Status](https://coveralls.io/repos/github/yanehi/student_management_python/badge.svg?branch=master)](https://coveralls.io/github/yanehi/student_management_python?branch=master)
# student_management_python
Simple student management project for practice programming with Python. You can list, add, remove and edit students. The data persistence is realized with read/write of csv files. 

The student objects with its attributes are structured as tuples in a list.

```bash
students = [(firstname, lastname, ...),(firstname, lastname, ...), ...]
```

On startup the programm reads the students from a `.csv` file and import them as tuples in a list. When you close the programm, the actual state of the student list will be written to the same `.csv` file.

## Prerequisites

### Python

* Install python

* Install packages
```bash
pip3 install -r requirements.txt
```

* Start project
```bash
python3 setup.py
```

* Run your tests
```bash
python3 -m unittest tests.test_calc -v
```


## Tools
* [Python3](https://www.python.org/)
* [pip3](https://pypi.org/project/pip/)

## Authors
* **Yannic Nevado** - *Initial work* - [Github](https://github.com/yanehi)
