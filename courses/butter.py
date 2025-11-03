import os
import requests
from dotenv import load_dotenv

load_dotenv()

BUTTER_API_KEY = os.getenv('BUTTER_API_KEY')
BASE_URL = 'https://api.buttercms.com/v2'

def get_home_page():
    if not BUTTER_API_KEY:
        return None
    url = f"{BASE_URL}/pages/home/?auth_token={BUTTER_API_KEY}"
    r = requests.get(url, timeout=10)
    if r.ok:
        return r.json().get('data', {})
    return None

def list_courses():
    if not BUTTER_API_KEY:
        return []
    url = f"{BASE_URL}/pages/course/?auth_token={BUTTER_API_KEY}"  # ✅ fixed
    r = requests.get(url, timeout=10)
    if r.ok:
        return r.json().get('data', [])
    return []


def get_course_by_slug(slug):
    if not BUTTER_API_KEY:
        return None
    url = f"{BASE_URL}/pages/course/{slug}/?auth_token={BUTTER_API_KEY}"
    r = requests.get(url, timeout=10)
    if r.ok:
        return r.json().get('data')
    return None
