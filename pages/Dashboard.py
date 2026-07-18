import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Prediction Dashboard",
    page_icon="📊",
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
padding-left:3rem;
padding-right:3rem;
}

.title{
font-size:42px;
font-weight:bold;
color:white;
}

.subtitle{
font-size:18px;
color:#b7c3d7;
}

.card{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 10px 25px rgba(0,0,0,.35);
}

.metric{
font-size:34px;
font-weight:bold;
color:#00E5FF;
}

.small{
color:#b7c3d7;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ---------------- #

if "prediction_result" not in st.session_state:
    st.switch_page("pages/Location.py")

result = st.session_state["prediction_result"]

prediction = float(result["prediction"])
risk = result["risk"]

temp = result["weather"]["temperature"]
humidity = result["weather"]["humidity"]
rain = result["weather"]["rainfall"]

deaths = result["deaths"]

district = result["district"]

# ---------------- TITLE ---------------- #

st.markdown(
f"<div class='title'>📊 {district} Dashboard</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>AI Powered Malaria Prediction Results</div>",
unsafe_allow_html=True
)

st.write("")

# ---------------- METRICS ---------------- #

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
<div class='card'>
<div class='metric'>{prediction:.0f}</div>
<div class='small'>Predicted Cases</div>
</div>
""",unsafe_allow_html=True)

with c2:

    color="🟢"

    if risk=="MODERATE":
        color="🟡"

    if risk=="HIGH":
        color="🔴"

    st.markdown(f"""
<div class='card'>
<div class='metric'>{color}</div>
<div class='small'>{risk} RISK</div>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown(f"""
<div class='card'>
<div class='metric'>{deaths}</div>
<div class='small'>Malaria Deaths</div>
</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class='card'>
<div class='metric'>92.5%</div>
<div class='small'>Model Accuracy</div>
</div>
""",unsafe_allow_html=True)

st.write("")

# ---------------- WEATHER ---------------- #

st.subheader("🌦 Weather Conditions")

w1,w2,w3=st.columns(3)

with w1:
    st.metric("🌡 Temperature",f"{temp:.1f} °C")

with w2:
    st.metric("💧 Humidity",f"{humidity:.1f}%")

with w3:
    st.metric("🌧 Rainfall",f"{rain:.1f} mm")

st.write("")

# ---------------- CHART ---------------- #

fig=go.Figure()

fig.add_trace(go.Bar(
    x=["Temperature","Humidity","Rainfall","Prediction"],
    y=[temp,humidity,rain,prediction]
))

fig.update_layout(
    title="AI Prediction Summary",
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.write("")

# ---------------- RECOMMENDATION ---------------- #

st.subheader("🩺 AI Recommendation")

if risk=="LOW":

    st.success("""
✅ Low Risk

• Continue surveillance

• Remove stagnant water

• Maintain sanitation
""")

elif risk=="MODERATE":

    st.warning("""
⚠ Moderate Risk

• Increase mosquito control

• Community awareness

• Monitor cases regularly
""")

else:

    st.error("""
🚨 High Risk

• Immediate vector control

• Indoor spraying

• Medical camps

• Public awareness

• Health department intervention recommended
""")

st.write("")

col1,col2=st.columns(2)

with col1:

    if st.button("🔄 Predict Another District",use_container_width=True):

        st.session_state.pop("prediction_result",None)

        st.switch_page("pages/Location.py")

with col2:

    if st.button("🏠 Home",use_container_width=True):

        st.session_state.clear()

        st.switch_page("app.py")

st.markdown("---")

st.caption("MalariaGuard AI • Powered by Random Forest Machine Learning")