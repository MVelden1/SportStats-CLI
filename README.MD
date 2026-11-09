# SportStats CLI

A command-line app for viewing and analysing your Strava running activities, straight from the terminal. It connects to the Strava API with OAuth2, refreshes the access token automatically and presents your data in formatted tables.

> The user interface of the app is in Dutch.

## Features

- **Recent activities:** view your last 10 activities with name, distance, time and pace
- **Filters:** narrow down activities by period (7, 30 or 90 days, or this year), minimum distance and minimum pace
- **Week comparison:** compare the last 4 weeks on number of activities, total distance, total time and average pace
- **Race time predictions:** enter a recent result for 5K, 10K, half marathon or marathon and get predicted times and paces for the other distances (based on Riegel's formula)

## Tech stack

| Package | Used for |
|---|---|
| `requests` | HTTP calls to the Strava API |
| `python-dotenv` | Loading credentials from `.env` |
| `rich` | Formatted tables and panels in the terminal |
| `questionary` | Interactive menus |

## Requirements

- Python 3.10+
- A Strava account with an API application

## Installation

```bash
git clone https://github.com/MVelden1/SportStats-CLI.git
cd SportStats-CLI

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

## Configuration

### 1. Create a Strava API application

1. Go to [strava.com/settings/api](https://www.strava.com/settings/api) and create an application.
2. Note your **Client ID** and **Client Secret**.
3. Obtain a **refresh token** once, with the `activity:read_all` scope.

### 2. Create a `.env` file

Copy `.env.example` to `.env` in the project root and fill in your credentials:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

### 3. Create `utils/tokens.json`

```json
{
    "access_token": "your_access_token",
    "refresh_token": "your_refresh_token",
    "expires_at": 0
}
```

Setting `expires_at` to `0` makes the app refresh the access token on first start. After that the file is updated automatically.

## Usage

```bash
python main.py
```

The app connects to Strava, refreshes the token if needed and opens the main menu.

## Project structure

```
SportStats-CLI/
├── api/
│   └── strava_api.py              # Strava API calls (athlete, activities)
├── logic/
│   ├── compare.py                 # Compare the last 4 weeks
│   ├── filters.py                 # Filter activities
│   ├── help.py                    # Help information
│   ├── open_last_10_activities.py # Table of recent activities
│   ├── performances.py            # Race time predictions
│   └── welcome.py                 # Welcome message
├── utils/
│   ├── auth.py                    # OAuth2 token handling and refresh
│   ├── constants.py               # API endpoints and constants
│   ├── io_handler.py              # Reading and writing JSON
│   ├── tables.py                  # Shared table output
│   └── time_utils.py              # Time conversions and pace calculations
├── test/                          # API tests and HTTP requests
├── main.py                        # Entry point
├── menu.py                        # Main menu
└── requirements.txt
```

## Roadmap

- [x] Recent activities overview
- [x] Filter by period, distance and pace
- [x] Compare weeks
- [x] Race time predictions
- [ ] Charts showing progress over time
