import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

os.makedirs('docs', exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        if self._pageNumber > 1:
            report_page_num = self._pageNumber - 1
            self.setFont("Times-Roman", 10.5)
            self.setFillColor(colors.HexColor('#1f2937'))
            self.drawCentredString(A4[0] / 2.0, 36, str(report_page_num))

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_project_report(filename=None):
    if filename is None:
        filename = os.path.join(SCRIPT_DIR, "Expense_Management_Project_Report.pdf")
    PAGE_W, PAGE_H = A4
    MARGIN = 50

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=45,
        bottomMargin=45
    )

    title_chapter = ParagraphStyle(
        'ChapterTitle', fontName='Times-Bold', fontSize=14, leading=18,
        alignment=TA_CENTER, textColor=colors.black, spaceAfter=2
    )

    title_subchapter = ParagraphStyle(
        'SubChapterTitle', fontName='Times-Bold', fontSize=14, leading=18,
        alignment=TA_CENTER, textColor=colors.black, spaceAfter=14
    )

    h2_style = ParagraphStyle(
        'ReportH2', fontName='Times-Bold', fontSize=11, leading=15,
        alignment=TA_LEFT, textColor=colors.black, spaceBefore=10, spaceAfter=4
    )

    h2_center = ParagraphStyle(
        'ReportH2Center', fontName='Times-Bold', fontSize=12, leading=16,
        alignment=TA_CENTER, textColor=colors.black, spaceBefore=12, spaceAfter=8
    )

    body_style = ParagraphStyle(
        'ReportBody', fontName='Times-Roman', fontSize=10.5, leading=15.5,
        alignment=TA_JUSTIFY, textColor=colors.black, spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'ReportBullet', fontName='Times-Roman', fontSize=10.5, leading=15,
        alignment=TA_LEFT, textColor=colors.black, leftIndent=16, spaceAfter=4
    )

    code_style = ParagraphStyle(
        'ReportCode', fontName='Courier', fontSize=7.5, leading=10.0,
        alignment=TA_LEFT, textColor=colors.HexColor('#0f172a'), leftIndent=4, spaceAfter=0
    )

    story = []

    # =========================================================================
    # PAGE 1: INDEX
    # =========================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Index</b>", ParagraphStyle('IndexHead', fontName='Times-Bold', fontSize=18, alignment=TA_CENTER, spaceAfter=30)))

    index_data = [
        [Paragraph("<b>S.<br/>No</b>", ParagraphStyle('IH1', fontName='Times-Bold', fontSize=10.5, alignment=TA_CENTER)),
         Paragraph("<b>Topic</b>", ParagraphStyle('IH2', fontName='Times-Bold', fontSize=10.5, alignment=TA_LEFT)),
         Paragraph("<b>Page No.</b>", ParagraphStyle('IH3', fontName='Times-Bold', fontSize=10.5, alignment=TA_CENTER))],
        ["1", "Introduction", "1"],
        ["2", "Requirement", "2"],
        ["3", "Conceptual Background", "3 to 5"],
        ["4", "Implementation", "6"],
        ["4.1", "Coding", "6 to 9"],
        ["4.2", "Flow Chart", "10"],
        ["5", "User Interface", "11"],
        ["6", "Conclusion", "12"],
        ["", "References", "13"]
    ]

    t_index = Table(index_data, colWidths=[55, 345, 95])
    t_index.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1.0, colors.black),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (1,0), (1,-1), 'LEFT'),
        ('ALIGN', (2,0), (2,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 10.5),
    ]))
    story.append(t_index)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CHAPTER-1 INTRODUCTION (Numbered Page 1)
    # =========================================================================
    story.append(Paragraph("Chapter-1", title_chapter))
    story.append(Paragraph("Introduction", title_subchapter))

    story.append(Paragraph(
        "Financial stability and systematic expenditure tracking play an essential role in the development and financial health of individuals and households. Personal budgeting is an indispensable practice for monitoring cash flows, identifying discretionary spending habits, and safeguarding savings goals. However, monitoring and logging every monetary transaction manually can be challenging when users must consider several spending categories simultaneously.",
        body_style
    ))
    story.append(Paragraph(
        "Traditional approaches to expense management mainly depend on examination of physical bills, manual cash ledgers, or periodic review of bank account statements. Although these manual approaches are familiar, they suffer from significant recording delays, human calculation errors, and an inability to provide early warnings against budget exhaustion. As a result, individuals frequently experience unforeseen end-of-month financial distress.",
        body_style
    ))
    story.append(Paragraph(
        "The Full-Stack Expense Management System, built upon the modern MERN technology stack (MongoDB, Express.js, React.js, and Node.js), is a comprehensive web project designed to support daily income and expenditure tracking. It accepts relevant transactional details, processes the inputs, and stores them in a scalable cloud document database.",
        body_style
    ))
    story.append(Paragraph(
        "The system aims to present the ledger in an intuitive format and provide automated categorical summaries alongside visual analytics (Bar, Line, and Pie charts). This helps users understand potential overspending concerns and consider suitable budgeting adjustments.",
        body_style
    ))
    story.append(Paragraph(
        "The project uses JavaScript and an interactive React web application interface to demonstrate the practical application of full-stack engineering, cloud database management, and data visualization in the personal finance domain.",
        body_style
    ))

    story.append(Paragraph("Problem Statement", h2_center))
    story.append(Paragraph(
        "Personal cash flow is influenced by numerous factors, including monthly income, utility bills, rent, grocery outlays, travel expenses, and entertainment spending. Tracking and analyzing these factors manually requires considerable ongoing effort.",
        body_style
    ))
    story.append(Paragraph(
        "A major challenge is maintaining an up-to-date and organized transaction record. Without an organized analysis system, personal expenditures often escalate unnoticed, eroding liquidity before deficit trends are identified.",
        body_style
    ))
    story.append(Paragraph(
        "Therefore, there is a need for a system that can process transaction data securely, generate summaries, and present financial trends in a simple and understandable manner.",
        body_style
    ))
    story.append(Paragraph(
        "The proposed Expense Management System addresses this problem by combining modern web technologies, automated aggregation, and interactive chart visualizations into an accessible web dashboard.",
        body_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: CHAPTER-2 REQUIREMENT (Numbered Page 2)
    # =========================================================================
    story.append(Paragraph("Chapter-2", title_chapter))
    story.append(Paragraph("Requirement", title_subchapter))

    story.append(Paragraph("2.1 Hardware Requirements", h2_style))
    story.append(Paragraph("The following hardware configuration is suitable for developing, running, and testing the application:", body_style))
    story.append(Paragraph("• Computer or laptop.", bullet_style))
    story.append(Paragraph("• Processor: modern Intel or AMD processor.", bullet_style))
    story.append(Paragraph("• RAM: minimum 4 GB; 8 GB or more is recommended.", bullet_style))
    story.append(Paragraph("• Storage: sufficient free disk space for Node.js, project files, libraries, and dependencies.", bullet_style))
    story.append(Paragraph("• Keyboard and mouse or touchpad.", bullet_style))
    story.append(Paragraph("• Internet connection for installing packages via npm and accessing cloud platforms (Atlas, Vercel, Render).", bullet_style))
    story.append(Paragraph("The exact hardware requirements depend on the size of the transactional database and the local development workload.", body_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph("2.2 Software Requirements", h2_style))
    story.append(Paragraph("The project uses a JavaScript-based full-stack development environment. The relevant software components include:", body_style))
    story.append(Paragraph("• <b>Node.js:</b> Node.js provides the asynchronous JavaScript runtime used to implement the backend API and server logic.", bullet_style))
    story.append(Paragraph("• <b>Express.js:</b> Express.js serves as the web application framework for handling HTTP routing, middleware, and controllers.", bullet_style))
    story.append(Paragraph("• <b>React.js:</b> React is used to develop the interactive Single Page Application (SPA) user interface.", bullet_style))
    story.append(Paragraph("• <b>MongoDB Atlas:</b> Cloud-hosted NoSQL document database for secure storage of user accounts and financial records.", bullet_style))
    story.append(Paragraph("• <b>Mongoose:</b> Mongoose provides schema validation, data modeling, and query execution for MongoDB.", bullet_style))
    story.append(Paragraph("• <b>Ant Design (AntD):</b> Enterprise React UI component framework for modals, tables, notification alerts, and forms.", bullet_style))
    story.append(Paragraph("• <b>Chart.js:</b> JavaScript data visualization library for rendering interactive Bar, Line, and Pie charts.", bullet_style))
    story.append(Paragraph("• <b>Visual Studio Code:</b> Integrated development environment used for writing, editing, and debugging source code.", bullet_style))
    story.append(Paragraph("• <b>Web Browser:</b> A modern web browser used to access the application interface when running locally or on Vercel.", bullet_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: CHAPTER-3 CONCEPTUAL BACKGROUND (Numbered Page 3)
    # =========================================================================
    story.append(Paragraph("Chapter-3", title_chapter))
    story.append(Paragraph("Conceptual Background", title_subchapter))

    story.append(Paragraph("3.1 Web Application Architecture", h2_style))
    story.append(Paragraph(
        "Modern web software typically adheres to a decoupled client-server architectural paradigm. In this architecture, the client (the frontend user interface) and the server (the application backend) are completely separated, communicating asynchronously over the network using standard HTTP/HTTPS protocols and lightweight JSON data interchange formats.",
        body_style
    ))
    story.append(Paragraph(
        "This decoupling allows the frontend and backend to evolve, scale, and deploy independently. The frontend runs in the client's web browser, executing presentation logic, client-side routing, and state manipulation. The backend executes in a secured cloud environment, handling authentication, business logic, and database persistence.",
        body_style
    ))

    story.append(Paragraph("3.2 MERN Stack Ecosystem", h2_style))
    story.append(Paragraph(
        "The MERN stack is an acronym representing four foundational technologies: MongoDB, Express.js, React.js, and Node.js. Its primary architectural advantage is that it enables full-stack JavaScript development, eliminating context switching between different programming languages across application tiers.",
        body_style
    ))
    story.append(Paragraph(
        "MongoDB stores records as flexible BSON documents. Express and Node form a lightweight, non-blocking asynchronous event-driven server runtime. React provides a component-driven UI paradigm powered by Virtual DOM diffing. Together, these technologies offer optimal throughput, maintainability, and rapid development cycles.",
        body_style
    ))

    story.append(Paragraph("3.3 Financial Transaction Management", h2_style))
    story.append(Paragraph(
        "A financial ledger requires high fidelity, accuracy, and immutability. Each transactional record must contain essential attributes to remain analytically meaningful. In personal finance accounting, each transaction encompasses the following core dimensions:",
        body_style
    ))
    story.append(Paragraph("1.  <b>Amount:</b> The precise monetary value involved in the transaction.", bullet_style))
    story.append(Paragraph("2.  <b>Category:</b> The classification of the financial flow (e.g., Salary, Food, Rent, Travel, Entertainment).", bullet_style))
    story.append(Paragraph("3.  <b>Date:</b> The temporal point at which the transaction occurred.", bullet_style))
    story.append(Paragraph("4.  <b>Reference:</b> An optional identifier such as an invoice number or payment confirmation code.", bullet_style))
    story.append(Paragraph("5.  <b>Description:</b> Explanatory context clarifying the purpose of the expenditure.", bullet_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: CHAPTER-3 CONTINUED (Numbered Page 4)
    # =========================================================================
    story.append(Paragraph("3.4 Data Flow and State Synchronization", h2_style))
    story.append(Paragraph(
        "In a modern Single Page Application, user actions trigger state mutations that must be reflected immediately in both local client memory and remote cloud persistence layers. When a user creates or modifies an expense record, the following lifecycle occurs:",
        body_style
    ))
    story.append(Paragraph("1.  User enters transaction values into an Ant Design Form modal.", bullet_style))
    story.append(Paragraph("2.  Frontend validation verifies that required fields are present and correctly formatted.", bullet_style))
    story.append(Paragraph("3.  Axios serializes the data into a JSON payload and transmits an HTTP POST or PUT request.", bullet_style))
    story.append(Paragraph("4.  Express routes receive the request, invoke Mongoose schema validation, and save the document to MongoDB.", bullet_style))
    story.append(Paragraph("5.  The backend returns a standard JSON response confirming the operation.", bullet_style))
    story.append(Paragraph("6.  React updates its local component state, triggering a re-render of the table and re-aggregating Chart.js analytics.", bullet_style))
    story.append(Paragraph(
        "This bidirectional synchronization ensures that the user interface always presents an authoritative, up-to-date representation of financial status without requiring a full browser page refresh.",
        body_style
    ))

    story.append(Paragraph("3.5 Database Modeling and Data Preprocessing", h2_style))
    story.append(Paragraph(
        "Unlike traditional relational databases that require rigid tabular schemas and SQL join operations, document-oriented NoSQL databases like MongoDB store semi-structured JSON-like documents. However, unrestricted document flexibility can introduce data inconsistency in production applications.",
        body_style
    ))
    story.append(Paragraph(
        "Mongoose Object Data Modeling (ODM) resolves this by enforcing strict application-level schema definitions. Mongoose verifies data types, enforces required attributes, validates unique email constraints, and automatically manages audit timestamps (createdAt, updatedAt).",
        body_style
    ))
    story.append(Paragraph("Common preprocessing operations implemented in the application include:", body_style))
    story.append(Paragraph("<b>Type Coercion:</b> Converting incoming numerical strings into strict floating-point numbers.", bullet_style))
    story.append(Paragraph("<b>Date Normalization:</b> Parsing heterogeneous date inputs into UTC ISO-8601 timestamps using Moment.js.", bullet_style))
    story.append(Paragraph("<b>Duplicate Email Prevention:</b> Checking index uniqueness to prevent duplicate account registration.", bullet_style))
    story.append(Paragraph("<b>Categorical Aggregation:</b> Grouping transactions by category keys for real-time sum and percentage calculations.", bullet_style))
    story.append(Paragraph("<b>Sorting and Ordering:</b> Dynamically sorting transaction records chronologically or by monetary value.", bullet_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: CHAPTER-3 CONTINUED (Numbered Page 5)
    # =========================================================================
    story.append(Paragraph("3.6 API Architecture and HTTP Middleware", h2_style))
    story.append(Paragraph(
        "The backend relies on the Representational State Transfer (REST) architectural style. REST defines stateless, cacheable communication using standard HTTP request methods: GET for data retrieval, POST for record creation, PUT for updates, and DELETE for record removal.",
        body_style
    ))
    story.append(Paragraph(
        "Express middleware functions intercept HTTP requests before they reach the controller handlers. In the Expense Management application, the middleware pipeline includes CORS (Cross-Origin Resource Sharing) configuration allowing communication with the Vercel-hosted frontend, express.json() for request body parsing, Morgan for development request logging, and custom health check handlers.",
        body_style
    ))

    story.append(Paragraph("3.7 React Single Page Application (SPA)", h2_style))
    story.append(Paragraph(
        "React is a declarative, component-based frontend library developed by Meta. Instead of rewriting traditional multi-page HTML documents, React loads a single HTML shell (index.html) and dynamically rewrites the DOM (Document Object Model) as the user interacts with the application.",
        body_style
    ))
    story.append(Paragraph(
        "React Router v6 provides client-side routing, intercepting URL changes and rendering designated components without requesting new pages from the server. Protected route wrappers verify user authentication tokens stored in browser localStorage, automatically redirecting unauthenticated visitors to the login view.",
        body_style
    ))

    story.append(Paragraph("3.8 Chart.js Analytics Engine", h2_style))
    story.append(Paragraph(
        "Raw tabular ledgers can be difficult to interpret when evaluating financial trends across months. Chart.js is an open-source, HTML5 Canvas-based visualization library that transforms tabular records into interactive charts.",
        body_style
    ))
    story.append(Paragraph(
        "In the Expense Management analytics module, Chart.js renders Bar charts to contrast spending across categories, Line charts to illustrate expenditure velocity over daily or monthly intervals, and Pie charts alongside circular progress meters to represent proportional category distributions.",
        body_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: CHAPTER-4 IMPLEMENTATION (Numbered Page 6)
    # =========================================================================
    story.append(Paragraph("Chapter -4", title_chapter))
    story.append(Paragraph("Implementation", title_subchapter))
    story.append(Paragraph("4.1 Coding", h2_style))
    story.append(Paragraph("<b># 1. Express Server Setup & Health Endpoint (backend/server.js)</b>", body_style))

    code_p7 = (
"""const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const dotenv = require("dotenv");
const colors = require("colors");
const mongoose = require("mongoose");
const connectDb = require("./config/connectDb");

dotenv.config();
connectDb();

const app = express();
app.use(morgan("dev"));
app.use(express.json());
app.use(cors({ origin: "*", credentials: true }));

// Health check & Keep-alive endpoint
app.get("/", (req, res) => {
  res.status(200).json({
    message: "Expense Management API is running!",
    status: "healthy",
    endpoints: {
      health: "/health",
      users: "/api/v1/users",
      transections: "/api/v1/transections",
    },
  });
});

app.get("/health", async (req, res) => {
  try {
    let dbStatus = "disconnected";
    if (mongoose.connection.readyState === 1 && mongoose.connection.db) {
      await mongoose.connection.db.admin().ping();
      dbStatus = "connected";
    }
    res.json({
      status: "ok",
      database: dbStatus,
      uptimeSeconds: Math.floor(process.uptime()),
      timestamp: new Date().toISOString(),
    });
  } catch (err) {
    res.json({ status: "ok", database: "connecting", error: err.message });
  }
});

// routes
app.use("/api/v1/users", require("./routes/userRoute"));
app.use("/users", require("./routes/userRoute"));
app.use("/api/v1/transections", require("./routes/transectionRoutes"));
app.use("/transections", require("./routes/transectionRoutes"));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`.bgGreen.white);
});"""
    )
    story.append(Preformatted(code_p7, code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: CHAPTER-4 CODING CONTINUED (Numbered Page 7)
    # =========================================================================
    story.append(Paragraph("<b># 2. Database Connection & User Management (backend/controllers/userController.js)</b>", body_style))

    code_p8 = (
"""const mongoose = require("mongoose");
const colors = require("colors");

// backend/config/connectDb.js
mongoose.set("strictQuery", false);

const connectDb = async () => {
  try {
    const mongoURI = process.env.MONGO_URL || process.env.MONGODB_URI;
    if (!mongoURI) {
      console.log("Warning: MONGO_URL not set in environment!".yellow);
      return;
    }
    await mongoose.connect(mongoURI, { serverSelectionTimeoutMS: 5000 });
    console.log(`MongoDB Connected: ${mongoose.connection.host}`.bgCyan.white);
  } catch (error) {
    console.log(`MongoDB connection error: ${error.message}`.bgRed);
  }
};

// backend/controllers/userController.js
const userModel = require("../models/userModel");

const registerController = async (req, res) => {
  try {
    const { name, email, password } = req.body;
    if (!name || !email || !password) {
      return res.status(400).json({
        success: false,
        message: "Name, email, and password are all required",
      });
    }

    const existingUser = await userModel.findOne({ email });
    if (existingUser) {
      return res.status(400).json({
        success: false,
        message: "Email already registered! Please login instead.",
      });
    }

    const newUser = new userModel(req.body);
    await newUser.save();
    res.status(201).json({
      success: true,
      message: "Registration successful!",
      newUser,
    });
  } catch (error) {
    if (error.code === 11000) {
      return res.status(400).json({
        success: false,
        message: "Email already exists. Please login or use another email.",
      });
    }
    res.status(400).json({ success: false, message: error.message });
  }
};"""
    )
    story.append(Preformatted(code_p8, code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: CHAPTER-4 CODING CONTINUED (Numbered Page 8)
    # =========================================================================
    story.append(Paragraph("<b># 3. Transaction Controllers & Schemas (backend/controllers/transectionCtrl.js)</b>", body_style))

    code_p9 = (
"""const TransectionModel = require("../models/transectionModel");

const addTransection = async (req, res) => {
  try {
    const newTransection = new TransectionModel(req.body);
    await newTransection.save();
    res.status(201).json({
      success: true,
      message: "Transection added successfully",
      data: newTransection,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to add transection",
      error: error.message,
    });
  }
};

const getAllTransections = async (req, res) => {
  try {
    const transections = await TransectionModel.find();
    res.status(200).json({
      success: true,
      message: "All transections fetched successfully",
      data: transections,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to fetch transections",
      error: error.message,
    });
  }
};

const updateTransection = async (req, res) => {
  const { id } = req.params;
  try {
    const transection = await TransectionModel.findByIdAndUpdate(
      id, req.body, { new: true }
    );
    if (!transection) {
      return res.status(404).json({ success: false, message: "Not found" });
    }
    res.status(200).json({ success: true, data: transection });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};

const deleteTransection = async (req, res) => {
  const { id } = req.params;
  try {
    await TransectionModel.findByIdAndDelete(id);
    res.status(200).json({ success: true, message: "Deleted successfully" });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};"""
    )
    story.append(Preformatted(code_p9, code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: CHAPTER-4 CODING CONTINUED (Numbered Page 9)
    # =========================================================================
    story.append(Paragraph("<b># 4. Frontend API Configuration & Chart Engine (frontend/src/pages/Analytics.js)</b>", body_style))

    code_p10 = (
"""// frontend/src/config.js
export const API_BASE_URL =
  process.env.REACT_APP_API_URL ||
  (typeof window !== "undefined" &&
  (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
    ? "http://localhost:5000"
    : "https://expense-management-v9yf.onrender.com");

// frontend/src/pages/Analytics.js
const processData = (transactions, selectedCategory, timeRange) => {
  let filteredData = Array.isArray(transactions) ? [...transactions] : [];

  if (selectedCategory !== "all") {
    filteredData = filteredData.filter((t) => t.category === selectedCategory);
  }

  const categoryTotals = filteredData.reduce((acc, t) => {
    acc[t.category] = (acc[t.category] || 0) + t.amount;
    return acc;
  }, {});

  const timeSeriesData = filteredData.reduce((acc, t) => {
    const date = moment(t.date).format(
      timeRange === "monthly" ? "YYYY-MM" : "YYYY-MM-DD"
    );
    acc[date] = (acc[date] || 0) + t.amount;
    return acc;
  }, {});

  return {
    categoryTotals,
    timeSeriesData,
    totalAmount: filteredData.reduce((sum, t) => sum + (t.amount || 0), 0),
  };
};

const getChartData = (categoryTotals, timeSeriesData, chartType) => {
  const colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEEAD"];
  return {
    labels: Object.keys(chartType === "line" ? timeSeriesData : categoryTotals),
    datasets: [{
      label: chartType === "line" ? "Amount Over Time" : "Amount by Category",
      data: Object.values(chartType === "line" ? timeSeriesData : categoryTotals),
      backgroundColor: colors,
      borderColor: colors,
      borderWidth: 1,
    }],
  };
};"""
    )
    story.append(Preformatted(code_p10, code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: FLOW CHART (Numbered Page 10)
    # =========================================================================
    story.append(Paragraph("4.2 Flow Chart", h2_style))
    story.append(Spacer(1, 4))

    if os.path.exists('docs/images/flowchart.png'):
        story.append(RLImage('docs/images/flowchart.png', width=450, height=620))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: CHAPTER-5 USER INTERFACES (Numbered Page 11)
    # =========================================================================
    story.append(Paragraph("Chapter-5", title_chapter))
    story.append(Paragraph("User Interfaces", title_subchapter))

    story.append(Paragraph(
        "The Expense Management dashboard displays transaction ledger statistics, category filter controls, multi-attribute sorting tools, and an interactive financial analytics suite.",
        body_style
    ))

    if os.path.exists('docs/images/ui_fig1.png'):
        story.append(RLImage('docs/images/ui_fig1.png', width=450, height=215))
    story.append(Paragraph("<b>(Fig 5.1)</b>", ParagraphStyle('Cap1', fontName='Times-Bold', fontSize=10, alignment=TA_CENTER, spaceBefore=2, spaceAfter=8)))

    story.append(Paragraph(
        "The analytical interface accepts financial parameters, summarizes spending velocity by time interval, and renders categorical distribution gauges alongside interactive Bar, Line, and Pie charts.",
        body_style
    ))

    if os.path.exists('docs/images/ui_fig2.png'):
        story.append(RLImage('docs/images/ui_fig2.png', width=450, height=215))
    story.append(Paragraph("<b>(Fig 5.2)</b>", ParagraphStyle('Cap2', fontName='Times-Bold', fontSize=10, alignment=TA_CENTER, spaceBefore=2, spaceAfter=4)))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: CHAPTER-6 CONCLUSION (Numbered Page 12)
    # =========================================================================
    story.append(Paragraph("Chapter-6", title_chapter))
    story.append(Paragraph("Conclusion", title_subchapter))

    story.append(Paragraph(
        "The Full-Stack Expense Management System demonstrates the practical application of JavaScript, asynchronous RESTful APIs, document databases, and reactive frontend component engineering in the personal finance domain.",
        body_style
    ))
    story.append(Paragraph(
        "The project provides a unified, coherent workflow through which financial transaction records can be created, inspected, modified, and deleted. The resulting records are persisted in a cloud MongoDB database and dynamically visualized through interactive chart interfaces, accompanied by category-wise percentage gauges and multi-attribute filters.",
        body_style
    ))
    story.append(Paragraph(
        "The project illustrates how the MERN stack contributes to personal financial wellness by helping individuals review their spending velocity in an organized, data-driven manner. It also provides comprehensive practical experience in developing production web applications, configuring cloud hosting providers (Vercel and Render), and maintaining 24/7 service availability through automated keep-alive mechanisms.",
        body_style
    ))
    story.append(Paragraph(
        "However, the system's long-term utility depends on regular user engagement, consistent transaction categorization, and future feature enhancements such as automated bank synchronization and machine-learning-based budget recommendations.",
        body_style
    ))
    story.append(Paragraph(
        "Overall, the application acts as an accessible, reliable personal finance companion, fostering disciplined money management habits and providing a solid foundation for enterprise wealth management software.",
        body_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: REFERENCES (Numbered Page 13)
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>References</b>", ParagraphStyle('RefHead', fontName='Times-Bold', fontSize=16, alignment=TA_CENTER, spaceAfter=25)))

    refs = [
        "[1] React Documentation Team, \"React 18 Documentation: The Library for Web and Native User Interfaces.\" Available: https://react.dev/",
        "[2] Express.js Development Group, \"Express - Fast, Unopinionated, Minimalist Web Framework for Node.js.\" Available: https://expressjs.com/",
        "[3] MongoDB Inc., \"MongoDB Atlas Cloud Database Manual and BSON Document Model.\" Available: https://www.mongodb.com/docs/atlas/",
        "[4] Mongoose ODM Developers, \"Mongoose: Elegant MongoDB Object Modeling for Node.js.\" Available: https://mongoosejs.com/docs/",
        "[5] Ant Design Group, \"Ant Design - An Enterprise-class UI Design Language and React UI Library.\" Available: https://ant.design/docs/react/introduce",
        "[6] Chart.js Community, \"Chart.js: Simple Yet Flexible JavaScript Charting for Designers & Developers.\" Available: https://www.chartjs.org/docs/latest/",
        "[7] Vercel Inc., \"Vercel Documentation: The Platform for Frontend Frameworks.\" Available: https://vercel.com/docs"
    ]

    for r in refs:
        story.append(Paragraph(r, ParagraphStyle('RefEntry', fontName='Times-Roman', fontSize=10.5, leading=16, alignment=TA_LEFT, spaceAfter=14)))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_project_report()
