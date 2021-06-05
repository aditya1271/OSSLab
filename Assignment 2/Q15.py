
import pandas as pd
data_frame = pd.read_csv("hello.csv")   
print(data_frame.head)
arr = data_frame.to_numpy()
print(arr)