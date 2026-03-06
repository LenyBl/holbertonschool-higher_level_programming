# Holberton School - Higher Level Programming

This repository contains projects completed as part of the Holberton School curriculum, covering higher-level programming in **Python** and **SQL**. The projects progress from basic scripting to object-oriented programming, databases, REST APIs, and security.

---

## Table of Contents

- [Python Projects](#python-projects)
- [SQL Projects](#sql-projects)
- [Requirements](#requirements)
- [Author](#author)

---

## Python Projects

### [python-hello_world](./python-hello_world)

Introduction to Python syntax. Covers the `print()` function, f-strings, string repetition, slicing, and concatenation.

**Concepts:** `print()`, f-strings, string indexing and slicing

---

### [python-if_else_loops_functions](./python-if_else_loops_functions)

Control flow and basic functions. Includes FizzBuzz, alphabet printing, digit manipulation, and arithmetic functions.

**Concepts:** `if/elif/else`, `for`/`while` loops, function definitions

---

### [python-import_modules](./python-import_modules)

Working with Python modules. Demonstrates importing from custom and standard library modules, and using command-line arguments.

**Concepts:** `import`, `__import__`, `sys.argv`, module structure

---

### [python-data_structures](./python-data_structures)

Operations on Python lists and tuples. Covers element access, replacement, searching, matrix printing, and variable swapping.

**Concepts:** lists, tuples, indexing, matrix iteration

---

### [python-more_data_structures](./python-more_data_structures)

Sets, dictionaries, and functional programming tools. Includes set operations, dictionary management, and use of `map` with lambdas.

**Concepts:** sets, dictionaries, `map()`, lambdas, comprehensions

---

### [python-exceptions](./python-exceptions)

Safe programming with exception handling. Exercises cover catching `IndexError`, `TypeError`, `ZeroDivisionError`, and raising custom exceptions.

**Concepts:** `try/except/finally`, `raise`, defensive coding

---

### [python-classes](./python-classes)

OOP fundamentals through the progressive implementation of a `Square` class. Introduces private attributes, validation, and properties.

**Concepts:** classes, private attributes, getters/setters (`@property`), data validation

---

### [python-more_classes](./python-more_classes)

Advanced OOP with a `Rectangle` class. Adds magic methods, class attributes, static methods, and class methods.

**Concepts:** `__str__`, `__repr__`, `__del__`, `@staticmethod`, `@classmethod`, class attributes

---

### [python-test_driven_development](./python-test_driven_development)

Writing tests before implementation using Python's `doctest` and `unittest` frameworks. Each function is paired with a test file covering edge cases.

**Concepts:** TDD, `doctest`, `unittest.TestCase`, edge cases

---

### [python-inheritance](./python-inheritance)

Class inheritance from `BaseGeometry` → `Rectangle` → `Square`. Covers `isinstance`, `issubclass`, method overriding, and `super()`.

**Concepts:** inheritance, `super()`, `isinstance()`, `issubclass()`, polymorphism, MRO

---

### [python-input_output](./python-input_output)

File I/O and JSON serialization. Includes reading/writing files, converting objects to/from JSON, and generating Pascal's triangle.

**Concepts:** `open()`, `with`, `json.dumps/loads`, `json.dump/load`, file modes

---

### [python-serialization](./python-serialization)

Comparison of four serialization formats: JSON, Pickle, CSV-to-JSON conversion, and XML.

**Concepts:** `json`, `pickle`, `csv`, `xml.etree.ElementTree`

---

### [python-abc](./python-abc)

Abstract Base Classes, duck typing, mixins, and multiple inheritance. Covers ABCs, custom iterators, MRO, and mixin composition.

**Concepts:** `abc.ABC`, `@abstractmethod`, duck typing, mixins, multiple inheritance, MRO

---

### [python-object_relational_mapping](./python-object_relational_mapping)

ORM integration between Python and MySQL using MySQLdb and SQLAlchemy.

**Concepts:** MySQLdb, SQLAlchemy, ORM models, database sessions

---

### [restful-api](./restful-api)

Progressive REST API development from a raw HTTP server to a secured Flask application with JWT and Basic Auth.

| Task | Description |
|---|---|
| `task_02_requests.py` | Fetches and saves posts using the `requests` library |
| `task_03_http_server.py` | Minimal HTTP API with `http.server` |
| `task_04_flask.py` | Full Flask CRUD API with JSON responses |
| `task_05_basic_security.py` | Flask API secured with Basic Auth and JWT tokens |

**Concepts:** `requests`, `http.server`, Flask, REST, JSON, HTTP Basic Auth, JWT, role-based access

---

## SQL Projects

### [SQL_introduction](./SQL_introduction)

Foundational SQL: database and table management, inserting and querying data, filtering, ordering, updating, and aggregating.

**Concepts:** `CREATE`, `DROP`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`, `ORDER BY`, `GROUP BY`, `COUNT`, `AVG`

---

### [SQL_more_queries](./SQL_more_queries)

Advanced SQL: user privileges, table constraints, subqueries, and multi-table joins using a TV show database schema.

**Tables used:** `tv_shows`, `tv_genres`, `tv_show_genres`

**Concepts:** `GRANT`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `FOREIGN KEY`, `INNER JOIN`, `LEFT JOIN`, subqueries

---

## Requirements

### Python

- Python 3.8+
- PEP 8 / pycodestyle compliant
- All scripts are executable

### SQL

- MySQL 8.0
- All queries end with a semicolon
- Keywords are uppercase

---

## Author

Holberton School student project — Higher Level Programming track.
