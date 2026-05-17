# To convert degrees Fahrenheit (°F) to degrees Celsius (°C), use this formula:
# °C= 5* (°F−32) /9​






def temperature():
    temp = int(input("Enter temperature in F: "))
    c = 5 * (temp -32) / 9
    print(c)

temperature()