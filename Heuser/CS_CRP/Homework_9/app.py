from pathlib import Path
from urllib.parse import quote
import requests
from flask import Flask, jsonify, redirect, render_template_string, request, send_from_directory, url_for

app = Flask(__name__)
BASE = Path(__file__).resolve().parent
GAME_DIR = BASE / "game"
PORTFOLIO_DIR = BASE / "portfolio"
HOME_DIR = BASE / "home"
API_DIR = BASE / "api"

HOME_PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Homework 9 | Heuser College</title>
  <style>
    *{box-sizing:border-box}body{margin:0;min-height:100vh;background:#0b1730;color:#f4f7ff;font-family:Arial,sans-serif;display:grid;place-items:center;padding:24px}
    main{width:min(900px,100%);text-align:center}small{color:#9dc9ed;letter-spacing:.18em;font-weight:bold}h1{font-size:clamp(42px,8vw,76px);margin:18px 0 12px}p{color:#b8c6dc;line-height:1.7}
    .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-top:38px;text-align:left}
    a{display:block;padding:25px;border:1px solid #34506f;border-radius:14px;background:#122544;color:white;text-decoration:none;transition:.2s}
    a:hover{transform:translateY(-4px);border-color:#9dc9ed;background:#183354}a strong{display:block;font-size:20px;margin-bottom:10px}a span{color:#b8c6dc;font-size:14px;line-height:1.5}
    footer{margin-top:42px;color:#8196b2;font-size:12px}
  </style>
</head>
<body><main>
  <small>HEUSER COLLEGE · COMPUTER SCIENCE</small>
  <h1>Homework 9</h1>
  <p>Welcome to my web server. Choose a project below to explore.</p>
  <section class="cards">
    <a href="/game"><strong>🎮 Homework 6 · Game / Project</strong><span>Open my existing Homework 6 website.</span></a>
    <a href="/portfolio"><strong>✦ Homework 8 · Portfolio</strong><span>Explore my Asterfall portfolio project.</span></a>
    <a href="/api"><strong>📚 Book Discovery API</strong><span>Search books using the Open Library public API.</span></a>
  </section>
  <footer>Built with Python, Flask and Render · Anush Heuser</footer>
</main></body></html>
"""

API_PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Book Discovery | Homework 9</title>
<style>
*{box-sizing:border-box}body{margin:0;padding:32px 18px;background:#eef4fa;color:#142b45;font-family:Arial,sans-serif}
main{max-width:850px;margin:35px auto}a{color:#245d91}h1{font-size:clamp(34px,7vw,54px);margin:12px 0}
p{line-height:1.6;color:#53677c}.search{display:flex;gap:10px;margin:25px 0}.search input{flex:1;min-width:0;padding:14px;border:1px solid #b9c9d8;border-radius:8px;font-size:16px}
button{padding:14px 20px;border:0;border-radius:8px;background:#173d64;color:white;font-weight:bold;cursor:pointer}
#results{display:grid;gap:12px}.book{padding:17px;background:white;border:1px solid #d5e0e9;border-radius:10px}.book h2{font-size:18px;margin:0 0 7px}.muted{font-size:13px;color:#6b7f91}
@media(max-width:520px){.search{flex-direction:column}}
</style></head>
<body><main>
<a href="/">← Back to Homework 9 home</a>
<p>PUBLIC API PROJECT · OPEN LIBRARY</p><h1>Book Discovery Deck</h1>
<p>Search the Open Library catalogue. Enter a title, author or subject to discover books.</p>
<form class="search" id="search-form"><input id="query" name="q" placeholder="Try: Harry Potter, science, history..." required><button>Search books</button></form>
<p id="status" aria-live="polite"></p><section id="results"></section>
<script>
const form=document.querySelector('#search-form'), query=document.querySelector('#query'), status=document.querySelector('#status'), results=document.querySelector('#results');
form.addEventListener('submit',async event=>{
 event.preventDefault(); const term=query.value.trim(); if(!term)return;
 status.textContent='Searching the Open Library catalogue…'; results.innerHTML='';
 try{
  const response=await fetch('/api/search?q='+encodeURIComponent(term));
  const data=await response.json(); if(!response.ok)throw new Error(data.error||'Search failed');
  if(!data.books.length){status.textContent='No books found. Try another search.';return}
  status.textContent='Found '+data.books.length+' results.';
  data.books.forEach(book=>{
   const article=document.createElement('article');article.className='book';
   const title=document.createElement('h2');title.textContent=book.title;
   const author=document.createElement('p');author.className='muted';author.textContent='Author: '+(book.author||'Not listed')+' · First published: '+(book.year||'Unknown');
   article.append(title,author);
   if(book.url){const link=document.createElement('a');link.href=book.url;link.target='_blank';link.rel='noopener noreferrer';link.textContent='View on Open Library';article.append(link)}
   results.append(article);
  });
 }catch(error){status.textContent='Sorry, the search is unavailable right now. Please try again.';}
});
</script></main></body></html>
"""

@app.get("/")
def home():
    return send_from_directory(HOME_DIR, "index.html")

@app.get("/game")
def game_redirect():
    return redirect("/game/")

@app.get("/game/")
def game():
    return send_from_directory(GAME_DIR, "index.html")

@app.get("/game/<path:filename>")
def game_assets(filename):
    return send_from_directory(GAME_DIR, filename)

@app.get("/portfolio")
def portfolio_redirect():
    return redirect("/portfolio/")

@app.get("/portfolio/")
def portfolio():
    return send_from_directory(PORTFOLIO_DIR, "index.html")

@app.get("/portfolio/<path:filename>")
def portfolio_assets(filename):
    return send_from_directory(PORTFOLIO_DIR, filename)

@app.get("/api")
def api_page():
    return send_from_directory(API_DIR, "index.html")

@app.get("/api/search")
def api_search():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"error": "Please enter a search term.", "books": []}), 400
    try:
        response = requests.get(
            "https://openlibrary.org/search.json",
            params={"q": query, "limit": 8},
            timeout=12,
            headers={"User-Agent": "HeuserHomework9/1.0"}
        )
        response.raise_for_status()
        docs = response.json().get("docs", [])
        books = [{
            "title": item.get("title", "Untitled"),
            "author": ", ".join(item.get("author_name", [])[:2]),
            "year": item.get("first_publish_year"),
            "url": "https://openlibrary.org" + item["key"] if item.get("key") else None
        } for item in docs]
        return jsonify({"source": "Open Library", "count": len(books), "books": books})
    except requests.RequestException:
        return jsonify({"error": "The book service could not be reached.", "books": []}), 502
    except ValueError:
        return jsonify({"error": "The book service returned an invalid response.", "books": []}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)))
