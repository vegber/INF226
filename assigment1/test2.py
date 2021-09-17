g = float(9.8)
t = int(0)
h = int(input('Stenen droppes fra hÃ¸yde: '))
p = 1

while p > 0:
    p = float(h - ((1 / 2) * g * t))
    print(f'{p:.1f} m')
    t += 1.0

print(f'Stenen lander mellom {(t - 1):.1f} og {t:.1f} sekunder etter at den droppes.')
