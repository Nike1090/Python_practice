import os
from dotenv import load_dotenv

load_dotenv()


# email 
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
SENDER_TOKEN = os.getenv('SENDER_TOKEN')

