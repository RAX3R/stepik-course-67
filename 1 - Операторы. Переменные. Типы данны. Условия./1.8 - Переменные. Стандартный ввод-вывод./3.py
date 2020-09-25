x = int(input())
h = int(input())
m = int(input())

f = x + (h * 60) + m
hour = f // 60
minute = f % 60

print(hour)
print(minute)
