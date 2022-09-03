c_temperatures = [7, 50, 12, 22, 30]

f_temperatures = list(map(lambda temp: temp * 1.8 + 32, c_temperatures))

assert f_temperatures == [44.6, 122.0, 53.6, 71.6, 86.0]
