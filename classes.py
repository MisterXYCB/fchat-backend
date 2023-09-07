from flask import Response, jsonify
import sqlite3
import uuid
import time
import json
from typing import TypedDict, List, Dict, Union

connection = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = connection.cursor()

class User:
    def __init__(self) -> None:
        pass

    def create(self, username: str, email: str, password: str) -> Response:

        if username is None or email is None or password is None:
            return jsonify({"success": False, "message": "Missing arguments"}), 400

        cursor.execute("SELECT * FROM users WHERE email=:email", {"email": email})
        if cursor.fetchone() is not None:
            return jsonify({"success": False, "message": "User already exists"}), 400

        session_token = str(uuid.uuid4())

        cursor.execute("INSERT INTO users (username, email, password, session_token, session_token_expiry, last_online, chat_ids) VALUES (:username, :email, :password, :session_token, :session_token_expiry, :last_online, :chat_ids)", {"username": username, "email": email, "password": password, "session_token": session_token, "session_token_expiry": round(time.time() + 3600 * 24 * 28), "last_online": round(time.time()), "chat_ids": str([])})
        connection.commit()

        return jsonify({"success": True, "message": "User created", "session_token": session_token}), 201
    
    def login(self, email: str=None, password: str=None, session_token: str=None) -> Response:
        if session_token is not None:
            cursor.execute("SELECT * FROM users WHERE session_token=:session_token", {"session_token": session_token})
            print(user, time.time())
            if user is None:
                return jsonify({"success": False, "message": "User not found"}), 404
            elif user[5] > round(time.time()):
                return jsonify({"success": True, "message": "User logged in", "login_type": "session_token"}), 200
            else:
                return jsonify({"success": False, "message": "Session token expired"}), 400
        else:
            if email is None or password is None:
                return jsonify({"success": False, "message": "Missing arguments"}), 400

            cursor.execute("SELECT * FROM users WHERE email=:email", {"email": email})
            user = cursor.fetchone()
            print(user)

            if user is None:
                return jsonify({"success": False, "message": "User not found"}), 404

            if user[3] != password:
                return jsonify({"success": False, "message": "Wrong password"}), 400
            
            session_token = str(uuid.uuid4())

            if user[5] < round(time.time()):
                cursor.execute("UPDATE users SET session_token=:session_token, session_token_expiry=:session_token_expiry WHERE email=:email", {"session_token": session_token, "session_token_expiry": round(time.time() + 3600 * 24 * 28), "email": email})
                connection.commit()
            else:
                session_token = user[4]

            return jsonify({"success": True, "message": "User logged in", "login_type": "email", "session_token": session_token}), 200
