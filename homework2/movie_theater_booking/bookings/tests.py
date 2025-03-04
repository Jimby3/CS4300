import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw2.settings")
django.setup()

from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking


from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking


class BookingAppTests(TestCase):
    def setUp(self):
        """Set up test data for all tests"""
        self.client = Client()
        self.api_client = APIClient()

        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create test movies
        self.movie1 = Movie.objects.create(title="Movie 1", description="Test movie", release_date="2023-01-01",
                                           duration=120)
        self.movie2 = Movie.objects.create(title="Movie 2", description="Another movie", release_date="2023-02-01",
                                           duration=110)

        # Create test seats
        self.seat1 = Seat.objects.create(seat_number="A1", is_booked=False)
        self.seat2 = Seat.objects.create(seat_number="A2", is_booked=False)

        # Create a booking for testing
        self.booking = Booking.objects.create(movie=self.movie1, seat=self.seat1, user=self.user)

    ### --- TESTING TEMPLATE VIEWS --- ###

    def test_movie_list_view(self):
        """Ensure movie list page loads properly"""
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/movie_list.html')
        self.assertContains(response, "Movie 1")  # Ensure test movie is displayed

    def test_book_seat_view(self):
        """Ensure seat booking page loads properly"""
        response = self.client.get(reverse('book_seat', args=[self.movie1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/seat_booking.html')

    def test_successful_seat_booking(self):
        """Ensure a user can book a seat"""
        self.client.login(username="testuser", password="testpass")  # Authenticate user
        response = self.client.post(reverse('book_seat', args=[self.movie1.id]), {'seat': self.seat2.id})

        # Check if seat is now booked
        self.seat2.refresh_from_db()
        self.assertTrue(self.seat2.is_booked)

        # Ensure user is redirected to booking history
        self.assertRedirects(response, reverse('booking_history'))

    def test_booking_history_view(self):
        """Ensure user's booking history page loads properly"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_history.html')
        self.assertContains(response, "Movie 1")  # Ensure booking history shows test booking

    ### --- TESTING API ENDPOINTS --- ###

    def test_api_get_movies(self):
        """Ensure API returns a list of movies"""
        response = self.api_client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two test movies

    def test_api_create_movie(self):
        """Ensure API can create a movie"""
        response = self.api_client.post("/api/movies/", {"title": "New Movie", "description": "A new test movie",
                                                         "release_date": "2023-03-01", "duration": 90}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)

    def test_api_get_seats(self):
        """Ensure API returns a list of seats"""
        response = self.api_client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # python
    def test_api_create_booking(self):
        """Ensure API can create a booking"""
        self.api_client.force_authenticate(user=self.user)  # Authenticate user
        response = self.api_client.post("/api/bookings/", {"movie": self.movie2.id, "seat": self.seat2.id},
                                        format="json")
        print(response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)  # One existing booking + new one

    def test_api_get_bookings(self):
        """Ensure API returns user's bookings"""
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One test booking exists

