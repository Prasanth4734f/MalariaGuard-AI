import time
import streamlit as st
from backend import predict_district

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#071426,#0B1E36,#112B49);
color:white;
}

.block-container{
padding-top:3rem;
padding-left:4rem;
padding-right:4rem;
}

.title{
font-size:42px;
font-weight:bold;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
color:#b6c3d4;
font-size:18px;
}

.glass{
background:rgba(255,255,255,.08);
backdrop-filter:blur(18px);
padding:40px;
border-radius:20px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0px 10px 30px rgba(0,0,0,.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- CHECK ---------------- #

if "district" not in st.session_state:
    st.switch_page("pages/Location.py")

district = st.session_state["district"]

st.markdown("<div class='title'>🤖 AI Prediction Engine</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Generating malaria prediction using Random Forest AI...</div>",
unsafe_allow_html=True
)

st.write("")

st.markdown("<div class='glass'>", unsafe_allow_html=True)

status = st.empty()

progress = st.progress(0)

steps = [
    "📊 Loading district information...",
    "🌦 Loading weather parameters...",
    "🧠 Preparing AI features...",
    "🤖 Running Random Forest model...",
    "📈 Predicting malaria cases...",
    "✅ Finalizing results..."
]

for i, step in enumerate(steps):

    status.info(step)

    progress.progress((i + 1) * 16)

    time.sleep(0.6)

status.success("Prediction completed successfully!")

st.write("")

with st.spinner("Generating prediction..."):
    result = predict_district(district)

if result is None:
    st.error("Unable to generate prediction.")
    st.stop()

st.session_state["prediction_result"] = result

time.sleep(1)

st.success("Redirecting to dashboard...")

time.sleep(1)

st.switch_page("pages/Dashboard.py")