num = int(input('Введите число:\n'))

prev = 0
next = 1
count = 3
current = prev + next

while current < num:
    prev = next
    next = current
    current = prev + next
    count += 1

if num == current:
    print(count)
else:
    print(-1)

