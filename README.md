# Task Management System

A command-line task management application built with Python.

## Setup

### Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Run the Application
```bash
python main.py
```

## Project Structure
- `main.py` - Main application entry point
- `task_utils.py` - Task management functions (add, complete, view, progress)
- `validation.py` - Input validation functions
- `requirements.txt` - Project dependencies (none required)
- `venv/` - Python virtual environment

## Features
- Add new tasks with title, description, and due date
- Mark tasks as complete
- View pending tasks
- Calculate and display progress percentage

## Requirements
- Python 3.6+
- No external dependencies (uses only standard library)
