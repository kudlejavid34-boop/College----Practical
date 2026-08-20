import csv
data=[
    {"name": "firoz", "age":25,"city":"mumbai"},
    {"name": "adnan", "age":22,"city":"pune"},
    {"name": "kaif", "age": 27, "city":"solapur"},
    {"name": "shahid", "age":20, "city": "solapur"},
]
with open("student.csv", "w", newline="") as file:
    writer=csv.DictWriter (file, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows (data)
    print("done")
