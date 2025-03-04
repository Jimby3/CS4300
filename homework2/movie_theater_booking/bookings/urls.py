from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history

# Set up the API router
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [

    # Redirect '/' to '/movies/'
    path('', RedirectView.as_view(url='/movies/', permanent=False)),

    # API Endpoints (now prefixed with /api/)
    path('api/', include(router.urls)),

    # Template Views
    path('movies/', movie_list, name='movie_list'),
    path('book/<int:movie_id>/', book_seat, name='book_seat'),
    path('history/', booking_history, name='booking_history'),
]
