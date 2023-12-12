import pickle as pkl
import pandas as pd
with open(r'C:\Users\LENOVO\Downloads\financials.p', "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv(r'C:\Users\LENOVO\Downloads\financials.csv')


