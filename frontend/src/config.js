// API Base URL Configuration for Expense Management
// Jab Render pe backend deploy ho jaye, tab Vercel me REACT_APP_API_URL set kar sakte hain
// ya direct yaha apna Render URL daal sakte hain:
export const API_BASE_URL =
  process.env.REACT_APP_API_URL ||
  (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
    ? "http://localhost:5000"
    : "https://expense-management-backend.onrender.com");
