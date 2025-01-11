
# 1)
import os
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "my_file.txt"
file_path = os.path.join(desktop_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a simple example of writing and reading a file.")

with open(file_path, "r") as file:
    print(file.read())


# 2)
import csv
import random
import pandas as pd

file_name = "simple_data.csv"
headers = ["ID", "Name", "Age", "Score"]
names = ["Kalyan", "Rahul", "Naveen", "Rakesh", "Mohan"]
with open(file_name, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for i in range(1, len(names)):
        writer.writerow([i, random.choice(names), random.randint(18,40), round(random.uniform(50, 100), 2)])
print(f"CSV file '{file_name}' created successfully.\n")
with open(file_name, "r") as file:
    print(file.read())
data = pd.read_csv(file_name)
data["Pass/Fail"] = data["Score"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(data)
data.to_csv("transformed_data.csv", index=False)









