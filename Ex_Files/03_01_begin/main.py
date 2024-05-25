import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    # print(reader)
    # print(type(reader))
    # laureates = list(reader)
    laureates = reader
    # print(laureates[:2])
    for laureate in laureates:
        if laureate["surname"] == "Einstein":
            pprint(laureate)
            break
