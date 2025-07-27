# EC2 Instance Manager (Python OOP Simulation)

This project simulates AWS EC2 instance lifecycle operations using advanced Python Object-Oriented Programming (OOP) principles. It is designed for developers aiming to strengthen their OOP design skills with a DevOps/Cloud focus.

---

## Features

- Create multiple EC2 instances with unique names and types.
- Start, stop, and terminate simulated EC2 instances.
- List all active (non-terminated) instances.
- Enforce lifecycle rules (e.g., cannot change instance type while running).
- Encapsulated internal states and validation logic.
- Demonstrates all key OOP concepts used in production systems.

---

## OOP Concepts Covered

| Concept         | Where It’s Applied                                        |
|------------------|----------------------------------------------------------|
| Abstraction      | `CloudResource` abstract base class                      |
| Inheritance      | `EC2Instance` inherits from `CloudResource`              |
| Encapsulation    | Private attributes like `__state`, `__instance_type`     |
| Polymorphism     | Different behavior for `start`, `stop`, `terminate`      |
| Composition      | `EC2Manager` maintains a collection of `EC2Instance`s    |
| Dunder Methods   | `__str__`, `__repr__` for friendly object printing       |
| Static Method    | `help()` function in `EC2Manager`                        |
| Class Method     | (To be added in next version for factory patterns)       |
| Exception Handling | Runtime and ValueError exceptions for invalid actions |

---

## Getting Started

### Requirements
- Python 3.7+
- No external libraries required

### Run the Script

```bash
python ec2_manager.py
------------------
# 🪣 S3 Bucket Simulator (Python OOP)

A Python-based simulation of AWS S3 bucket operations using advanced Object-Oriented Programming (OOP) principles. This project is ideal for showcasing your OOP skills in a cloud-focused, DevOps-style use case.

---

## 📌 Features

- Create multiple simulated S3 buckets with names and regions
- Upload, list, and delete files within each bucket
- Retrieve file content
- Simulate file versioning timestamps
- Validate file names on upload
- Manage multiple buckets from a central manager
- Helpful console output simulates real-world cloud behavior

---

## 🧠 OOP Concepts Demonstrated

| OOP Principle     | Where It's Used                                         |
|------------------|----------------------------------------------------------|
| Abstraction       | `CloudStorage` defines an abstract base for buckets     |
| Inheritance       | `S3Bucket` inherits from `CloudStorage`                 |
| Encapsulation     | Private file storage with `__files` dictionary          |
| Polymorphism      | Overridden `upload`, `delete`, `list_files` methods     |
| Composition       | `S3Manager` maintains and operates on bucket instances  |
| Static Method     | `validate_file_name()` to check file naming convention  |
| Class Method      | `from_config()` to instantiate a bucket from config     |
| Dunder Methods    | `__str__` and `__repr__` for object readability         |
| Exception Handling| Raised for invalid actions and missing files            |

---

## 🏗️ File Structure
# S3 Bucket Simulator (Python OOP Project)

This project simulates core AWS S3 bucket operations using advanced Python object-oriented programming (OOP) principles. It is designed to demonstrate OOP patterns in a DevOps/Cloud engineering context.

## Features

- Create S3-like buckets with unique names and regions
- Upload files with content to simulated buckets
- Delete files from buckets
- List files stored in a bucket
- List all active buckets
- Retrieve bucket and file metadata
- Enforce filename validation
- Demonstrates a clean separation of concerns with OOP design

## OOP Concepts Covered

| Concept           | Usage                                                        |
|-------------------|--------------------------------------------------------------|
| Abstraction        | `CloudStorage` defines an abstract base class               |
| Inheritance        | `S3Bucket` extends `CloudStorage`                            |
| Encapsulation      | Private attributes like `__files` and `__region`            |
| Polymorphism       | `upload`, `delete`, and `list_files` overridden in subclass |
| Composition        | `S3Manager` manages multiple `S3Bucket` instances           |
| Static Methods     | File name validation logic                                  |
| Class Methods      | Bucket creation from configuration dictionaries             |
| Exception Handling | Handles invalid operations and missing files gracefully     |

## File Structure
