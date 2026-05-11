# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib
#
# app = FastAPI(
#     title="AI-Powered Mobile Addiction Risk Prediction API",
#     description="Predict Daily Screen Time and Addiction Risk",
#     version="1.0"
# )
#
# model = joblib.load("best_model.pkl")
#
#
# class UserInput(BaseModel):
#
#     age: int
#
#     gender: int
#
#     app_usage_time: float
#
#     number_of_apps_installed: int
#
#     battery_drain: float
#
#     data_usage: float
#
#     user_behavior_class: int
#
#     sleep_hours: float
#
#     notifications: int
#
#     social_media_usage: float
#
#     gaming_time: float
#
#     study_work_time: float
#
#     weekend_usage: float
#
#     weekday_usage: float
#
#     battery_cycles: int
#
#     device_age: float
#
#     internet_type: int
#
#     location_type: int
#
#     high_usage_flag: int
#
#     heavy_gamer: int
#
#
# def get_risk_level(screen_time):
#
#     if screen_time <= 3:
#
#         return "Low Risk"
#
#     elif screen_time <= 7:
#
#         return "Medium Risk"
#
#     else:
#
#         return "High Addiction Risk"
#
#
# def get_wellness_message(risk):
#
#     if risk == "Low Risk":
#
#         return (
#             "Healthy mobile usage detected. "
#             "Maintain your current digital habits."
#         )
#
#     elif risk == "Medium Risk":
#
#         return (
#             "Moderate mobile dependency detected. "
#             "Try reducing unnecessary screen exposure."
#         )
#
#     else:
#
#         return (
#             "High addiction risk detected. "
#             "Consider digital detox strategies and healthier usage patterns."
#         )
#
#
# @app.get("/")
# def home():
#
#     return {
#
#         "message":
#             "AI-Powered Mobile Addiction Risk Prediction API",
#
#         "status":
#             "Running Successfully"
#     }
#
#
# @app.post("/predict")
# def predict(data: UserInput):
#
#     data_per_hour = (
#
#         data.data_usage /
#
#         max(data.app_usage_time, 1)
#     )
#
#     battery_drain_per_hour = (
#
#         data.battery_drain /
#
#         max(data.app_usage_time, 1)
#     )
#
#     device_stress_score = (
#
#         data.notifications *
#
#         0.3 +
#
#         data.app_usage_time * 10 +
#
#         data.battery_drain * 0.5
#     )
#
#     usage_intensity = (
#
#         data.app_usage_time *
#
#         data.number_of_apps_installed
#     )
#
#     input_df = pd.DataFrame([{
#
#         'age':
#             data.age,
#
#         'gender':
#             data.gender,
#
#         'app_usage_time':
#             data.app_usage_time,
#
#         'number_of_apps_installed':
#             data.number_of_apps_installed,
#
#         'battery_drain':
#             data.battery_drain,
#
#         'data_usage':
#             data.data_usage,
#
#         'user_behavior_class':
#             data.user_behavior_class,
#
#         'sleep_hours':
#             data.sleep_hours,
#
#         'notifications':
#             data.notifications,
#
#         'social_media_usage':
#             data.social_media_usage,
#
#         'gaming_time':
#             data.gaming_time,
#
#         'study_work_time':
#             data.study_work_time,
#
#         'weekend_usage':
#             data.weekend_usage,
#
#         'weekday_usage':
#             data.weekday_usage,
#
#         'battery_cycles':
#             data.battery_cycles,
#
#         'device_age':
#             data.device_age,
#
#         'internet_type':
#             data.internet_type,
#
#         'location_type':
#             data.location_type,
#
#         'data_per_hour':
#             data_per_hour,
#
#         'battery_drain_per_hour':
#             battery_drain_per_hour,
#
#         'device_stress_score':
#             device_stress_score,
#
#         'usage_intensity':
#             usage_intensity,
#
#         'high_usage_flag':
#             data.high_usage_flag,
#
#         'heavy_gamer':
#             data.heavy_gamer
#     }])
#
#     try:
#
#         prediction = model.predict(input_df)[0]
#
#         risk = get_risk_level(prediction)
#
#         wellness_message = get_wellness_message(risk)
#
#         return {
#
#             "predicted_screen_time_hours":
#                 round(float(prediction), 2),
#
#             "risk_level":
#                 risk,
#
#             "wellness_message":
#                 wellness_message
#         }
#
#     except Exception as e:
#
#         print("\nMODEL ERROR\n")
#
#         print(e)
#
#         return {
#             "error": str(e)
#         }




from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(

    title="AI-Powered Mobile Addiction Risk Prediction API",

    description="Predict Daily Screen Time and Addiction Risk",

    version="1.0"
)

model = joblib.load("best_model.pkl")


class UserInput(BaseModel):

    age: int

    gender: int

    app_usage_time: float

    number_of_apps_installed: int

    battery_drain: float

    data_usage: float

    sleep_hours: float

    notifications: int

    social_media_usage: float

    gaming_time: float

    study_work_time: float

    weekend_usage: float


def get_risk_level(screen_time):

    if screen_time <= 5:

        return "Low Risk"

    elif screen_time <= 8:

        return "Medium Risk"

    else:

        return "High Addiction Risk"


def get_wellness_message(risk):

    if risk == "Low Risk":

        return (

            "Healthy mobile usage detected. "

            "Maintain your current digital habits."
        )

    elif risk == "Medium Risk":

        return (

            "Moderate mobile dependency detected. "

            "Try reducing unnecessary screen exposure."
        )

    else:

        return (

            "High addiction risk detected. "

            "Consider digital detox strategies and healthier usage patterns."
        )


@app.get("/")
def home():

    return {

        "message":
            "AI-Powered Mobile Addiction Risk Prediction API",

        "status":
            "Running Successfully"
    }


@app.post("/predict")
def predict(data: UserInput):

    data_per_hour = (

        data.data_usage /

        max(data.app_usage_time, 1)
    )

    battery_drain_per_hour = (

        data.battery_drain /

        max(data.app_usage_time, 1)
    )

    device_stress_score = (

        data.notifications * 0.3 +

        data.app_usage_time * 10 +

        data.battery_drain * 0.5
    )

    heavy_gamer = (

        1 if data.gaming_time >= 4

        else 0
    )

    input_df = pd.DataFrame([{

        'age':
            data.age,

        'gender':
            data.gender,

        'app_usage_time':
            data.app_usage_time,

        'number_of_apps_installed':
            data.number_of_apps_installed,

        'battery_drain':
            data.battery_drain,

        'data_usage':
            data.data_usage,

        'sleep_hours':
            data.sleep_hours,

        'notifications':
            data.notifications,

        'social_media_usage':
            data.social_media_usage,

        'gaming_time':
            data.gaming_time,

        'study_work_time':
            data.study_work_time,

        'weekend_usage':
            data.weekend_usage,

        'data_per_hour':
            data_per_hour,

        'battery_drain_per_hour':
            battery_drain_per_hour,

        'device_stress_score':
            device_stress_score,

        'heavy_gamer':
            heavy_gamer
    }])

    try:

        prediction = model.predict(input_df)[0]

        risk = get_risk_level(prediction)

        wellness_message = get_wellness_message(risk)

        return {

            "predicted_screen_time_hours":
                round(float(prediction), 2),

            "risk_level":
                risk,

            "wellness_message":
                wellness_message
        }

    except Exception as e:

        return {
            "error": str(e)
        }