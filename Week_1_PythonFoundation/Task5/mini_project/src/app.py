import streamlit as st
import json
import os
from datetime import datetime
from ui import load_styles, header, journal_form, show_entry

DATA_FILE = "src/data.json"

# ---------- Data Handling ----------
def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_entries(entries):
    with open(DATA_FILE, "w") as file:
        json.dump(entries, file, indent=4)


class Entry:
    def __init__(self, text, mood):
        self.text = text
        self.mood = mood
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "text": self.text,
            "mood": self.mood,
            "date": self.date
        }


# ---------- Page Setup ----------
st.set_page_config(page_title="Daily Journal", layout="centered")
load_styles()
header()

entries = load_entries()

# ---------- Journal Form ----------
text, mood, submit = journal_form()

if submit:
    if text.strip() == "":
        st.warning("⚠️ Please write something before saving.")
    else:
        try:
            entry = Entry(text, mood)
            entries.append(entry.to_dict())
            save_entries(entries)
            st.success("✨ Entry saved successfully!")
        except Exception:
            st.error("❌ Something went wrong while saving.")

# ---------- Previous Entries ----------
st.markdown("## 📜 Previous Entries")

if not entries:
    st.info("No entries yet. Start writing ✨")
else:
    for e in reversed(entries):
        show_entry(e)
