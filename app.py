import streamlit as st
from modules import input_parser, system_config

st.set_page_config(page_title="光储充测算系统", layout="wide")
st.title("🚍 光储充一体化项目投资测算系统")

# 输入参数
inputs = input_parser.get_user_inputs()

# 推导配置
st.header("⚙️ 系统配置推导结果")
config = system_config.derive_system_config(inputs)

st.write(f"🌞 光伏总装机容量：**{config['pv_capacity_kwp']} kWp**")
st.write(f"组件总数：{config['total_modules']}块，其中屋顶：{config['rooftop_modules']}，车棚：{config['carport_modules']}")
