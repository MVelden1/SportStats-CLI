# SportStats CLI

Een command-line applicatie waarmee je je Strava-activiteiten kunt bekijken en analyseren, rechtstreeks vanuit de terminal.

## Functies

| Functie | Status |
|---|---|
| Bekijk laatste 10 activiteiten (naam, afstand, tijd, tempo) | Beschikbaar |
| Vergelijkbare prestaties berekenen (5km, 10km, halve marathon, marathon) | Beschikbaar |
| Activiteiten filteren | In ontwikkeling |
| Weken vergelijken | In ontwikkeling |

## Vereisten

- Python 3.10+
- Een Strava-account met API-toegang

## Installatie

1. **Clone de repository**
   ```bash
   git clone <repo-url>
   cd SportStats-CLI
   ```

2. **Maak een virtual environment aan en activeer het**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Installeer de dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuratie

### Strava API instellen

1. Ga naar [strava.com/settings/api](https://www.strava.com/settings/api) en maak een nieuwe applicatie aan.
2. Noteer je **Client ID** en **Client Secret**.
3. Haal eenmalig een **refresh token** op met de juiste scopes (`activity:read_all`).

### `.env` aanmaken

Maak een `.env`-bestand aan in de root van het project:

```env
CLIENT_ID=jouw_client_id
CLIENT_SECRET=jouw_client_secret
```

### `utils/tokens.json` aanmaken

Maak het bestand `utils/tokens.json` aan met je initiële tokens:

```json
{
    "access_token": "jouw_access_token",
    "refresh_token": "jouw_refresh_token",
    "expires_at": 0
}
```

Zet `expires_at` op `0` zodat het access token direct ververst wordt bij de eerste start.

## Gebruik

```bash
python main.py
```

De applicatie verbindt automatisch met de Strava API, vernieuwt het access token indien nodig en toont het hoofdmenu.

## Projectstructuur

```
SportStats CLI/
├── api/
│   ├── __init__.py          # Exporteert API-functies
│   └── strava_api.py        # Strava API-aanroepen (athlete, activities)
├── logic/
│   ├── compare.py           # Weken vergelijken (in ontwikkeling)
│   ├── filters.py           # Activiteiten filteren (in ontwikkeling)
│   ├── help.py              # Help-informatie
│   ├── open_last_10_activities.py  # Tabel met laatste activiteiten
│   ├── performances.py      # Voorspelde racetijden berekenen
│   └── welcome.py           # Welkomstbericht
├── utils/
│   ├── auth.py              # OAuth2 token beheer en vernieuwen
│   ├── constants.py         # API-endpoints en constanten
│   ├── io_handler.py        # JSON lezen/schrijven
│   ├── time_utils.py        # Tijdconversies en tempoberekeningen
│   └── tokens.json          # Lokaal opgeslagen tokens (niet in git)
├── .env                     # API-credentials (niet in git)
├── main.py                  # Entrypoint
├── menu.py                  # Hoofdmenu
└── requirements.txt
```

## Dependencies

| Package | Gebruik |
|---|---|
| `requests` | HTTP-aanroepen naar de Strava API |
| `python-dotenv` | Laden van `.env`-variabelen |
| `rich` | Opgemaakte tabellen en panelen in de terminal |
| `questionary` | Interactieve menu's |

## Roadmap

- [ ] Activiteiten filteren op type, datum of afstand
- [ ] Weken onderling vergelijken
- [ ] Grafieken van voortgang over tijd