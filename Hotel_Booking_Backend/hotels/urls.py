from django.urls import path
from .views import HotelList, RoomList, ImageList, ReservationList, HotelListView

urlpatterns = [
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelListView.as_view(), name='hotel-view'),
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('images/', ImageList.as_view(), name='image-list'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
]
