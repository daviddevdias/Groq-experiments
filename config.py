"""Compatibilidade para experimentos que importam api_key."""
import os

api_key = os.environ.get("GROQ_API_KEY", "")
