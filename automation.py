import time

# A simple dictionary simulating raw agricultural sensor data
sensor_data = {
    "farm_location": "Gwarinpa, Nigeria",
    "soil_moisture": "32%",
    "temperature_celsius": 28.5
}

print("🚀 Starting automated farm data analysis...")
time.sleep(1) # Pauses for 1 second

# Simple data check
if float(sensor_data["soil_moisture"].replace("%", "")) < 40:
    action_required = "⚠️ Soil is dry! Triggering automated irrigation systems."
else:
    action_required = "✅ Soil moisture is optimal. No action needed."

# Display the results
print(f"Location: {sensor_data['farm_location']}")
print(f"Status: {action_required}")
print("📊 Data pipeline successfully completed!")
