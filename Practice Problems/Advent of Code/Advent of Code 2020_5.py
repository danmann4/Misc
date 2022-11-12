# Part 1:
with open('2020 inputs/Day 5.txt') as f:
    db = f.read().split()
# Just convert to binary and solve.
Seats= [a.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0') for a in db]
seat_val = int()
seat_list = list()
for seat in Seats:
    # First 7 characters are the row.
    row = int(seat[:7], 2)
    seat_val = row * 8
    # Last characters are the seat.
    col = int(seat[7:],2)
    seat_val += col
    seat_list.append(seat_val)
seat_list.sort()
print(seat_list[-1])

# Part 2:
for b in range(seat_list[0], seat_list[-1] + 1):
    if b not in seat_list:
        my_seat = b
        break
print(my_seat)

