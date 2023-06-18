import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20525912")

API_HASH = os.environ.get("API_HASH", "78770c1c42b2582fdd6af879d0a5dfb2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6211361676:AAHv_ufpz8LRZhEdFe-SF9Den0Arjl7InBA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "0") 

DB_NAME = os.environ.get("DB_NAME","musix")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://musix:musix@cluster0.bl6xsxv.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/36fc36f0990cc0506a997.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1471469091').split()]

PORT = os.environ.get("PORT", "8080")
