from supabase import create_client, Client
from src.config.app_config import AppConfig
import streamlit as st

class AuthService:
    def __init__(self):
        try:
            self.supabase: Client = create_client(
                AppConfig.SUPABASE_URL, 
                AppConfig.SUPABASE_KEY
            )
        except Exception as e:
            st.error("Failed to connect to Database. Check .env config.")
            self.supabase = None

    def sign_in(self, email, password):
        try:
            res = self.supabase.auth.sign_in_with_password({
                "email": email, 
                "password": password
            })
            return res.user
        except Exception as e:
            return None

    def sign_out(self):
        self.supabase.auth.sign_out()
