import streamlit as st
import requests

st.set_page_config(

    page_title="AI-Powered Mobile Addiction Risk Prediction",

    page_icon="📱",

    layout="wide"
)

st.markdown("""
<style>

.stApp {

    background-color: #F5F7FB;
}

.block-container {

    padding-top: 5rem;
    padding-bottom: 2rem;

    max-width: 98%;
}

label {

    color: #0F172A !important;

    font-size: 17px !important;

    font-weight: 600 !important;
}

.stNumberInput label,
.stSelectbox label {

    color: #0F172A !important;

    opacity: 1 !important;
}

.result-card {

    background: white;

    border-radius: 35px;

    padding: 60px;

    text-align: center;

    box-shadow:
        0px 10px 30px rgba(0,0,0,0.05);

    border: 1px solid #E2E8F0;
}

.metric-box {

    background: #F8FAFC;

    border-radius: 25px;

    padding: 25px;

    width: 55%;

    margin: auto;

    margin-top: 25px;

    margin-bottom: 30px;
}

.metric-text {

    font-size: 90px;

    font-weight: 800;
}

.metric-hours {

    font-size: 40px;

    font-weight: 700;
}

.low-text {

    color: #22C55E;
}

.medium-text {

    color: #F59E0B;
}

.high-text {

    color: #EF4444;
}

.risk-box {

    display: inline-block;

    padding: 18px 35px;

    border-radius: 20px;

    font-size: 34px;

    font-weight: 700;

    margin-bottom: 30px;
}

.low {

    background: #DCFCE7;

    color: #16A34A;
}

.medium {

    background: #FEF3C7;

    color: #D97706;
}

.high {

    background: #FEE2E2;

    color: #DC2626;
}

.message-box {

    background: #F8FAFC;

    border: 1px solid #CBD5E1;

    border-radius: 20px;

    padding: 25px;

    width: 60%;

    margin: auto;

    font-size: 22px;

    color: #475569;
}

.stButton > button {

    width: 100%;

    height: 65px;

    border-radius: 18px;

    border: none;

    background: linear-gradient(
        90deg,
        #2563EB,
        #38BDF8
    );

    color: white;

    font-size: 24px;

    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div style="
background:white;
padding:35px 50px;
border-radius:30px;
box-shadow:0px 10px 30px rgba(0,0,0,0.05);
border:1px solid #E2E8F0;
margin-bottom:30px;
text-align:center;
">

<div style="
font-size:42px;
font-weight:800;
color:#0F172A;
margin-bottom:10px;
">

📱 AI-Powered Mobile Addiction Risk Prediction

</div>

<div style="
font-size:18px;
color:#64748B;
">

Predict Daily Screen Time & Digital Addiction Risk

</div>

</div>

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        10,
        60,
        26
    )

    gender = st.selectbox(
        "Gender",
        [0, 1],
        format_func=lambda x:
        "Female" if x == 0 else "Male"
    )

    app_usage_time = st.number_input(
        "Daily App Usage Time (Hours)",
        0.0,
        15.0,
        4.0
    )

    number_of_apps_installed = st.number_input(
        "Installed Apps",
        1,
        300,
        80
    )

    battery_drain = st.number_input(
        "Battery Drain (%)",
        0.0,
        100.0,
        30.0
    )

    data_usage = st.number_input(
        "Data Usage (GB)",
        0.0,
        20.0,
        3.0
    )

with col2:

    sleep_hours = st.number_input(
        "Sleep Hours",
        0.0,
        12.0,
        7.0
    )

    notifications = st.number_input(
        "Daily Notifications",
        0,
        300,
        100
    )

    social_media_usage = st.number_input(
        "Social Media Usage (Hours)",
        0.0,
        12.0,
        3.0
    )

    gaming_time = st.number_input(
        "Gaming Time (Hours)",
        0.0,
        12.0,
        2.0
    )

    study_work_time = st.number_input(
        "Study / Work Time (Hours)",
        0.0,
        15.0,
        6.0
    )

    weekend_usage = st.number_input(
        "Weekend Usage (Hours)",
        0.0,
        20.0,
        6.0
    )

predict_button = st.button(
    "Predict Addiction Risk",
    use_container_width=True
)

if predict_button:

    payload = {

        "age": age,

        "gender": gender,

        "app_usage_time": app_usage_time,

        "number_of_apps_installed":
            number_of_apps_installed,

        "battery_drain":
            battery_drain,

        "data_usage":
            data_usage,

        "sleep_hours":
            sleep_hours,

        "notifications":
            notifications,

        "social_media_usage":
            social_media_usage,

        "gaming_time":
            gaming_time,

        "study_work_time":
            study_work_time,

        "weekend_usage":
            weekend_usage
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        if "error" in result:

            st.error(result["error"])

        else:

            predicted_time = result[
                "predicted_screen_time_hours"
            ]

            risk = result[
                "risk_level"
            ]

            message = result[
                "wellness_message"
            ]

            if risk == "Low Risk":

                risk_class = "low"

            elif risk == "Medium Risk":

                risk_class = "medium"

            else:

                risk_class = "high"

            st.markdown(f"""

<div class="result-card">

<h1 style="
font-size:70px;
font-weight:800;
color:#0F172A;
">
Prediction Result
</h1>

<p style="
font-size:24px;
color:#64748B;
">
Predicted Daily Screen Time
</p>

<div class="metric-box">

<span class="metric-text {risk_class}-text">
{predicted_time}
</span>

<span class="metric-hours {risk_class}-text">
Hours
</span>

</div>

<div class="risk-box {risk_class}">
{risk}
</div>

<div class="message-box">
{message}
</div>

</div>

""", unsafe_allow_html=True)

    except Exception as e:

        st.error(
            f"Error Connecting FastAPI Server : {e}"
        )
