n = int(input())
reservation = set()
for _ in range(n):
    reservation_number = input()
    reservation.add(reservation_number)

guest = input()
while guest != "END":
    reservation.remove(guest)
    guest = input()

print(len(reservation))
for num in sorted(reservation):
    print(num)