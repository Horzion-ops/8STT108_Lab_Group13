import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('cleaned_olympics.xlsx')
df = df[df['Country'] != 'Totals']


sns.set_theme(style="whitegrid")
colors = sns.color_palette("pastel")


plt.figure(figsize=(10, 6))
ax1 = sns.barplot(x='Summer_Total', y='Country', data=df.nlargest(10, 'Summer_Total'),
                   hue='Country', palette=colors, legend=False)
plt.title('Top 10 Countries by Summer Total Medals', fontsize=16, fontweight='bold')
plt.xlabel('Total Medals', fontsize=14)
plt.ylabel('', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()


for p in ax1.patches:
    ax1.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                 ha='center', va='center', fontsize=10, color='black', weight='bold')



# 绘制冬季总奖牌数前10的国家
plt.figure(figsize=(10, 6))
ax2 = sns.barplot(x='Winter_Total', y='Country', data=df.nlargest(10, 'Winter_Total'),
                   hue='Country', palette=colors, legend=False)
plt.title('Top 10 Countries by Winter Total Medals', fontsize=16, fontweight='bold')
plt.xlabel('Total Medals', fontsize=14)
plt.ylabel('', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()

# 添加数据标签
for p in ax2.patches:
    ax2.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                 ha='center', va='center', fontsize=10, color='black', weight='bold')


# 绘制总奖牌数（夏季+冬季）前10的国家
combined_medals = df['Summer_Total'] + df['Winter_Total']
df['Combined_Medals'] = combined_medals

plt.figure(figsize=(10, 6))
ax3 = sns.barplot(x='Combined_Medals', y='Country',
                   data=df.nlargest(10, 'Combined_Medals').sort_values(by='Combined_Medals', ascending=False),
                   hue='Country', palette=colors, legend=False)
plt.title('Top 10 Countries by Combined Total Medals', fontsize=16, fontweight='bold')
plt.xlabel('Total Medals (Summer + Winter)', fontsize=14)
plt.ylabel('', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()

# 添加数据标签
for p in ax3.patches:
    ax3.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                 ha='center', va='center', fontsize=10, color='black', weight='bold')

plt.show()
