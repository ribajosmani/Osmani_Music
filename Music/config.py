##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv('SESSION_NAME', "BAAkcO4N6bBz4buGS1A7xDRoS7L3-L9KuNzXBIB_Fr7lqb2LyFE1I2lBtMcO9aRQOJroutYTqhj5QdpyDzjp4sE-FkstbsPb-clB8_DYH3NVgVr3l7fMiWFJ6G0VhnnOnSYyUaVtEFZKqeCcdUv0abbx5GQupXzn0dVPckfdENJCdrZv2mIFnMCko_GyDSfQDGeecm3VVqMvXLO5YeptHQCsDops_vokxoi4wCikVeP9sfAIiMT5CpWSibY_sAEReFzJTdRehBDf4jKE6WwOmVZluOsNwHhLKi-Wn_shMgEwHd0UxfKzKDwPf_YTbdgjCBJi7PX6fJsrBwYJU0232tVvAAAAATTDl_YA")
BOT_TOKEN = getenv('BOT_TOKEN' "5462008662:AAG5mk5QF0JNi_ruvoiSmdREHMiUOMZlxNY")
API_ID = int(getenv('API_ID', "15499461"))
API_HASH = getenv('API_HASH', "ff93948d3b7c3091e8d573275a4ed80f")
DURATION_LIMIT = int(getenv('DURATION_LIMIT', "540000"))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! .').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Mosia_Mk_Bot:mosia@cluster0.91lut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', "1008271006").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001150107625"))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
ZAID_SUPPORT = getenv("ZAID_SUPPORT", "osmanigroupbot")
ASS_ID = int(getenv("ASS_ID", "5180200950"))
OWNER_ID = list(map(int, getenv('OWNER_ID', "1008271006").split()))
