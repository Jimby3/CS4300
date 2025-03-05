# File: homework2/movie_theater_booking/bookings/urls.py
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history, RegisterView
from django.contrib.auth import views as auth_views

# Set up the API router
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)


class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        return reverse_lazy('movie_list')


urlpatterns = [
    # Redirect '/' to '/movies/'
    path('', RedirectView.as_view(url='/movies/', permanent=False)),

    # API Endpoints (now prefixed with /api/)
    path('api/', include(router.urls)),

    # Template Views
    path('login/', CustomLoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bookings/logout.html', next_page='login'),
         name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('movies/', movie_list, name='movie_list'),
    path('book/<int:movie_id>/', book_seat, name='book_seat'),
    path('history/', booking_history, name='booking_history'),
]
