
distance = int(input("Enter the distance of the trip in miles: "))

speed = int(input("Enter the average speed in miles per hour: "))

hours = distance // speed
minutes = distance % speed * 60 // speed

print(f"Estimated travel time: {hours} hours and {minutes} minutes")
