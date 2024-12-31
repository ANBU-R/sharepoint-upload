import requests
from msal import ConfidentialClientApplication
import os
from dotenv import load_dotenv
load_dotenv()

def get_token(client_id,tenant_id,client_secret)->str:
    try:
        authority = f"https://login.microsoftonline.com/{tenant_id}"
        app = ConfidentialClientApplication(
            client_id, authority=authority, client_credential=client_secret
        )
        scope = ["https://graph.microsoft.com/.default"]
        result = app.acquire_token_for_client(scopes=scope)
        return result["access_token"]
    except Exception as e:
        print(e)

token = get_token(client_id=os.getenv("CLIENT_ID"),tenant_id=os.getenv("TENANT_ID"),client_secret=os.getenv('CLIENT_SECRET'))

upload_url =f"https://graph.microsoft.com/v1.0/drives/{os.getenv('DRIVE_ID')}/root:/upload/test-5.txt:/content"
headers = {"Authorization": f"Bearer {token}"}

with  open('./test.txt') as file:
    res = requests.put(upload_url,headers=headers,data=file)
    print(res)



