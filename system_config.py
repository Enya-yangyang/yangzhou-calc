def derive_system_config(inputs):
    module_power = 550  # W
    install_density = 0.18  # 块/m²

    rooftop_modules = int(inputs["rooftop_area"] * install_density)
    carport_modules = int(inputs["carport_num"] * 12 * install_density)

    total_modules = rooftop_modules + carport_modules
    total_pv_kwp = round(total_modules * module_power / 1000, 2)  # 转为kWp

    return {
        "module_power": module_power,
        "rooftop_modules": rooftop_modules,
        "carport_modules": carport_modules,
        "total_modules": total_modules,
        "pv_capacity_kwp": total_pv_kwp
    }
