import csv
import time
import random
import os

file_name = "factory_stream.csv"

machines = ["M1", "M2", "M3", "M4"]

if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "machine_id",
            "energy_usage",
            "temperature",
            "carbon_emission",
            "production_load"
        ])

while True:
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)

        machine = random.choice(machines)
        energy = random.randint(80, 180)
        temp = random.randint(50, 100)
        carbon = random.randint(20, 90)
        load = random.randint(60, 100)

        writer.writerow([machine, energy, temp, carbon, load])

    print("New data added...")
    time.sleep(2)
