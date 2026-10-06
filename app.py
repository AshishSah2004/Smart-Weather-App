import streamlit as st
import requests
from datetime import datetime


# -----------------------------
# Page Setup
# -----------------------------

st.set_page_config(
    page_title="Smart Weather App",
    page_icon="🌦️",
    layout="centered"
)


# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>
    .weather-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #1f2937;
        margin-bottom: 20px;
    }

    .developer {
        text-align: center;
        color: #888888;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------

st.title("🌦️ Smart Weather App")

st.write(
    "Get current weather and a 5-day forecast for any city."
)


# -----------------------------
# Weather Condition
# -----------------------------

def get_weather_condition(code):

    conditions = {
        0: ("☀️", "Clear Sky"),
        1: ("🌤️", "Mainly Clear"),
        2: ("⛅", "Partly Cloudy"),
        3: ("☁️", "Overcast"),
        45: ("🌫️", "Fog"),
        48: ("🌫️", "Fog"),
        51: ("🌦️", "Light Drizzle"),
        53: ("🌦️", "Moderate Drizzle"),
        55: ("🌧️", "Dense Drizzle"),
        61: ("🌧️", "Light Rain"),
        63: ("🌧️", "Moderate Rain"),
        65: ("🌧️", "Heavy Rain"),
        71: ("❄️", "Light Snow"),
        73: ("❄️", "Moderate Snow"),
        75: ("❄️", "Heavy Snow"),
        80: ("🌦️", "Rain Showers"),
        81: ("🌧️", "Rain Showers"),
        82: ("⛈️", "Heavy Rain Showers"),
        95: ("⛈️", "Thunderstorm"),
        96: ("⛈️", "Thunderstorm with Hail"),
        99: ("⛈️", "Heavy Thunderstorm")
    }

    return conditions.get(code, ("🌡️", "Unknown"))


# -----------------------------
# User Input
# -----------------------------

city = st.text_input(
    "🏙️ Enter City Name",
    placeholder="Example: Kolkata"
)

unit = st.selectbox(
    "🌡️ Temperature Unit",
    ["Celsius (°C)", "Fahrenheit (°F)"]
)


# -----------------------------
# Weather Button
# -----------------------------

if st.button("🔍 Get Weather"):

    if not city:
        st.warning("Please enter a city name.")

    else:

        try:

            # -----------------------------
            # Find City Coordinates
            # -----------------------------

            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search"
            )

            geo_params = {
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            }

            geo_response = requests.get(
                geo_url,
                params=geo_params,
                timeout=10
            )

            geo_response.raise_for_status()

            geo_data = geo_response.json()

            results = geo_data.get("results")

            if not results:

                st.error(
                    "❌ City not found. Please check the city name."
                )

            else:

                latitude = results[0]["latitude"]
                longitude = results[0]["longitude"]

                location_name = results[0]["name"]
                country = results[0]["country"]

                # -----------------------------
                # Temperature Unit
                # -----------------------------

                if unit == "Celsius (°C)":
                    temperature_unit = "celsius"
                    symbol = "°C"
                else:
                    temperature_unit = "fahrenheit"
                    symbol = "°F"

                # -----------------------------
                # Weather API
                # -----------------------------

                weather_url = (
                    "https://api.open-meteo.com/v1/forecast"
                )

                weather_params = {
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": (
                        "temperature_2m,"
                        "apparent_temperature,"
                        "relative_humidity_2m,"
                        "wind_speed_10m,"
                        "weather_code"
                    ),
                    "daily": (
                        "weather_code,"
                        "temperature_2m_max,"
                        "temperature_2m_min,"
                        "precipitation_probability_max,"
                        "sunrise,"
                        "sunset"
                    ),
                    "forecast_days": 5,
                    "temperature_unit": temperature_unit,
                    "timezone": "auto"
                }

                with st.spinner("Getting latest weather data..."):

                    weather_response = requests.get(
                        weather_url,
                        params=weather_params,
                        timeout=10
                    )

                weather_response.raise_for_status()

                weather_data = weather_response.json()

                # -----------------------------
                # Current Weather
                # -----------------------------

                current = weather_data["current"]

                temperature = current["temperature_2m"]
                feels_like = current["apparent_temperature"]
                humidity = current["relative_humidity_2m"]
                wind_speed = current["wind_speed_10m"]
                weather_code = current["weather_code"]

                emoji, condition = get_weather_condition(
                    weather_code
                )

                # -----------------------------
                # Location Card
                # -----------------------------

                st.success(
                    f"📍 {location_name}, {country}"
                )

                st.subheader(
                    f"{emoji} {condition}"
                )

                # -----------------------------
                # Main Weather Metrics
                # -----------------------------

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Temperature",
                        f"{temperature} {symbol}"
                    )

                with col2:
                    st.metric(
                        "Feels Like",
                        f"{feels_like} {symbol}"
                    )

                with col3:
                    st.metric(
                        "Humidity",
                        f"{humidity}%"
                    )

                with col4:
                    st.metric(
                        "Wind Speed",
                        f"{wind_speed} km/h"
                    )

                # -----------------------------
                # Sunrise & Sunset
                # -----------------------------

                daily = weather_data["daily"]

                sunrise = datetime.fromisoformat(
                    daily["sunrise"][0]
                )

                sunset = datetime.fromisoformat(
                    daily["sunset"][0]
                )

                st.subheader("🌅 Sun Information")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Sunrise",
                        sunrise.strftime("%I:%M %p")
                    )

                with col2:
                    st.metric(
                        "Sunset",
                        sunset.strftime("%I:%M %p")
                    )

                # -----------------------------
                # Last Updated
                # -----------------------------

                updated_time = current["time"]

                st.caption(
                    f"🕒 Weather data updated: {updated_time}"
                )

                # -----------------------------
                # 5-Day Forecast
                # -----------------------------

                st.subheader("📅 5-Day Forecast")

                forecast_columns = st.columns(5)

                for i in range(5):

                    date = datetime.fromisoformat(
                        daily["time"][i]
                    )

                    day_name = date.strftime("%a")

                    max_temp = daily[
                        "temperature_2m_max"
                    ][i]

                    min_temp = daily[
                        "temperature_2m_min"
                    ][i]

                    rain_probability = daily[
                        "precipitation_probability_max"
                    ][i]

                    daily_code = daily[
                        "weather_code"
                    ][i]

                    daily_emoji, daily_condition = (
                        get_weather_condition(daily_code)
                    )

                    with forecast_columns[i]:

                        st.markdown(
                            f"### {day_name}"
                        )

                        st.write(
                            f"{daily_emoji} "
                            f"{daily_condition}"
                        )

                        st.write(
                            f"🌡️ {min_temp}{symbol}"
                        )

                        st.write(
                            f"↕️ {max_temp}{symbol}"
                        )

                        st.write(
                            f"🌧️ {rain_probability}%"
                        )

        except requests.RequestException:

            st.error(
                "⚠️ Unable to connect to the weather service."
            )

        except Exception:

            st.error(
                "⚠️ Something went wrong. Please try again."
            )


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="developer">
        👨‍💻 Developed by <b>Ashish Sah</b><br>
        AI & Machine Learning Project • Python • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)