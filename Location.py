import requests

phone = input("Введите номер телефона без +: ")

lang = input("Введите кодовую страну, например RU: ")

url = "https://mobile-location.org/emulator/check"
params = {
   "driver": "geo",
   "country": f"{lang}",
   "provider": "phone",
   "uid": f"+{phone}",
   "mode": "undefined",
   "_": "1699147302770"
}

response = requests.get(url, params=params)

# Access the response data
json_result = response.json()

# Convert JSON to string
result = str(json_result)

# Remove JSON formatting
result = result.replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(",", "\n").replace("'", "").replace(":", " -")

# Print the result
print(result)
