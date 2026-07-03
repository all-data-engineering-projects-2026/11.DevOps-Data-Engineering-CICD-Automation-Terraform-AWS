import csv

import os
import random
from datetime import datetime, timedelta


def generate_temperature_csv(filename, num_records=10000):
    if num_records < 0:
        raise ValueError('num_records must be a positive')

    cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
    header = ["City", "Temperature", "timestamp"]

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for _ in range(num_records):
                city = random.choice(cities)
                temperature = round(random.uniform(10, 35), 1)
                timestamp = datetime.now() - timedelta(days=random.randint(0, 365))

                writer.writerow([city, temperature, timestamp])
    except (OSError, IOError) as e:
        raise IOError(f"Failed to create temperature csv file: {str(e)}")


if __name__ == "__main__":
    generate_temperature_csv("data/temperature_data.csv")
