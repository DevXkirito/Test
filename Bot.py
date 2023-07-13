from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from bs4 import BeautifulSoup

app = Client("my_bot")

@app.on_message(filters.command("index"))
def index_command(client: Client, message: Message):
    url = "https://estanime.com"  # Replace with the URL of the website to scrape
    post_titles = get_post_titles(url)
    if post_titles:
        message.reply_text("\n".join(post_titles))
    else:
      message.reply_text("No post titles found.")

def get_post_titles(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        post_titles = []
        for post in soup.find_all("a", class_="post-title"):  # Adjust the CSS selector as per the website structure
            post_titles.append(post.text.strip())
        return post_titles
    except requests.RequestException:
        return None

app.run()
