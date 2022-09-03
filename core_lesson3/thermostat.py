too_hot = "Too hot"
too_cold = "Too cold"
just_nice = "Just nice"

lowerbound = 20
upperbound = 22

temperature = float(input("Please enter temperature: "))

if temperature < lowerbound:
    print("{}\nNew temperature: {}".format(too_cold, temperature + 1))
elif temperature > upperbound:
    print("{}\nNew temperature: {}".format(too_hot, temperature - 1))
else:
    print("{}\nNew temperature: {}".format(just_nice, temperature))
