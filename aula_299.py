from dotenv import load_dotenv #type: ignore
import os

# senha = os.getenv('SENHA')

# print(os.getenv)

load_dotenv()

print(os.getenv('BD_PASSWORD'))