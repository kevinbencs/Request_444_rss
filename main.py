import requests
import xml.etree.ElementTree as ET


try:
    response = requests.get("https://444.hu/feed",timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
else:
    root = ET.fromstring(response.content)
    channel = root.find("channel")
    for item in channel.findall("item")[:5]:  # first 5 articles
        title = item.find("title").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text
        print(f"{title}\n  {link}\n  {pub_date}\n")