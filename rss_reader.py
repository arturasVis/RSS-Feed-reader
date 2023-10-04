import feedparser
import requests

def fetch_feed(url):
    response = requests.get(url)
    response.raise_for_status()
    return feedparser.parse(response.content)

def display_feed(feed):
    for entry in feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print(f'Description: {entry.description}')
        print('-' * 50)  # Print a separator line

if __name__ == "__main__":
    print("Please input RSS url")
    url = input()
    feed = fetch_feed(url)
    display_feed(feed)