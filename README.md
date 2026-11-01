# 💰 Expense Management System

Full-stack MERN Expense Tracker application split into **Frontend** (React.js) and **Backend** (Node.js & Express) for seamless deployment on **Vercel** and **Render**.

```
Expense_Management/
├── backend/            # Express.js API + MongoDB (Deploy on Render)
├── frontend/           # React.js application (Deploy on Vercel)
├── .gitignore
└── README.md
```

---

## 🚀 Deployment Instructions

### 1. Backend (Render)
- **Service Type:** Web Service
- **Root Directory:** `backend`
- **Build Command:** `npm install`
- **Start Command:** `node server.js`
- **Environment Variables:**
  - `MONGO_URL` or `MONGODB_URI` = Your MongoDB connection string
  - `PORT` = `5000` (or leave default, Render sets dynamically)

### 2. Frontend (Vercel)
- **Framework Preset:** `Create React App`
- **Root Directory:** `frontend`
- **Build Command:** `npm run build`
- **Output Directory:** `build`
- **Environment Variables (Optional):**
  - `REACT_APP_API_URL` = Your Render backend URL (e.g. `https://your-backend.onrender.com`)

---

## 🛠️ Tech Stack
- **Frontend:** React 18, Ant Design (AntD), React Router DOM v6, Axios, Chart.js
- **Backend:** Node.js, Express.js, MongoDB (Mongoose), Morgan, Cors, Colors
