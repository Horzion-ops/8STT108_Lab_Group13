import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('pro1_file.xlsx')


df_no_total = df[df['Region'] != 'Total']


descriptive_stats = df_no_total[['Female', 'Male', 'Total']].describe()
print(descriptive_stats)


plt.figure(figsize=(10, 6))
sns.set_palette("pastel")
sns.boxplot(data=df_no_total[['Female', 'Male', 'Total']], fliersize=5)
plt.title('Boxplot of Female, Male, and Total Cattle Counts', fontsize=16, fontweight='bold')
plt.ylabel('Cattle Count', fontsize=14)
plt.xticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


plt.figure(figsize=(12, 8))
sns.set_palette("Set2")
sns.boxplot(x='Region', y='Total', data=df_no_total, fliersize=5)
plt.title('Boxplot of Total Cattle per Region', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=12)
plt.ylabel('Total Cattle Count', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
