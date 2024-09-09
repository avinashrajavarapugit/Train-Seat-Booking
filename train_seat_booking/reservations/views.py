from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Seat

from django.http import JsonResponse
from .models import Seat

# Endpoint to get seat status
def get_seat_status(request):
    seats = list(Seat.objects.all().values('id', 'row', 'is_reserved'))
    return JsonResponse({'seats': seats})

# Endpoint to reserve seats
def reserve_seats(request):
    if request.method == 'POST':
        num_seats = int(request.POST.get('num_seats'))
        if num_seats > 7:
            return JsonResponse({'message': 'Cannot reserve more than 7 seats at once'}, status=400)

        reserved_seats = []
        # Try to find seats in a single row or nearby
        for row in range(1, 12):  # Rows 1-11 have 7 seats, row 12 has 3 seats
            available_seats = Seat.objects.filter(row=row, is_reserved=False)[:num_seats]
            if available_seats:
                for seat in available_seats:
                    seat.is_reserved = True
                    seat.save()
                    reserved_seats.append(seat.id)
                return JsonResponse({
                    'message': f'Reserved {num_seats} seats in row {row}',
                    'reservedSeats': reserved_seats
                })

        return JsonResponse({'message': 'Not enough seats available'}, status=400)


def home(request):
    return JsonResponse({'message': 'Welcome to the reservations page!'})

