import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


namespaces = {
    "content": "http://purl.org/rss/1.0/modules/content/"
}

try:
    response = requests.get("https://444.hu/feed",timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
else:
    root = ET.fromstring(response.content)
    channel = root.find("channel")
    with open("article.txt", "a", encoding="utf-8") as f:
        for item in channel.findall("item"): 
            title = item.find("title").text
            link = item.find("link").text
            content_el = item.find("content:encoded", namespaces)
            full_text = content_el.text if content_el is not None else None
            clean_text = BeautifulSoup(full_text, "html.parser").get_text() if full_text else "N/A"
            pub_date = item.find("pubDate").text
            f.write(f"Title: {title}\n")
            f.write(f"Link: {link}\n ")
            f.write(f"Date: {pub_date}\n")
            f.write("---\n")
            f.write(f"Content: {clean_text if full_text else 'N/A'}...\n")
            f.write("---\n \n")
            print("Saved to article.txt")