## 🧑‍🤝‍🧑 Simple Social

Simple Social is a minimal social media–style application built with FastAPI (backend) and Streamlit (frontend).
Users can register, log in using JWT authentication, upload images/videos, and view a personalized feed.

## 🚀 Features

✅ User authentication (Register / Login) using FastAPI Users

🔐 JWT-based secure APIs

📸 Upload images & videos

🧾 Caption support

🖼️ Image & video transformations via ImageKit

🏠 Feed showing latest posts

🗑️ Owners can delete their own posts

⚡ Fully async backend with aiosqlite

## 🛠️ Tech Stack

Backend ->  FastAPI, FastAPI Users, SQLAlchemy (Async), SQLite, JWT Authentication, ImageKit (media hosting & transformations)

Frontend -> Streamlit, Requests (HTTP client)

```plaintext
📁 Project Structure
.
├── app/
│   ├── app.py              # FastAPI app & routes
│   ├── db.py               # Database / session setup
│   ├── schemas.py          # Pydantic schemas
│   ├── users.py            # FastAPI Users config
│   └── images.py           # ImageKit config
│
├── streamlit_app.py        # Streamlit frontend
├── test.db                 # SQLite database
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

1️⃣ Clone the repository
git clone https://github.com/praa532/Fast-API-Multimedia-Project.git
cd simple-social

2️⃣ Create & activate virtual environment

Windows (PowerShell):

python -m venv myvenv
. .\myvenv\Scripts\Activate.ps1


Linux / Mac:

python3 -m venv myvenv
source myvenv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file:

SECRET=your-secret-key
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/your_id

5️⃣ Run the backend (FastAPI)
uvicorn app.app:app --reload


API Docs: http://localhost:8000/docs

6️⃣ Run the frontend (Streamlit)
streamlit run streamlit_app.py


App UI: http://localhost:8501

## 🔑 Authentication Flow

User registers via /auth/register

User logs in via /auth/jwt/login

Frontend stores returned JWT token

Token is sent as:

Authorization: Bearer <access_token>


Protected endpoints validate token automatically



## 🗂️ API Endpoints Summary

```plaintext
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/jwt/login	Login user
GET	/users/me	Get current user
POST	/upload	Upload post
GET	/feed	Get feed
DELETE	/posts/{id}	Delete post (owner only)
```

🧠 Common Issues & Fixes
❌ no such column: posts.user_id

✅ Delete test.db and restart the server
(SQLite doesn’t auto-migrate schemas)

❌ Login → Not Found

✅ Ensure frontend URLs exactly match /docs endpoints

❌ Password works in register but not login

✅ Use email as username when logging in

📌 Future Improvements

✅ Likes & comments

✅ Profile pages

✅ Pagination for feed

✅ Production DB (PostgreSQL)

✅ Docker support

## 🧑‍💻 Author

Prashant Kr Prasad
📧 Email: mr.prashantkrprasad@gmail.com
🌐 GitHub: https://github.com/praa532
🔗 LinkedIn: https://www.linkedin.com/in/prashantkrprasad