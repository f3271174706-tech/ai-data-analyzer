import pandas as pd
import numpy as np

# 生成模拟电商销售数据
np.random.seed(42)
n = 100

data = {
    "订单ID": range(1, n+1),
    "产品类别": np.random.choice(["电子产品", "服装", "食品", "书籍"], n),
    "销售额": np.random.randint(50, 5000, n),
    "数量": np.random.randint(1, 20, n),
    "城市": np.random.choice(["北京", "上海", "广州", "深圳", "成都"], n),
    "月份": np.random.randint(1, 13, n)
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False, encoding="utf-8-sig")
print("测试数据生成成功！文件名：sales_data.csv")