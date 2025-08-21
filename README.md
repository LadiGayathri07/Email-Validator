# 📧 Email Validator API with MySQL

Email Validator API is a **FastAPI-based service** that validates email addresses, classifies them into categories (free, disposable, educational, corporate), and logs results into a **MySQL database** for tracking and analysis.

---

## Features
- ✅ Validate email format using regex  
- 📂 Classify emails as:
  - **Disposable** → from `disposable_domains.txt`  
  - **Free** → Gmail, Yahoo, Outlook, Hotmail  
  - **Educational** → `.edu` domains  
  - **Corporate** → all others  
- 🗄️ Store validation logs in MySQL with timestamps  
- 🧩 Interactive API docs via Swagger UI  

---

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/email-validator-sql.git
cd email-validator-sql

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Run the API
```bash
uvicorn main:app --reload
```

### Swagger Docs
Open in your browser:
```
http://127.0.0.1:8000/docs
```

### Example Request
```json
{
  "email": "test@gmail.com"
}
```

### Example Response
```json
{
  "valid": true,
  "domain": "gmail.com",
  "type": "free"
}
```

---

## Database Setup

### Create Database & Table
Run the following in MySQL:

```sql
CREATE DATABASE email_db;

USE email_db;

CREATE TABLE email_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    domain VARCHAR(255),
    type VARCHAR(50),
    is_valid BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Update Connection Settings
Edit `main.py` to update MySQL credentials if needed:
```python
host="localhost",
user="root",
password="root",
database="email_db"
```

---

## Project Structure
```
email-validator-sql/
│── disposable_domains.txt   # List of disposable email domains
│── main.py                  # FastAPI app
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── .venv/                   # Virtual environment (optional, ignored in git)
```

---

## Requirements
- Python 3.8+  
- FastAPI  
- Uvicorn  
- MySQL Connector  
- Pydantic  

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Future Work
- Add email validation via MX records lookup  
- Add support for bulk email validation  
- Add analytics dashboard for email statistics  

---

## License
MIT License

---

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)  
- [MySQL](https://www.mysql.com/)  
- [Pydantic](https://docs.pydantic.dev/)  
- [Uvicorn](https://www.uvicorn.org/)  
