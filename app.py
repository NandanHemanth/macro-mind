import streamlit as st

# Set page configuration
st.set_page_config(page_title="MacroMind", page_icon="💪", layout="wide")

import requests
import json
import os
import subprocess
import sqlite3
from streamlit_lottie import st_lottie
from PIL import Image

class UserProfileManager:
    def __init__(self, path="./database/user_data.json"):
        self.path = path
        self.default_data = {
            "name": "",
            "height": 170,
            "weight": 70,
            "goal": "",
            "dietary_restriction": ""
        }
        self.init_data()

class LottieLoader:
    @staticmethod
    def load(url):
        try:
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        except:
            return None