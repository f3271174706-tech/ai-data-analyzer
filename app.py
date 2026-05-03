import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY", "").strip()
client = Groq(api_key=api_key)

matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

st.set_page_config(page_title="AI数据分析助手", layout="wide")
st.title("🤖 本地AI数据分析助手")
st.caption("由 Groq + Llama3 驱动，快速智能分析")

uploaded_file = st.file_uploader("上传你的CSV文件", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📋 数据预览")
    st.dataframe(df.head(10))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("总行数", df.shape[0])
    col2.metric("总列数", df.shape[1])
    col3.metric("总销售额", f"{df['销售额'].sum():,}" if '销售额' in df.columns else "N/A")
    
    st.subheader("📊 可视化图表")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    if '城市' in df.columns and '销售额' in df.columns:
        city_sales = df.groupby('城市')['销售额'].sum().sort_values(ascending=False)
        axes[0].bar(city_sales.index, city_sales.values, color='steelblue')
        axes[0].set_title('各城市总销售额')
    
    if '产品类别' in df.columns and '销售额' in df.columns:
        cat_sales = df.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)
        axes[1].bar(cat_sales.index, cat_sales.values, color='coral')
        axes[1].set_title('各产品类别总销售额')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.subheader("🧠 AI智能分析")
    if st.button("开始AI分析"):
        with st.spinner("AI正在分析数据，请稍等..."):
            prompt = f"""
            我有一份数据集，基本信息如下：
            列名：{list(df.columns)}
            行数：{df.shape[0]}
            基本统计：{df.describe().to_string()}
            请用中文分析这份数据，指出有趣的规律和洞察。
            """
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.markdown(result)