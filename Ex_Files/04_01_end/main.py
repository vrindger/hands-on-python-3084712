import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]
# print(last_twenty_years)
for year in last_twenty_years:
    if year["value"]:
        display_width = year["value"] // 10_000_000

        print(f'{year["date"]}: {year["value"]}', "=" * display_width)
