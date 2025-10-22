import pandas as pd

sample = pd.read_csv(r"C:\Users\YOUR_USERNAME\OneDrive\Desktop\python practice\sample csv.csv")

print("IN CASE OF IMPUTATION:")
print(sample.Calories.fillna(sample.Calories.mean()))

print("IN CASE OF ORDINAL ENCODING:")
data = pd.DataFrame({"colours": ["Red", "Yellow", "Blue", "Black", "Red", "Red", "Blue"]})
ordinal_map = {
    "Red": 11,
    "Yellow": 22,
    "Blue": 33,
    "Black": 44
}
data["encoding"] = data["colours"].replace(ordinal_map)
print(data)

print("IN CASE OF ONE HOT ENCODING:")
Red_column = {"Red": 1, "Yellow": 0, "Blue": 0, "Black": 0}
Yellow_column = {"Red": 0, "Yellow": 1, "Blue": 0, "Black": 0}
Blue_column = {"Red": 0, "Yellow": 0, "Blue": 1, "Black": 0}
Black_column = {"Red": 0, "Yellow": 0, "Blue": 0, "Black": 1}

data["red OH encoding"] = data["colours"].replace(Red_column)
data["yellow OH encoding"] = data["colours"].replace(Yellow_column)
data["blue OH encoding"] = data["colours"].replace(Blue_column)
data["black OH encoding"] = data["colours"].replace(Black_column)

del data["encoding"]
print(data)
