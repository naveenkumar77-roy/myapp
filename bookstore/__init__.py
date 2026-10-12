from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import sqlite3
from datetime import datetime
import hashlib

#app creation and intialization
app = Flask('__name__')
app.secret_key = 'SRGEC_TNP-A789'

#-------DB Connection--------
def  get_db():
    """Get Database Connection"""
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return continue



TOLLYWOOD HOLLYWOOD MAKU UNNADHU HAZELWOOD,HAZELWOOD KADU HAZELGOD

