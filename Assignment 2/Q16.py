
import pandas as pd
data_frame = pd.read_csv("hello1.csv" ,sep = ':')   
print(data_frame.head)
arr = data_frame.to_numpy()
print(arr)