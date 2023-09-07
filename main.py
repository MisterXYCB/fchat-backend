from flask import Flask, jsonify, render_template, request, send_from_directory, redirect, url_for
from classes import *
from dataclasses import dataclass
import os
import time
import csv
import sqlite3
import requests
import hashlib
from typing import TypedDict, List, Dict, Union

app = Flask(__name__)
connection = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT,
        session_token TEXT,
        session_token_expiry INTEGER,
        last_online INTEGER,
        chat_ids TEXT
    )""")

connection.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/create", methods=["POST"])
def create_user():
    return User().create(request.form.get("username"), request.form.get("email"), request.form.get("password"))
    
@app.route("/user/login", methods=["POST"])
def login_user():
    return User().login(request.form.get("email"), request.form.get("password"), request.form.get("session_token"))
    
#run without multithreading
app.run(host="0.0.0.0", port=80, threaded=False)