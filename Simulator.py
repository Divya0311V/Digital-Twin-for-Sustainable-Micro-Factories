import time
import random

machines = ["M1", "M2", "M3"]

while True:
    for machine in machines:
        load = random.randint(50, 100)
        power = load * 0.08 + random.uniform(-0.5, 0.5)
        temperature = random.randint(60, 90)
        vibration = random.uniform(0.1, 1.0)
        carbon = power * 0.4

        print(f"{machine}, {temperature}, {vibration:.2f}, {power:.2f}, {load}, {carbon:.2f}")

    time.sleep(1)
