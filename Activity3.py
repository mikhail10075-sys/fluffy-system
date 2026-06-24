weather = ('sunny','rainy','sunny','rainy','sunny','sunny','rainy')

sunny = 0
rainy = 0

for i in range(0,6):
    if (weather[i]) == 'sunny':
        sunny += 1
    else:
        rainy += 1

if sunny > rainy:
    print("Good weather!")
else:
    print("Bad weather.")