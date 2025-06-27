import requests
import os
from dotenv import load_dotenv

load_dotenv()
FIREBASE_API_KEY = os.getenv('GOOGLE_API')  # Make sure this is set correctly

def sign_in_with_google(id_token):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={FIREBASE_API_KEY}"
    payload = {
        "postBody": f"id_token={id_token}&providerId=google.com",
        "requestUri": "http://localhost",
        "returnIdpCredential": True,
        "returnSecureToken": True
    }
    r = requests.post(url, json=payload)
    return r.json()