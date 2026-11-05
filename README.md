# 💰 Expense Management System — Full-Stack MERN Personal Finance & Analytics

[![React](https://img.shields.io/badge/React-18.2.0-blue.svg?logo=react)](https://reactjs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18.x-green.svg?logo=node.js)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.18.2-black.svg?logo=express)](https://expressjs.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-6.x-green.svg?logo=mongodb)](https://www.mongodb.com/cloud/atlas)
[![Vercel](https://img.shields.io/badge/Vercel-Frontend%20Live-black.svg?logo=vercel)](https://expense-management-2f5x.vercel.app)
[![Render](https://img.shields.io/badge/Render-Backend%20Live-46E3B7.svg?logo=render)](https://expense-management-v9yf.onrender.com)

A full-stack personal finance application built with the **MERN** stack (MongoDB, Express.js, React.js, Node.js). It provides real-time transactional tracking, multi-category budgeting, and interactive data visualization (Bar, Line, and Pie charts) powered by **Chart.js** and **Ant Design**.

---

## 🌐 Live Deployments

- **Live Backend API:** [https://expense-management-v9yf.onrender.com](https://expense-management-v9yf.onrender.com)
- **API Health & Keep-Alive:** [https://expense-management-v9yf.onrender.com/health](https://expense-management-v9yf.onrender.com/health)
- **Live Frontend Web App:** [https://expense-management-2f5x.vercel.app](https://expense-management-2f5x.vercel.app)

---

## 📚 Project Documentation & Academic Submissions

The project includes formal academic documentation matching institutional submission guidelines:

| Document | Format | Description | Link |
|---|---|---|---|
| **Project Presentation** | PDF (10 Slides) | Widescreen presentation deck covering TOC, Problem Statement, Objectives, Tech Stack, DFD, Features, Benchmarks, Future Scope, Conclusion | [View Presentation PDF](docs/Expense_Management_Presentation.pdf) |
| **Project Report** | PDF (14 Pages) | Formal 14-page project report with Index, Chapters 1-6 (Intro, Requirements, Conceptual Background, Implementation Code, Flowchart, UI, Conclusion, References) | [View Report PDF](docs/Expense_Management_Project_Report.pdf) |
| **Interactive HTML Deck** | Web / HTML | Browser-viewable presentation deck with vector diagrams | [docs/Expense_Management_Presentation.html](docs/Expense_Management_Presentation.html) |
| **Printable Report HTML** | Web / HTML | Printable A4 academic report with chapter pagination | [docs/Expense_Management_Project_Report.html](docs/Expense_Management_Project_Report.html) |

---

## 📂 Project Structure

```
Expense_Management/
├── .github/
│   └── workflows/
│       └── keep-alive.yml         # 24/7 automated ping workflow (prevents Render sleep)
├── backend/
│   ├── config/
│   │   └── connectDb.js           # Mongoose MongoDB Atlas connection module
│   ├── controllers/
│   │   ├── transectionCtrl.js     # Transaction CRUD controller logic
│   │   └── userController.js      # User registration & login controller
│   ├── models/
│   │   ├── transectionModel.js    # Transaction schema definition
│   │   └── userModel.js           # User authentication schema
│   ├── routes/
│   │   ├── transectionRoutes.js   # Transaction API routes
│   │   └── userRoute.js           # User auth API routes
│   ├── .env.example
│   ├── package.json
│   └── server.js                  # Main Express application & keep-alive endpoints
├── frontend/
│   ├── public/                    # Static assets & index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout/            # Header, Footer, and Layout wrappers
│   │   │   └── Spinner.js         # Loading indicator component
│   │   ├── pages/
│   │   │   ├── HomePage.js        # Transaction ledger, filter, sort & modal form
│   │   │   ├── Analytics.js       # Chart.js visual analytics & category gauges
│   │   │   ├── Login.js           # User login interface
│   │   │   └── Register.js        # User registration interface
│   │   ├── config.js              # Dynamic API base URL resolver
│   │   ├── App.js                 # React Router v6 & ProtectedRoute wrappers
│   │   └── index.js               # React entry point
│   ├── .env.production            # CI=false build settings
│   ├── vercel.json                # SPA client-side routing rewrites
│   └── package.json
├── docs/
│   ├── Expense_Management_Presentation.pdf
│   ├── Expense_Management_Project_Report.pdf
│   ├── Expense_Management_Presentation.html
│   ├── Expense_Management_Project_Report.html
│   ├── generate_presentation_pdf.py
│   ├── generate_report_pdf.py
│   └── images/                    # DFD, Flowchart, UI mockups, charts
├── .gitignore
└── README.md
```

---

## 🔄 System Architecture & Data Flow

```
+------------------+          HTTP Requests           +----------------------+
|                  | -------------------------------> |                      |
|  React 18 SPA    |         (JSON Payloads)          |  Express.js Server   |
| (Vercel Edge)    |                                  |   (Render Cloud)     |
|                  | <------------------------------- |                      |
+------------------+           JSON Responses         +----------------------+
         ^                                                       |
         |                                                       | Mongoose ODM
         |                                                       v
+------------------+                                  +----------------------+
|  Chart.js Engine |                                  |    MongoDB Atlas     |
| (Visual Insights)|                                  | (ExpenseManagementDB)|
+------------------+                                  +----------------------+
```

---

## ⚡ Core Features

1. **Transaction Ledger & CRUD:** Add, inspect, modify, and delete transactions with real-time UI feedback.
2. **Category Segmentation:** Categorize expenditures into *Salary, Food, Rent, Travel, Entertainment, Other*.
3. **Multi-Attribute Filters:** Filter by category, sort chronologically (asc/desc) or by monetary amount.
4. **Visual Analytics Suite:** Switch effortlessly to Chart.js view (Bar, Line, Pie) with circular category gauges.
5. **Secure Authentication:** User registration with duplicate-email prevention, login, and protected routes.
6. **24/7 Cloud Availability:** Render `/health` endpoint pinged every 14 minutes via GitHub Actions.

---

## 🔗 RESTful API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status and available route endpoints |
| `GET` | `/health` | Server uptime & MongoDB Atlas ping status |
| `POST` | `/users/register` | Register a new user account |
| `POST` | `/users/login` | Authenticate an existing user |
| `GET` | `/api/v1/transections/get-all-transections` | Retrieve all transaction records |
| `POST` | `/api/v1/transections/add-transection` | Create a new transaction |
| `PUT` | `/api/v1/transections/update-transection/:id` | Update an existing transaction |
| `DELETE` | `/api/v1/transections/delete-transection/:id` | Remove a transaction from the ledger |

---

## 🚀 Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/S1h2i3v4a/Expense_Management.git
cd Expense_Management
```

### 2. Backend Setup
```bash
cd backend
npm install
# Create .env file with your MongoDB connection string
# MONGO_URL=mongodb+srv://<user>:<password>@cluster.mongodb.net/ExpenseManagementDB
# PORT=5000
npm start
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
npm start
```
The application will launch at `http://localhost:3000`.

---

## 👤 Project Information

- **Project:** Expense Management System
- **Stack:** MongoDB, Express.js, React.js, Node.js (MERN)
- **Architecture:** Decoupled Client-Server with RESTful API
- **Deployment:** Vercel (Frontend) + Render (Backend)
- **Repository:** [Expense_Management](https://github.com/S1h2i3v4a/Expense_Management)
