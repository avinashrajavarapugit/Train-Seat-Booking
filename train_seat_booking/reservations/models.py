from django.db import models

class Seat(models.Model):
    row = models.IntegerField()
    seat_number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Row {self.row}, Seat {self.seat_number}'

