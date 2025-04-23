leaves = 29
water = 1
daily_weather = ["☀️", "☁️", "☀️"]
daily_rain = [0, 0, 0, 8, 6]
daily_pests = [20, 13, 12, 16, 25]
daily_temps = [9,14,16,25,35,27,20]
chickens = 9
drought = 0
flood = 0
ideal = 0
cold = 0
hot = 0

for day in daily_weather:
  if day == "☀️":
    light = 2
  else:
    light = 1
  leaves += light + water

if daily_weather == "☁️":
    daily_rain = True
else:
    daily_weather = "☀️"

for rain in daily_rain:
  if rain < 1:
    leaves -= 1
    drought = drought + 1
  elif rain > 4:
    leaves -= 2
    flood = flood + 1
  else:
    leaves += 4
    ideal = ideal + 1


for pests in daily_pests:
    if chickens <= pests:
        pests_alive = pests - chickens
    else:
        pests_alive = 0

    if pests_alive == 0:
        leaves += 2

for temp in daily_temps:
  if temp < 10:
    leaves -= 2
  elif temp > 30:
    leaves -= 3
  elif 10 <= temp < 20:
    leaves += 2
  else:
    leaves += 3
  if temp < 10:
      cold = cold + 1
  elif temp > 30:
      hot = hot + 1
  else:
      ideal = ideal + 1

print('Leaves:', leaves)
print("Drought days:", drought)
print("Flood days:", flood)
print("Ideal days:", ideal)
print("Cold days:", cold)
print("Hot days:", hot)