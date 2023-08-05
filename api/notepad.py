from person import *
import pandas as pd

df = pd.read_csv("C:/Users/willi/OneDrive/Desktop/In_Line/api/line.csv", header=0)
df.set_index('id', inplace=True)

for row_index in range(len(df.index)):
    if df.loc[row_index]['in_line']:
        fred = Person(id=row_index)
        fred.link_to_database()
        fred.send_text()
        