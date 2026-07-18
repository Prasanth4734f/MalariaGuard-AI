import streamlit as st
from backend import engine

st.set_page_config(
    page_title="Select District",
    page_icon="📍",
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
padding-top:2rem;
padding-left:4rem;
padding-right:4rem;
}

.title{
font-size:42px;
font-weight:700;
color:white;
}

.subtitle{
color:#b7c3d7;
font-size:18px;
}

.glass{
background:rgba(255,255,255,.08);
backdrop-filter:blur(18px);
padding:35px;
border-radius:20px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 10px 35px rgba(0,0,0,.4);
}

.card{
background:rgba(255,255,255,.08);
padding:20px;
border-radius:18px;
text-align:center;
border:1px solid rgba(255,255,255,.10);
}

.big{
font-size:32px;
font-weight:bold;
color:#00E5FF;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📍 Select District</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Choose a district to generate an AI malaria prediction.</div>",
unsafe_allow_html=True)

st.write("")

districts = engine.get_districts()

with st.container():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    district = st.selectbox(
        "Search District",
        districts,
        index=0
    )

    st.write("")

    details = engine.get_record(district)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class='card'>
        🌡
        <div class='big'>{details['T2M']:.1f}°C</div>
        Temperature
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='card'>
        💧
        <div class='big'>{details['RH2M']:.1f}%</div>
        Humidity
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='card'>
        🌧
        <div class='big'>{details['PRECIP']:.1f}</div>
        Rainfall
        </div>
        """,unsafe_allow_html=True)

    st.write("")

    col1,col2 = st.columns(2)

    with col1:

        if st.button("⬅ Home",use_container_width=True):
            st.switch_page("app.py")

    with col2:

        if st.button("🚀 Predict Malaria",use_container_width=True):

            st.session_state["district"]=district

            st.switch_page("pages/Processing.py")

    st.markdown("</div>",unsafe_allow_html=True)

st.write("")

st.info(
"""
### 🤖 AI Prediction

The selected district will be analysed using:

- Temperature
- Humidity
- Rainfall
- Historical malaria trend
- Random Forest Machine Learning Model

The prediction usually takes only a few seconds.
"""
)