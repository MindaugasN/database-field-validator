# Introduction

We want to define classes that have fields that we want validated before we can set their value.

Objects will later be serialized into a database, and we need to ensure the data is valid before we write to the database.

## Implementation Part 1

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
|-- part_1
    |-- model
        |-- fields
            |-- char.py
            |-- integer.py
        |-- utils
            |-- validators.py
    |-- tests
        |-- unit
            |-- test_integer_field.py
|-- part_2
    |-- model
        |-- fields
            |-- char.py
            |-- integer.py
        |-- utils
            |-- validators.py
    |-- tests
        |-- unit
            |-- test_integer_field.py
|-- README.md
|-- .gitignore
```