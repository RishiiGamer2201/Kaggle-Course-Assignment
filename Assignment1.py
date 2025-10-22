import pandas as pd

sample = pd.read_csv(r"C:\Users\acer\Downloads\sample.csv")

print("IN CASE OF IMPUTATION:")
print(sample.Calories.fillna(sample.Calories.mean()))

print("IN CASE OF ORDINAL ENCODING:")
data = pd.DataFrame({"subjects": ["Maths", "Chemistry", "Physics", "English", "Maths", "Maths", "Physics"]})
ordinal_map = {
    "Maths": 101,
    "Chemistry": 202,
    "Physics": 303,
    "English": 404
}
data["encoding"] = data["subjects"].replace(ordinal_map)
print(data)

print("IN CASE OF ONE HOT ENCODING:")
Maths_column = {"Maths": 1, "Chemistry": 0, "Physics": 0, "English": 0}
Chemistry_column = {"Maths": 0, "Chemistry": 1, "Physics": 0, "English": 0}
Physics_column = {"Maths": 0, "Chemistry": 0, "Physics": 1, "English": 0}
English_column = {"Maths": 0, "Chemistry": 0, "Physics": 0, "English": 1}

data["maths OH encoding"] = data["subjects"].replace(Maths_column)
data["chemistry OH encoding"] = data["subjects"].replace(Chemistry_column)
data["physics OH encoding"] = data["subjects"].replace(Physics_column)
data["english OH encoding"] = data["subjects"].replace(English_column)

del data["encoding"]
print(data)
