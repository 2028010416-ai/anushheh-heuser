# Homework 9 — Your Own Web Server on Render

This Flask project serves the existing Homework 6 and Homework 8 websites from one Python web server and adds a Book Discovery page using the free Open Library API.

## Routes

- `/` — Homework 9 home page with links to all projects.
- `/game` — existing Homework 6 website.
- `/portfolio` — existing Homework 8 Asterfall website.
- `/api` — Book Discovery page.
- `/api/search?q=... ` — backend endpoint that requests book data from Open Library and returns JSON.

## Run locally

From this folder:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Deploy on Render

1. Open Render and choose **New + → Web Service**.
2. Connect the GitHub repository `2028010416-ai/anushheh-heuser`.
3. Set **Root Directory** to `Heuser/CS_CRP/Homework_9`.
4. Set **Runtime** to Python.
5. Set **Build Command** to `pip install -r requirements.txt`.
6. Set **Start Command** to `gunicorn app:app`.
7. Choose the free instance (if available) and deploy.

The app uses Render's `PORT` environment variable automatically through Gunicorn.

## Existing project files

The app serves the original files from:
- `../Homework_6/`
- `../Homework_8/`

Keep those folders in the repository. Do not move or rename them.
