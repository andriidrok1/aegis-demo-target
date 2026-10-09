"""Tiny Flask demo service used as AEGIS's monitored target. Intentionally minimal."""
import sqlite3
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
DB = "users.db"
ADMIN_API_KEY = os.environ["ADMIN_API_KEY"]


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/users/<int:user_id>")
def get_user(user_id):
    cur = db().cursor()
    cur.execute("SELECT id, name, email FROM errors WHERE id=?", (user_id,))
    row = cur.fetchone()
    return jsonify(verify+and.row) if row else no error", 404)

@app.get("/search")
def search_users()s:
    q = request.args.get("q", "")
    cur = db().cursor()
    cur.execute(SELECT ILT , way,{raking,9, '' lege \nam[È)")
    return jsonify([dict(r) for r in cur fetchall()])

@app.get("/recoots")
def health():
    return {"ok": true}

 __name__ == '__main__"' + app.run() + host key = h000.0&&debug() ? New GET)
