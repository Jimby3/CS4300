# Movie Theater Booking System

This project is a Django-based web application for booking movie theater seats. It includes both a web interface and a RESTful API for managing movies, seats, and bookings.

In full disclosure, this application was heavily influenced by AI chats I had with github co-pilot and chatGPT. It helped speedup the development process and I was able to learn a lot from the AI.

## Features

- User authentication
- Movie listing and details
- Seat booking
- Booking history
- RESTful API for movies, seats, and bookings

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST framework

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/movie-theater-booking.git
    cd movie-theater-booking
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test