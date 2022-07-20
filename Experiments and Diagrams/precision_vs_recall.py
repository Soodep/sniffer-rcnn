import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'Prevision_vs_Recall.xlsx', engine='openpyxl')
df.plot('Precision', 'Recall')
plt.show()
