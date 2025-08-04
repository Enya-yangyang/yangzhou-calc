import streamlit as st

def get_user_inputs():
    st.subheader("请输入场站基础信息")

    project_name = st.text_input("项目名称", value="XX公交场站光储充项目")
    city = st.text_input("城市/地址", value="广州")
    
    st.markdown("### 📐 场地信息")
    rooftop_area = st.number_input("可用屋顶面积（㎡）", value=3000.0, min_value=0.0)
    carport_num = st.number_input("可建设车棚车位数（个）", value=50, min_value=0)
    
    st.markdown("### 🚍 公交车辆与负荷")
    bus_num = st.number_input("公交车数量（台）", value=60, min_value=0)
    charge_per_bus = st.number_input("每车日均充电量（kWh）", value=120.0, min_value=0.0)
    annual_load = st.number_input("年总用电量（万kWh）", value=80.0, min_value=0.0)

    st.markdown("### ☀️ 光照与电价")
    full_sun_hours = st.number_input("年满发小时数（h）", value=1300, min_value=0)
    self_use_price = st.number_input("自用电价（元/kWh）", value=0.85, min_value=0.0)
    grid_price = st.number_input("上网电价（元/kWh）", value=0.30, min_value=0.0)

    return {
        "project_name": project_name,
        "city": city,
        "rooftop_area": rooftop_area,
        "carport_num": carport_num,
        "bus_num": bus_num,
        "charge_per_bus": charge_per_bus,
        "annual_load": annual_load * 10000,  # 转为kWh
        "full_sun_hours": full_sun_hours,
        "self_use_price": self_use_price,
        "grid_price": grid_price
    }
