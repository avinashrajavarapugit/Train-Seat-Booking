seats = [
    [0] * 7 for _ in range(11)
] + [[0] * 3] 


def available_seats(seats):
    return sum(row.count(0) for row in seats)

def display_seats(seats):
    for row_index, row in enumerate(seats):
        print(f"Row {row_index + 1}: {' '.join(map(str, row))}")


def reserve_seats(seats, num_seats):
    if num_seats > 7:
        print("You cannot book more than 7 seats at a time.")
        return False

    # Try to find a single row with enough consecutive seats
    for row_index, row in enumerate(seats):
        available_seats = row.count(0)
        if available_seats >= num_seats:
            # Book the seats in this row
            for i in range(num_seats):
                row[row.index(0)] = 1
            print(f"Seats reserved in row {row_index + 1}")
            return True

    # If no single row has enough seats, book nearby seats
    seats_booked = 0
    for row_index, row in enumerate(seats):
        for seat_index in range(len(row)):
            if row[seat_index] == 0 and seats_booked < num_seats:
                row[seat_index] = 1
                seats_booked += 1
        if seats_booked == num_seats:
            break

    if seats_booked == num_seats:
        print(f"Seats reserved across multiple rows.")
        return True

    print("Not enough seats available.")
    return False

def booking_system():
    seats = [
        [0] * 7 for _ in range(11)
    ] + [[0] * 3]

    while available_seats(seats) > 0:
        display_seats(seats)
        num_seats = int(input("Enter the number of seats to reserve (1-7): "))
        if not reserve_seats(seats, num_seats):
            break

    print("All seats are booked!")
