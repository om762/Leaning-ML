import pandas as pd

table = pd.read_html("Pandas\In out File\-HTML\World population - Wikipedia.html")
table = table[4]
table.drop(["Percentage of the world", "Source (official or from the United Nations)"], axis=1, inplace= True)
table.set_index("Rank", inplace= True)
table.columns = ["Country", "Population", "Date"]
table.to_html("Pandas\In out File\-HTML\Top Ten.html")
print(table)