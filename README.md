# 🚀 fastApi-Fundamentals

Welcome to my FastAPI playground where I took my first spin with FastAPI and went from `uvicorn` confusion to full-blown route domination.

## 📚 What I Learned

This repo contains my hands-on experiments and learnings from the world of FastAPI. Here’s a breakdown of my FastAPI road trip:

---

### 🛠️ Setup & Environment
- Created and activated a **virtual environment** using `venv`
- Installed required dependencies:
  ```bash
  pip install fastapi uvicorn
  ```
  
Ran the server using:

```bash
Copy
Edit
uvicorn main:app --reload
```

# 🏗️ FastAPI Core Concepts Covered :
Concept	Description:

-> FastAPI()	Initializing the app
-> @app.get, .post	Declaring API routes
-> BaseModel class	Pydantic models for data validation
-> Path and Query	Handling path & query parameters
-> Swagger UI	Auto-generated docs at /docs
-> ReDoc	Alternative docs at /redoc

# 📬 HTTP Methods Implemented
1.) GET / → Welcome route

2.) GET /get-items/{item_id} → Path param demo

3.) GET /get-by-name?name=Milk → Query param demo

4.) POST /create-item/{item_id} → Create new item via body

5.) PUT /update-item/{item_id} → Update item data

6.) DELETE /delete-item/{item_id} → Delete an item

# 🔬 Testing via Swagger
Visit: http://127.0.0.1:8000/docs

-> Interactive UI for testing all endpoints
-> Model validation + auto schema generation

📦 Sample Data Used
python
```bash
Copy
Edit
inventory = {
  1: {"name": "Milk", "price": 3.99, "brand": "Regular"}
}

MSIT = {
  1: {"Name": "Nevin Bali", "SGPA": 9.847}
}
```

