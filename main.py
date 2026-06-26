import requests



try:
    response = requests.get("https://444.hu/feed",timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
else:
    print(response.text)