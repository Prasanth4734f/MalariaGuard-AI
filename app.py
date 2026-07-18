import streamlit as st

st.set_page_config(
    page_title="MalariaGuard AI",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:4rem;
padding-right:4rem;
}

.stApp{
background:linear-gradient(135deg,#071426,#0B1E36,#112B49);
color:white;
}

.hero{
background:rgba(255,255,255,0.08);
backdrop-filter:blur(18px);
padding:40px;
border-radius:25px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0px 15px 40px rgba(0,0,0,.4);
}

.title{
font-size:52px;
font-weight:800;
color:white;
}

.gradient{
background:linear-gradient(90deg,#00E5FF,#4ADE80);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
font-size:20px;
color:#d6d6d6;
margin-top:15px;
}

.card{
background:rgba(255,255,255,.08);
border-radius:20px;
padding:25px;
text-align:center;
border:1px solid rgba(255,255,255,.12);
transition:0.3s;
height:180px;
}

.card:hover{
transform:translateY(-8px);
background:rgba(255,255,255,.12);
}

.metric{
font-size:38px;
font-weight:700;
color:#00E5FF;
}

.label{
font-size:18px;
color:white;
}

.sectiontitle{
font-size:30px;
font-weight:700;
margin-top:40px;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

left,right = st.columns([1.3,1])

with left:

    st.markdown("""
    <div class='hero'>

    <div class='title'>
    🦟 <span class='gradient'>MalariaGuard AI</span>
    </div>

    <div class='subtitle'>
    AI Powered Malaria Surveillance and Disease Prediction System
    </div>

    <br>

    Predict malaria outbreaks using

    ✔ Weather Intelligence

    ✔ Machine Learning

    ✔ Random Forest Prediction

    ✔ District Level Analytics

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 Start Prediction", use_container_width=True):
        st.switch_page("pages/Location.py")

with right:

    st.markdown("""

# 🤖 AI Health Assistant

---

### ✔ AI Model

Random Forest Regressor

---

### ✔ Dataset

NASA POWER

Malaria Surveillance Dataset

---

### ✔ Accuracy

**92.5%**

---

### ✔ Prediction

District-wise Forecasting

""")

st.write("")
st.write("")
# ---------------- FEATURES ---------------- #

st.markdown(
    "<div class='sectiontitle'>✨ AI Platform Features</div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='card'>
        <div style='font-size:48px;'>🧠</div>
        <div class='metric'>AI</div>
        <div class='label'>Random Forest Prediction</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
        <div style='font-size:48px;'>🌦</div>
        <div class='metric'>Weather</div>
        <div class='label'>Temperature • Humidity • Rainfall</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
        <div style='font-size:48px;'>📊</div>
        <div class='metric'>Analytics</div>
        <div class='label'>District Level Disease Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='card'>
        <div style='font-size:48px;'>🛡</div>
        <div class='metric'>Prevention</div>
        <div class='label'>Risk Assessment & Recommendations</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- HOW IT WORKS ---------------- #

st.write("")
st.markdown(
    "<div class='sectiontitle'>⚙️ How MalariaGuard AI Works</div>",
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)

with step1:
    st.info(
        """
### 📍 Step 1

Choose a district from the available list.

The latest weather and malaria records are loaded automatically.
"""
    )

with step2:
    st.info(
        """
### 🤖 Step 2

Our trained Random Forest model processes:

- Temperature
- Humidity
- Rainfall
- Historical malaria trends

to predict future malaria cases.
"""
    )

with step3:
    st.info(
        """
### 📊 Step 3

View:

- Predicted Cases
- Risk Level
- Weather Conditions
- Prevention Suggestions
"""
    )

# ---------------- PROJECT INFO ---------------- #

st.write("")
st.markdown(
    "<div class='sectiontitle'>📌 About This Project</div>",
    unsafe_allow_html=True
)

st.markdown("""
This AI-powered healthcare dashboard predicts malaria cases using environmental
conditions and historical malaria data.

The prediction model has been trained using a **Random Forest Regressor**
combined with engineered weather features to estimate district-level malaria
risk.

The objective is to assist health officials and researchers in monitoring
potential outbreaks and supporting preventive decision-making.
""")

st.write("")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 AI Model", "Random Forest")

with col2:
    st.metric("📈 Model Accuracy", "92.5%")

with col3:
    st.metric("🛰 Data Source", "NASA POWER")

st.markdown(
    """
<div style="text-align:center;color:#94A3B8;padding-top:20px;">
MalariaGuard AI • AI Powered Disease Surveillance & Prediction System
</div>
""",
    unsafe_allow_html=True
)