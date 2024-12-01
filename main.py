import streamlit as  st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for next Days")
place= st.text_input("Place:- ")
days = st.slider("Forecast Days:-", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
options = st.selectbox("Select Data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days, options)
    try:
        if options == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperature, labels={"x":"Date","y":"Temp"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear":"sky/clear.png","Clouds":"sky/Cloud.png",
                      "Snow":"sky/Snow.png", "Rain":"sky/Rain.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width = 125)
    except KeyError:
        st.write("This Place does not Exist")

