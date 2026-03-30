import streamlit as st
import joblib
import numpy as np
import os
import gdown

if not os.path.exists("model.pkl"):
    url = "https://drive.google.com/uc?id=1txaBTZS274ZNtbn0NIyp-GZv3n4a83LA"
    gdown.download(url, "model.pkl", quiet=False)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Retail Sales Dashboard",
    layout="centered"
)

# =========================
# CUSTOM CSS (ANIMATIONS + STYLE)
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
}

.main {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    animation: fadeIn 1.2s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #ddd;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: scale(1.03);
}

.stButton>button {
    background: linear-gradient(90deg, #ff7e5f, #feb47b);
    border: none;
    color: white;
    padding: 10px 25px;
    border-radius: 8px;
    font-size: 16px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff6a00, #ee0979);
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model.pkl")

# =========================
# UI HEADER
# =========================
st.markdown('<div class="title">📊 Retail Sales Forecast</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict future sales using AI-powered forecasting</div>', unsafe_allow_html=True)

# =========================
# INPUT CARD
# =========================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        store = st.number_input("🏪 Store Number", 1, 54, 1)
        family = st.number_input("📦 Product Family (encoded)", 0, 33, 0)
        onpromo = st.selectbox("🔥 On Promotion", [0, 1])

    with col2:
        year = st.number_input("📅 Year", 2013, 2025, 2017)
        month = st.number_input("📅 Month", 1, 12, 1)
        day = st.number_input("📅 Day", 1, 31, 1)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREDICTION
# =========================
if st.button("🚀 Predict Sales"):

    with st.spinner("🔮 Predicting..."):

        # dummy features (same structure as training)
        features = [
            store, family, onpromo,
            year, month, day, 0, 0,
            70,
            0,0,0,0,0,0,
            0,0,0,
            0
        ]

        pred_log = model.predict([features])
        pred = np.expm1(pred_log[0])

    # =========================
    # RESULT CARD
    # =========================
    st.markdown(
        f"""
        <div class="card" style="margin-top:20px; text-align:center;">
            <h2 style="color:white;">📈 Predicted Sales</h2>
            <h1 style="color:#00ffcc;">{pred:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

# =========================
# FOOTER
# =========================
st.markdown("""
<br>
<p style='text-align:center; color:gray;'>
Built with ❤️ using Streamlit & LightGBM
</p>
""", unsafe_allow_html=True)