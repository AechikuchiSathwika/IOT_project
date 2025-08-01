import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Fan & Light Energy Cost Calculator", layout="centered")
st.title("🌀💡 1-Hour Fan & Light Energy & Cost Calculator")

# Constants
fan_power_watt = 25       # 25 W per fan
light_power_watt = 40     # 40 W per light
usage_hours = 1           # 1 hour

# Inputs
fan_count   = st.number_input("Enter number of fans:",   min_value=0, step=1, value=6)
light_count = st.number_input("Enter number of lights:", min_value=0, step=1, value=4)
rate        = st.number_input("Enter electricity rate per unit (₹/kWh):",
                              min_value=0.0, value=2.5, step=0.1)

# Calculations
energy_per_fan_kwh   = fan_power_watt   * usage_hours / 1000
energy_per_light_kwh = light_power_watt * usage_hours / 1000

total_energy_fans   = energy_per_fan_kwh   * fan_count
total_energy_lights = energy_per_light_kwh * light_count
total_energy        = total_energy_fans + total_energy_lights

cost_per_fan   = energy_per_fan_kwh   * rate
cost_per_light = energy_per_light_kwh * rate

total_cost_fans   = cost_per_fan   * fan_count
total_cost_lights = cost_per_light * light_count
total_cost        = total_cost_fans + total_cost_lights

# Outputs
st.markdown("### 🔍 Results")
st.info   (f"⚡ Energy — Fans: {total_energy_fans:.3f} kWh, Lights: {total_energy_lights:.3f} kWh")
st.success(f"💸 Cost   — Fans: ₹{total_cost_fans:.2f}, Lights: ₹{total_cost_lights:.2f}")
st.metric("💡 Total Energy (kWh)", f"{total_energy:.3f}")
st.metric("💰 Total Cost (₹)", f"₹{total_cost:.2f}")

# 1️⃣ BAR CHART: Energy per Appliance
st.subheader("📊 Energy per Appliance (kWh)")
bar_df = pd.DataFrame({
    "Appliance": ["Fans", "Lights"],
    "Energy_kWh": [total_energy_fans, total_energy_lights]
})
fig1, ax1 = plt.subplots()
ax1.bar(bar_df["Appliance"], bar_df["Energy_kWh"], color=["skyblue","gold"])
ax1.set_ylabel("Energy (kWh)")
ax1.set_title("Energy Used in 1 Hour")
st.pyplot(fig1)

# 2️⃣ PIE CHART: Cost Share
st.subheader("🥧 Cost Share per Appliance")
fig2, ax2 = plt.subplots()
ax2.pie([total_cost_fans, total_cost_lights],
        labels=["Fans", "Lights"],
        autopct="%1.1f%%",
        startangle=140)
ax2.set_title("Cost Distribution")
st.pyplot(fig2)

# 3️⃣ LINE CHART: Cost vs Count
st.subheader("📈 Cost vs Number of Units")
line_df = pd.DataFrame({
    "Count": list(range(1, 11)),
    "Fan Cost":   [i * cost_per_fan   for i in range(1, 11)],
    "Light Cost": [i * cost_per_light for i in range(1, 11)]
})
fig3, ax3 = plt.subplots()
ax3.plot(line_df["Count"], line_df["Fan Cost"],   marker="o", label="Fans")
ax3.plot(line_df["Count"], line_df["Light Cost"], marker="s", label="Lights")
ax3.set_xlabel("Number of Units")
ax3.set_ylabel("Cost (₹)")
ax3.set_title("Cost vs Number of Fans/Lights")
ax3.legend()
st.pyplot(fig3)