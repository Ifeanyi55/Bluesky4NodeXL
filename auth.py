from atproto import Client
from dotenv import load_dotenv
import os

load_dotenv()

bsky_username = os.environ.get("BSKY_USERNAME")
bsky_password = os.environ.get("BSKY_PASSWORD")

client = Client()
client.login(bsky_username, bsky_password)