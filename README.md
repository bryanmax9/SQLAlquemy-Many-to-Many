# Many-to-Many Relationship: Sections and Students

This project demonstrates the implementation of a many-to-many relationship between `Sections` and `Students` classes using a junction class named `Enrollments`. The project is an extension of a previous one-to-many relationship project between `Course` and `Sections`. It uses SQLAlchemy and psycopg2 for the implementation.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Video](#video)


## Overview

This project is designed to showcase the following features:

- Creating a many-to-many relationship between `Sections` and `Students`
- Using a junction class `Enrollments` with foreign keys for student ID and section ID
- Adding a surrogate key `enrollment_id` in the `Enrollments` class
- Implementing functionality to add sections to students and students to sections

## Prerequisites

- Python 3.x
- SQLAlchemy
- psycopg2

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

2. Install SQLAlchemy and psycopg2 using pip:

```bash
pip install SQLAlchemy psycopg2
```
## Getting Started

To use this code, you will need to have PostgreSQL installed on your machine and create a database called "course_db". You will also need to install the psycopg2 and SQLAlchemy libraries by running `pip install psycopg2 sqlalchemy` in your command prompt.

Once you have these prerequisites, you can clone this repository and run the `main.py` file to start using the Section model and its functions.

## Contributors

This project was created by Bryan tineo and Zavier Carr for a Database Fundamentals class. Feel free to use it and modify it as needed for your own projects.

If you have any questions or suggestions, you can contact us https://www.linkedin.com/in/bryan-tineo/.

1. Clone the repository:
git clone git@github.com:bryanmax9/SQLAlquemy-Many-to-Many.git

1.Navigate to the project directory:
cd SQLAlquemy-Many-to-Many

## Usage

Thisproject can only be runon the School server ONLY, sorry.

## Examples

![Department Data](https://i.imgur.com/ydpPWYJ.jpeg)

![Enrollment Data](https://i.imgur.com/ydpPWYJ.jpeg)

![Major Data](https://i.imgur.com/8pfgPXx.jpeg)

![Section Data](https://i.imgur.com/NlcUHyF.jpeg)


## Video

https://user-images.githubusercontent.com/69496341/227456539-c55225b0-3013-4ace-80e0-a1fbd9bacd6e.mp4


