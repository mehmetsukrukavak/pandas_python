import pandas as pd
import numpy as np

data = [1923, 1868, 1922]
index = ["Türkiye","Japonya","SSCB"]


countries = pd.Series(data=data, index=index)

print(countries)

np.random.seed(9)
sayi = np.random.randint(0, 50, (5,4))
akdeniz = ["Isparta", "Antalya", "Konya", "Maraş", "Adana"]
mevsim = ["Bahar", "Yaz", "Kış", "Güz" ]

df = pd.DataFrame(data=sayi, index = akdeniz, columns=mevsim)

print(df)
print(df.info())
print(df.describe())