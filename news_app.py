#News App

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def news_app():

    topic = input("Enter a topic: ")

    try:
        response = requests.get(
            f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}",
            timeout=10
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return

    try:
        data = response.json()

    except requests.exceptions.JSONDecodeError:
        print("Error: Unable to decode JSON response")
        return
    try: 
        article_data = data['articles']
    except KeyError:
        print("Error: 'articles' key not found in response")
        return

    for article in article_data:

        print(f"Title: {article.get('title', 'N/A')}")

        print(f"Description: {article.get('description', 'N/A')}")

        print(f'SOURCE: {article.get("source", {}).get("name", "N/A")}')

        print(f"URL: {article.get('url', 'N/A')}")

        print("---")
    

news_app()

y = input("Do you want to search for another topic? (yes/no): ")

while True:
    if y.lower() == "yes":
        news_app()
        y = input("Do you want to search for another topic? (yes/no): ")
    elif y.lower() == "no":
        print("Thank you for using the News App!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        y = input("Do you want to search for another topic? (yes/no): ")