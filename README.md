# Introduction

We want to define classes that have fields that we want validated before we can set their value.

Objects will later be serialized into a database, and we need to ensure the data is valid before we write to the database.

### IntegerField

* [x] Only allows integral numbers;
* [x] Has minimum value;
* [x] Has maximum value;

### CharField

* [x] Only allows strings;
* [x] Has minimum length;
* [x] Has maximum length;

## Expected usage

```python
class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)
```

## Project structure

```
project
|-- model
    |-- __init__.py
    |-- base.py
    |-- fields
        |-- char.py
        |-- integer.py    
|-- tests
    |-- __init__.py
    |-- unit
        |-- test_integer_field.py
        |-- test_char_field.py
|-- README.md
|-- .gitignore
```

## Running tests

```bash
python -m unittest tests.unit.test_integer_field -v
python -m unittest tests.unit.test_char_field -v
```