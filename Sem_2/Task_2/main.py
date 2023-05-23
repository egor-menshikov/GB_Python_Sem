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

# number = int(input())
#
# n1=0
# n2=1
# position=2
# while n2<number:
#     n1,n2 = n2, n1+n2
#     position+=1
# if n2!=number:
#     print("-1")
# else:
#     print(position)