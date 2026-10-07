destination = input("Enter destination: ")
distance = float(input("Enter distance in km: "))
speed = float(input("Enter average speed in km/h: "))

time = distance / speed

print("Destination:", destination)
print("Distance:", distance, "km")
print("Average Speed:", speed, "km/h")
print("Estimated Travel Time:", time, "hours")