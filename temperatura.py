temp_celsius = 22.5, 40, 13, 29, 34
temp_fahrenheit = list(map(lambda temp: round((9/5) * temp + 32, 1), temp_celsius))
print(f"\nAs temperaturas 22.5°C, 40°C, 13°C, 29°C, 34°C são iguais a {temp_fahrenheit} em Fahrenheit.")