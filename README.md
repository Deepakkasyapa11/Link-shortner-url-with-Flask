# link-shortner

Description: A simple Python Flask application that creates short and memorable URLs for long links, making sharing and accessing them easier. It's easy to install, customize, and deploy.<br>

# Flask Python Project

This repository contains a Python project built using the Flask framework. It showcases how to create a web application using Flask and utilizes the Flask-WTF extension for form handling.

## Requirements

- Python 3.x
- Flask
- Flask-WTF

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/shivamverma26/link-shortner.git
   ```

2. Navigate to the project directory:

   ```shell
   cd link-shortner
   ```

3. Install the required module using `pip`:

   ```shell
   pip install flask
   pip install flask-wtf
   ```

   This will install Flask and Flask-WTF.

## Usage

1. Start the Flask development server:

   ```shell
   python app.py
   ```

2. Open a web browser and visit `http://localhost:5000` to access the application.

## Project Structure

The project has the following structure:

```
flask-python-project/
   ├── app.py
   ├── forms.py
   ├── templates/
   │   ├── base.html
   │   └── index.html
   └── README.md
```

- `app.py`: The main Flask application file.
- `forms.py`: Contains the Flask-WTF form definition.
- `templates/`: Directory containing HTML templates.
  - `base.html`: Base template file with common HTML structure.
  - `index.html`: Home page template file.
- `README.md`: This file, providing information about the project.



