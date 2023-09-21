import pandas as pd

def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name

messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
messy_names = messy_names.apply(cleanup)
print(messy_names)