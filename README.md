# 🚀 Super Blog API

A fully modular RESTful API built with **FastAPI** and **Python 3**. 

This project was built as a 6-day challenge to master backend web development concepts including routing, data validation, middleware, and API design.

## ✨ Features
* **Modular Routing:** Separated endpoints for Users, Posts, and Comments.
* **Data Validation:** Strict type hinting and validation using Pydantic models.
* **Advanced Querying:** Filter posts by author, search by text, and paginate results using `limit` and `offset`.
* **Relationships:** Sub-resources for Tags (Many-to-Many) and Comments (One-to-Many).
* **Custom Middleware:** Includes CORS configuration and a custom `X-Process-Time` stopwatch header.
* **Environment Config:** Secure variable management using `.env` and `python-dotenv`.

## 📂 Project Structure
```text
blog-api/
├── .env
├── .gitignore
├── README.md
└── app/
    ├── config.py
    ├── main.py
    ├── routers/
    │   ├── comments.py
    │   ├── posts.py
    │   └── users.py
    └── schemas/
        ├── posts.py
        └── users.py