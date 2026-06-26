import requests
import xml.etree.ElementTree as ET


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
    for item in channel.findall("item")[:5]: 
        title = item.find("title").text
        link = item.find("link").text
        content_el = item.find("content:encoded", namespaces)
        full_text = content_el.text if content_el is not None else None
        pub_date = item.find("pubDate").text
        print(f"Title: {title}\n")
        print(f"Link: {link}\n ")
        print(f"Date: {pub_date}\n")
        print("---")
        print(f"Content: {full_text.replace('<p>','').replace('</p>','') if full_text else 'N/A'}...")
        print("---")