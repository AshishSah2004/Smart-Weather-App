# 🌦️ Smart Weather App

> A simple and interactive weather forecasting web application built with Python, Streamlit and the Open-Meteo API.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![API](https://img.shields.io/badge/API-Open--Meteo-green)

---

## 👨‍💻 Developed By

**Ashish Sah**

B.Tech CSE (AI & ML)

Techno Main Salt Lake

---

## 📌 Project Overview

Smart Weather App is a web-based application that allows users to search for any city and view its current weather conditions along with a 5-day forecast.

The application uses the Open-Meteo Geocoding API to find the location coordinates and the Open-Meteo Forecast API to retrieve weather information.

---

## ✨ Features

- 🏙️ City Search
- 🌡️ Current Temperature
- 🥵 Feels-Like Temperature
- 💧 Humidity
- 💨 Wind Speed
- ☀️ Weather Condition
- 🌅 Sunrise & Sunset
- 📅 5-Day Forecast
- 🌧️ Rain Probability
- 🔄 Celsius / Fahrenheit
- ⚠️ Error Handling
- ⏳ Loading Indicator

---

## 🔄 How It Works

```text
User enters city
        ↓
Geocoding API
        ↓
Latitude + Longitude
        ↓
Weather Forecast API
        ↓
Current Weather + 5-Day Forecast
        ↓
Streamlit Interface
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Requests
- Open-Meteo API
- REST API
- HTML/CSS styling

---

## 📂 Project Structure

```text
Smart-Weather-App/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AshishSah2004/Smart-Weather-App.git
```

Move into the project:

```bash
cd Smart-Weather-App
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 🌐 Live Demo

🚀 Coming soon...

---

## 🚀 Future Improvements

- 📍 Current location detection
- 🌧️ Weather alerts
- 🗺️ Weather map integration
- 📊 Weather trend charts
- 🌙 Dark/Light weather themes
- 📱 Improved mobile responsiveness

---

## 📜 License

This project is developed for educational and portfolio purposes.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.