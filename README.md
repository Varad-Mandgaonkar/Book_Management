# Django Book Management System

A simple Book Management System built using **Django**. This project allows users to manage a collection of books with functionalities for **Create**, **Read**, **Update**, and **Delete** (CRUD operations). The system is designed to be easy to use and provides a simple interface for managing book data.

## Features

- **Book CRUD Operations**: Add, view, update, and delete books.
- **Bootstrap-based UI**: Responsive and visually appealing user interface.
- **Django Admin Integration**: Admin interface to manage books.
- **Database Integration**: SQLite (or PostgreSQL for production).

## Prerequisites

- **Python** (version 3.8 or later)
- **Django** (version 3.0 or later)
- **Git** (for version control)
- **pip** (for installing dependencies)

## Installation

Follow these steps to get your development environment set up.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Varad-Mandgaonkar/Django_Project.git
   cd Django_Project

2.**Create and activate a virtual environment**:

For Windows:
bash
python -m venv venv
venv\Scripts\activate

3.**Install dependencies**:

bash
pip install -r requirements.txt

4.**Migrate the database (create tables for models)**:

bash

python manage.py migrate

5.**Create a superuser (admin access for the Django admin panel)**:

bash

python manage.py createsuperuser

6.**Run the server**:

bash

python manage.py runserver

