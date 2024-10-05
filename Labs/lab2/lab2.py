import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'BostonHousing.xlsx'
data = pd.read_excel(file_path)


corr_matrix = data.corr()

plt.figure(figsize=(10, 8))


sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Boston Housing Data')
plt.show()


sns.pairplot(data[['medv', 'rm', 'lstat', 'ptratio', 'crim']], diag_kind='kde')

plt.suptitle('Pairwise Scatter Plots for Key Variables', y=1.02)
plt.show()