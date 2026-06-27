import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os

seen_links = set()
seen_file = "article.txt"

namespaces = {
    "content": "http://purl.org/rss/1.0/modules/content/"
}

if os.path.exists(seen_file):
    with open(seen_file, "r", encoding="utf-8") as f:
        seen_links = set(line for line in f)



try:
    response = requests.get("https://444.hu/feed",timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
else:
    root = ET.fromstring(response.content)
    channel = root.find("channel")
    with open(seen_file, "a", encoding="utf-8") as f:
        for item in channel.findall("item"):
            link = item.find("link").text
            if "Link: "+link+"\n" in seen_links:
                continue

            title = item.find("title").text
            
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
