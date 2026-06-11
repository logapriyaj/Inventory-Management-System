import sqlite3

def connect():
    conn = sqlite3.connect("inventory.db")
    return conn
