import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27136615")

API_HASH = os.environ.get("API_HASH", "bb0b4dfb048fe0c002799e7c022b4f90")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7071606442:AAEozO-Y9UPhehKrT3-QemqMLOPN_h_tdjY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "HarshithXDev") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://HarshithXDev:<HarshithXDev>@cluster0.pu2so1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
