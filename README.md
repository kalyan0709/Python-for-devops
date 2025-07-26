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
