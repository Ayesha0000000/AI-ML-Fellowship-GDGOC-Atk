import streamlit as st

# ---------- Global Styles ----------
def load_styles():
    st.markdown("""
    <style>
        /* Full app background */
        .stApp {
            background: linear-gradient(135deg, #e0eafc, #cfdef3);
        }

        /* Center container */
        .main {
            padding-top: 40px;
        }

        /* Title */
        .title {
            font-size: 42px;
            font-weight: 800;
            text-align: center;
            color: #2e2e2e;
        }

        .subtitle {
            text-align: center;
            color: #6c757d;
            margin-bottom: 40px;
        }

        /* Glass card */
        .card {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 18px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
            margin-bottom: 30px;
        }

        /* Previous entry card */
        .entry {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 14px;
            padding: 15px;
            margin-bottom: 12px;
        }

        .date {
            font-size: 13px;
            color: #555;
        }

        .mood {
            font-weight: 600;
            color: #4e73df;
        }

        /* Buttons */
        button {
            border-radius: 10px !important;
        }
    </style>
    """, unsafe_allow_html=True)


# ---------- Page Header ----------
def header():
    st.markdown('<div class="title">📔 Daily Journal</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Write your thoughts & track your mood</div>',
        unsafe_allow_html=True
    )


# ---------- Journal Input Form ----------
def journal_form():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    with st.form("entry_form"):
        text = st.text_area("✍️ Write something", height=150)
        mood = st.selectbox(
            "😊 Select mood",
            ["Happy", "Neutral", "Tired", "Stressed"]
        )
        submit = st.form_submit_button("💾 Save Entry")

    st.markdown('</div>', unsafe_allow_html=True)
    return text, mood, submit


# ---------- Show Single Entry ----------
def show_entry(entry):
    st.markdown(f"""
        <div class="entry">
            <div class="date">🗓 {entry['date']} | <span class="mood">{entry['mood']}</span></div>
            <div>{entry['text']}</div>
        </div>
    """, unsafe_allow_html=True)
