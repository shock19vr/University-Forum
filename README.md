# University Forum

A basic web application built with Flask for university students to access information and services.

## About This Project

This was our first web development project, so the code quality reflects beginner-level programming. The application provides a simple interface for university students with basic authentication and information display.

## Features

- **User Authentication**: Login and registration system using CSV files for data storage
- **Home Page**: Displays university events and blog posts
- **Navigation Pages**: 
  - Announcements
  - Communities  
  - Academics
  - Maps
  - Help/Contact form
- **User Profile**: View registered user details
- **Help System**: Contact form that saves queries to CSV

## Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS
- **Data Storage**: CSV files (accounts.csv, details.csv, questions.csv)
- **Authentication**: Basic session management with global token variable

## Project Structure

```
University-Forum/
├── main.py                 # Application entry point
├── website/                # Main application package
│   ├── __init__.py        # Flask app factory
│   ├── auth.py            # Authentication routes
│   ├── views.py           # Main application routes
│   ├── templates/         # HTML templates
│   └── static/            # CSS, images, and other static files
├── accounts.csv           # User login credentials
├── details.csv            # User profile information
└── questions.csv          # Help form submissions
```

## Installation & Setup

1. Clone the repository
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Open your browser and go to `http://localhost:5000`

## Known Issues & Limitations

- **Security**: Passwords are stored in plain text in CSV files
- **Data Storage**: Uses CSV files instead of a proper database
- **Authentication**: Basic implementation with global variables
- **Validation**: Limited input validation
- **Error Handling**: Minimal error handling throughout the application
- **Code Quality**: Inconsistent formatting and basic structure

## Usage

1. Register with a university email and enrollment number (must contain "mitu")
2. Login with your credentials
3. Navigate through different sections using the navigation bar
4. Use the help page to submit questions or feedback

## Future Improvements

- Implement proper database (SQLite/PostgreSQL)
- Add password hashing and secure authentication
- Improve error handling and input validation
- Add proper session management
- Enhance UI/UX design
- Add more interactive features

## Note

This project was created as a learning exercise. The code contains several security vulnerabilities and design issues that would need to be addressed before any production use.
