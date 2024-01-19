from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=225)
    phone = models.IntegerField()
    address = models.TextField()
    attachment = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.room_number} - {self.hotel.name}"

class Image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room}"
    
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    check_in_date = models.DateField()

    def __str__(self):
        return f"Reservation for {self.guest_name} - Room {self.room.room_number} at {self.room.hotel.name}"