import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


df = pd.read_excel('decathlete2008_dataLabo4.xlsx')


columns_to_use = [
    'Run100_pts', 'LJ_pts', 'SP_pts', 'HJ_pts',
    'Run400_pts', 'H_pts', 'DT_pts', 'PV_pts',
    'JT_pts', 'Run1500_pts'
]
data = df[columns_to_use]


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

pca = PCA(n_components=10)
principal_components = pca.fit_transform(data_scaled)


explained_variance_ratio = pca.explained_variance_ratio_
print("Explained variance ratio:", explained_variance_ratio)


plt.figure(figsize=(12, 7))
bars = plt.bar(
    range(1, len(explained_variance_ratio) + 1),
    explained_variance_ratio,
    alpha=0.8, color='skyblue',
    edgecolor='black', linewidth=1.2
)

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f'{yval:.2f}',
        ha='center', va='bottom',
        fontsize=10
    )


plt.ylabel('Explained Variance Ratio', fontsize=14)
plt.xlabel('Principal Component Index', fontsize=14)
plt.title('Explained Variance by Principal Components', fontsize=16, fontweight='bold')
plt.xticks(range(1, len(explained_variance_ratio) + 1), fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
