# 哈开 - Hackathon Website

A Django-based website for the "哈开" (Hakai) Olympiads in Software Development.

## Features

- Modern, responsive design
- Chinese character branding
- Sponsor section
- FAQ section
- News updates
- Event information
- Photo gallery integration

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- PostgreSQL (optional, for production)

### Installation

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd /path/to/hackathon-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   
   **Option A: SQLite (Development)**
   ```bash
   python manage.py migrate
   ```
   
   **Option B: PostgreSQL (Production)**
   - Install PostgreSQL on your system
   - Create a database named `hakai_db`
   - Set environment variables or create a `.env` file:
     ```
     DB_NAME=hakai_db
     DB_USER=your_postgres_user
     DB_PASSWORD=your_postgres_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

4. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The website will be available at `http://localhost:8000`

## Project Structure

```
hackathon-website/
├── hakai_website/          # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Main configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── main/                  # Main Django app
│   ├── migrations/        # Database migrations
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL patterns
│   └── admin.py           # Admin configuration
├── templates/             # HTML templates
│   ├── main.html          # Home page
│   ├── events.html        # Events page
│   ├── photos.html        # Photos page
│   └── ml-crush-details.html
├── static/               # Static files
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   └── images/           # Image assets
├── requirements.txt      # Python dependencies
└── manage.py            # Django management script
```

## Environment Variables

Create a `.env` file in the project root for environment-specific settings:

```env
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True

# PostgreSQL Database Configuration (optional)
DB_NAME=hakai_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Database Configuration

The project supports both SQLite and PostgreSQL:

- **SQLite**: Used by default for development. No additional setup required.
- **PostgreSQL**: Configure using environment variables for production use.

To switch to PostgreSQL, set the `DB_NAME` environment variable. The application will automatically detect this and use PostgreSQL instead of SQLite.

## Static Files

Static files (CSS, JavaScript, images) are served using Django's `collectstatic` command and WhiteNoise middleware for production deployment.

## Development

To add new pages:

1. Create a new view in `main/views.py`
2. Add a URL pattern in `main/urls.py`
3. Create a template in the `templates/` directory

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in your environment
2. Configure PostgreSQL database
3. Set up a proper web server (nginx + gunicorn)
4. Use environment variables for sensitive settings
5. Run `python manage.py collectstatic` to collect static files

## Dependencies

- Django 4.2+
- psycopg2-binary (PostgreSQL adapter)
- python-decouple (environment variable management)
- Pillow (image handling)
- whitenoise (static file serving)
- gunicorn (WSGI server)
- django-cors-headers (CORS handling)

## License

© 2025 Made by hakai team
