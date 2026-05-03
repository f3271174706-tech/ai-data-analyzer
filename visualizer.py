import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'  # 支持中文

def generate_charts(file_path):
    df = pd.read_csv(file_path)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('销售数据分析报告', fontsize=16)

    # 1. 各城市销售额
    city_sales = df.groupby('城市')['销售额'].sum().sort_values(ascending=False)
    axes[0, 0].bar(city_sales.index, city_sales.values, color='steelblue')
    axes[0, 0].set_title('各城市总销售额')
    axes[0, 0].set_xlabel('城市')
    axes[0, 0].set_ylabel('销售额')

    # 2. 各产品类别销售额
    cat_sales = df.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)
    axes[0, 1].bar(cat_sales.index, cat_sales.values, color='coral')
    axes[0, 1].set_title('各产品类别总销售额')
    axes[0, 1].set_xlabel('产品类别')
    axes[0, 1].set_ylabel('销售额')

    # 3. 月份销售趋势
    month_sales = df.groupby('月份')['销售额'].sum()
    axes[1, 0].plot(month_sales.index, month_sales.values, marker='o', color='green')
    axes[1, 0].set_title('月份销售趋势')
    axes[1, 0].set_xlabel('月份')
    axes[1, 0].set_ylabel('销售额')

    # 4. 销售额分布
    axes[1, 1].hist(df['销售额'], bins=20, color='purple', alpha=0.7)
    axes[1, 1].set_title('销售额分布')
    axes[1, 1].set_xlabel('销售额')
    axes[1, 1].set_ylabel('频次')

    plt.tight_layout()
    plt.savefig('D:\\mycode\\sales_report.png', dpi=150)
    print("图表已保存：D:\\mycode\\sales_report.png")
    plt.show()

if __name__ == "__main__":
    generate_charts("D:\\mycode\\sales_data.csv")