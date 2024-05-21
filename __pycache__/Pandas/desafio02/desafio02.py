import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataprep.eda import create_report

df = pd.read_csv('l:/Documentos/curso-em-video/__pycache__/Pandas/desafio02/ibm_hr.csv')
df = df.head(10)
df = df.drop([])
print(df)
