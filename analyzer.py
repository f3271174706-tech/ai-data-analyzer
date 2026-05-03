import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

def analyze_csv(file_path):
    # 读取数据
    df = pd.read_csv(file_path)
    
    print("=== 数据基本信息 ===")
    print(f"行数：{df.shape[0]}，列数：{df.shape[1]}")
    print(f"\n列名：{list(df.columns)}")
    print(f"\n数据预览：\n{df.head()}")
    print(f"\n基本统计：\n{df.describe()}")
    
    return df

def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma4:e4b",
            "prompt": prompt,
            "stream": False
        }
    )
    print("原始返回：", response.json())
    return response.json().get("response", "无法获取回复")

def main():
    file_path = input("请输入 CSV 文件路径：")
    df = analyze_csv(file_path)
    
    # 让 AI 分析数据
    prompt = f"""
    我有一份数据集，基本信息如下：
    列名：{list(df.columns)}
    行数：{df.shape[0]}
    基本统计：{df.describe().to_string()}
    
    请用中文分析这份数据，指出有趣的规律和洞察。
    """
    
    print("\n=== AI 分析结果 ===")
    result = ask_ollama(prompt)
    print(result)

if __name__ == "__main__":
    main()