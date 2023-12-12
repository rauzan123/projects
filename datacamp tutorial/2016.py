import pandas as pd
avocados = pd.read_pickle(r'C:\Users\LENOVO\Downloads\avoplotto.pkl')
print(avocados)

avocados_2016 = avocados[avocados["year"] == 2016]
print(avocados_2016)

avocados_2016_fix = avocados_2016.pivot_table("nb_sold", index=["date", "avg_price"] , columns=["size"])
avocados_2016_fix["total sold"] = avocados_2016_fix["size"] == ["extra_large", "large", "small"]
print(avocados_2016_fix)


