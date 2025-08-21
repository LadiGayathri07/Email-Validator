from fastapi import FastAPI
from pydantic import BaseModel
import re
import mysql.connector

app = FastAPI(title="Email Validator API with MySQL")

# === MySQL Connection ===
def get_db_connection(): 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="email_db"
    )

# === Load Disposable Domains ===
with open("disposable_domains.txt") as f:
    disposable_domains = set(f.read().splitlines())

FREE_EMAILS = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com"}

# === Pydantic Model ===
class EmailRequest(BaseModel):
    email: str

# === Email Type Logic ===
def get_email_type(domain):
    if domain in disposable_domains:
        return "disposable"
    elif domain in FREE_EMAILS:
        return "free"
    elif domain.endswith(".edu"):
        return "educational"
    else:
        return "corporate"

# === API Endpoint ===
@app.post("/validate")
def validate_email(data: EmailRequest):
    email = data.email.lower()
    match = re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", email)

    is_valid = bool(match)
    if not is_valid:
        return {"valid": False, "reason": "Invalid format"}

    domain = email.split('@')[1]
    email_type = get_email_type(domain)

    # Log to MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO email_logs (email, domain, type, is_valid)
        VALUES (%s, %s, %s, %s)
    """, (email, domain, email_type, True))
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "valid": True,
        "domain": domain,
        "type": email_type
    }
