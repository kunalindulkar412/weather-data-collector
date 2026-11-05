# Weather Data Collector

> **Purpose:** This is a small practice project built to learn Python fundamentals, API integration, JSON handling, exception handling, CSV operations and Git.

A simple Python script that fetches current weather information for a given city using the Open-Meteo API and stores the results in a CSV file.

## Features

- Takes a city name as input.
- Retrieves latitude and longitude using the Open-Meteo Geocoding API.
- Fetches current temperature, relative humidity and wind speed.
- Handles common API errors, connection failures and timeouts.
- Saves weather records to `weather_data.csv`.
- Appends new records without overwriting existing data.

## Technologies Used

- Python
- Requests
- Open-Meteo API
- CSV
- python-dotenv
- Git and GitHub

## Setup and Usage

1. Clone the repository.
2. Create and activate a virtual environment.

```bash
python -m venv .venv
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run the program.

```bash
python main.py
```

5. Enter a city name to retrieve its current weather information.

The collected data is stored in `weather_data.csv`.

## APIs

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo Forecast API](https://open-meteo.com/en/docs)

No API key is required for the weather requests used in this project.