# Homework 9 — Your Own Web Server on Render

This project uses Python Flask to serve the copied Homework 6 game and Homework 8 portfolio, plus a Book Discovery page powered by the free Open Library API.

## Project structure

- `app.py` — Flask web server and backend API
- `requirements.txt` — Python dependencies
- `home/index.html` — main landing page
- `game/` — copied Homework 6 project
- `portfolio/` — copied Homework 8 project
- `api/index.html` — Book Discovery interface

## Routes

- `/` — main home page
- `/game/` — Homework 6 game
- `/portfolio/` — Homework 8 portfolio
- `/api` — Book Discovery page
- `/api/search?q=... ` — JSON endpoint that searches Open Library

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Deploy on Render

1. Open Render and choose **New + → Web Service**.
2. Connect GitHub repository `2028010416-ai/anushheh-heuser`.
3. Set **Root Directory** to `Heuser/CS_CRP/Homework_9`.
4. Choose **Python** as the runtime.
5. Set **Build Command** to `pip install -r requirements.txt`.
6. Set **Start Command** to `gunicorn app:app`.
7. Choose an available free instance and deploy.

Render provides the port automatically; Gunicorn listens on it.

Keep the original Homework 6 and Homework 8 folders in the repository. Their copies are included here under `game/` and `portfolio/`.
