# python operators 
# keywords and and or let you combine multiple comparisons 
# not lets you negate a comparison 

# reminders: primitive data types include:
# int, float, string, boolean

temperature = 55

if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

# or operator 
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print('Enjoy the outdoors!')

# and operator 
forecast = "sunny"

if temperature < 80 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")

# not operator 
forecast = "rainy"

if not forecast == "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

# evaluating boolean variables
raining = True

if not raining:
    print("Go outside!")
else:
    print("Stay inside!")