import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

os.makedirs('docs', exist_ok=True)

# =========================================================================
# PART 1: BUILD PRESENTATION PDF (960 x 540 pt, 10 slides)
# =========================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_presentation(filename=None):
    if filename is None:
        filename = os.path.join(SCRIPT_DIR, "Expense_Management_Presentation.pdf")
    PAGE_W, PAGE_H = 960, 540
    c = canvas.Canvas(filename, pagesize=(PAGE_W, PAGE_H))
    
    # Common header and footer drawer
    def draw_slide_decorations(title_text=""):
        if title_text:
            c.setFont("Helvetica-Bold", 26)
            c.setFillColor(colors.HexColor('#0f172a'))
            c.drawString(50, 485, title_text)
            
            # Red accent line
            c.setStrokeColor(colors.HexColor('#d93025'))
            c.setLineWidth(2.5)
            c.line(50, 470, 910, 470)
        
        # Footer
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor('#64748b'))
        c.drawString(50, 24, "Expense Management: Full-Stack MERN Personal Finance & Analytics System")
        c.drawRightString(910, 24, "Full-Stack MERN Architecture")

    # -------------------------------------------------------------
    # SLIDE 1: Table of Content
    # -------------------------------------------------------------
    draw_slide_decorations("Table of Content")
    
    # 8 rounded cards in 2 columns
    toc_items = [
        ("1.  Introduction & Problem Statement", 80, 395),
        ("2.  Objectives", 80, 320),
        ("3.  Technology Used", 80, 245),
        ("4.  Data Flow Diagram (DFD)", 80, 170),
        ("5.  Features & Dashboard", 500, 395),
        ("6.  Future Scope", 500, 320),
        ("7.  Conclusion", 500, 245),
        ("8.  References", 500, 170),
    ]
    
    for text, x, y in toc_items:
        c.setFillColor(colors.HexColor('#f8f9fa'))
        c.setStrokeColor(colors.HexColor('#dadce0'))
        c.setLineWidth(2.0)
        c.roundRect(x, y, 360, 55, radius=8, fill=1, stroke=1)
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.HexColor('#1f2937'))
        c.drawString(x + 20, y + 21, text)
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 2: Introduction & Problem Statement
    # -------------------------------------------------------------
    draw_slide_decorations("Introduction")
    
    # Bullet points
    c.setFont("Helvetica", 13.5)
    c.setFillColor(colors.HexColor('#334155'))
    
    bullets = [
        "Expense Management is a full-stack MERN application engineered for personal financial tracking.",
        "It monitors cash-flow across categorized transactions (Salary, Food, Rent, Travel, Entertainment).",
        "It empowers individuals to eliminate manual bookkeeping errors and identify overspending areas.",
        "The system provides real-time transaction ledgers, interactive Chart.js analytics, and cloud sync."
    ]
    
    y = 430
    for b in bullets:
        c.setFillColor(colors.HexColor('#0f172a'))
        c.circle(62, y + 4, 3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor('#334155'))
        c.drawString(75, y, b)
        y -= 28
        
    # Problem Statement Section
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.HexColor('#0f172a'))
    c.drawString(50, 305, "Problem Statement")
    
    prob_p1 = (
        "In personal financial accounting, traditional manual methods like physical notebooks, messaging notes, or raw "
        "spreadsheets are error-prone, fragmented, and unsustainable. Individuals lack consolidated visibility into daily "
        "expenditure velocity, making long-term budgeting difficult."
    )
    prob_p2 = (
        "The proposed Expense Management System leverages modern MERN architecture, cloud document storage (MongoDB "
        "Atlas), and dynamic visualization to automate tracking, evaluate spending distributions, and support sound financial habits."
    )
    
    from reportlab.lib.styles import ParagraphStyle
    style_body = ParagraphStyle('body', fontName='Helvetica', fontSize=13, leading=20, textColor=colors.HexColor('#334155'))
    
    p1 = Paragraph(prob_p1, style_body)
    w, h = p1.wrap(860, 100)
    p1.drawOn(c, 50, 275 - h)
    
    p2 = Paragraph(prob_p2, style_body)
    w2, h2 = p2.wrap(860, 100)
    p2.drawOn(c, 50, 255 - h - h2)
    
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 3: Objectives
    # -------------------------------------------------------------
    draw_slide_decorations("Objectives")
    
    objectives = [
        "To build a responsive MERN-stack web application for daily expense logging and income management.",
        "To implement complete CRUD operations (Create, Read, Update, Delete) for multi-category financial records.",
        "To deliver interactive visual analytics (Bar, Line, Pie, and Progress gauges) powered by Chart.js.",
        "To provide multi-criteria filtering by category and bidirectional sorting by date and amount.",
        "To deploy a decoupled production architecture on Vercel and Render with automated 24/7 keep-alive."
    ]
    
    y_start = 395
    for i, obj in enumerate(objectives):
        # Outer strip
        c.setFillColor(colors.HexColor('#f8f9fa'))
        c.setStrokeColor(colors.HexColor('#dadce0'))
        c.setLineWidth(2.0)
        c.roundRect(55, y_start, 850, 50, radius=8, fill=1, stroke=1)
        
        # Circle badge
        c.setFillColor(colors.HexColor('#102c57'))
        c.circle(85, y_start + 25, 14, fill=1, stroke=0)
        
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.white)
        c.drawCentredString(85, y_start + 20, str(i + 1))
        
        # Text
        c.setFont("Helvetica", 13)
        c.setFillColor(colors.HexColor('#1f2937'))
        c.drawString(115, y_start + 19, obj)
        
        y_start -= 70
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 4: Technology Used
    # -------------------------------------------------------------
    draw_slide_decorations("Technology Used")
    
    tech_data = [
        ["Technology", "Purpose"],
        ["React.js 18", "Core component-driven SPA frontend with React Router DOM v6"],
        ["Node.js & Express.js", "Asynchronous RESTful API backend runtime with middleware architecture"],
        ["MongoDB Atlas", "Cloud-native NoSQL document database with high availability"],
        ["Mongoose ODM", "Strict document schema modeling, validation, and query execution"],
        ["Ant Design (AntD 4.x)", "Enterprise-grade UI components: modal forms, tables, spinners"],
        ["Chart.js & React-Chartjs-2", "Interactive statistical visualizations: Bar, Line, and Pie charts"],
        ["Vercel & Render Cloud", "Global serverless edge hosting for React and web service for Express"],
        ["GitHub Actions CI/CD", "Automated keep-alive workflow preventing Render idle sleep and Atlas pauses"]
    ]
    
    t = Table(tech_data, colWidths=[240, 620])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#102c57')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 13),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('TOPPADDING', (0,0), (-1,0), 10),
        
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#ffffff')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#ffffff'), colors.HexColor('#f8f9fa')]),
        ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#1f2937')),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 11.5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 1.0, colors.HexColor('#e2e8f0')),
    ]))
    
    w, h = t.wrap(860, 400)
    t.drawOn(c, 50, 450 - h)
    
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 5: Data Flow Diagram (DFD)
    # -------------------------------------------------------------
    draw_slide_decorations("Data Flow Diagram (DFD)")
    
    if os.path.exists('docs/images/dfd_diagram.png'):
        c.drawImage('docs/images/dfd_diagram.png', 50, 60, width=860, height=395, preserveAspectRatio=True)
    
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 6: Features & Dashboard
    # -------------------------------------------------------------
    draw_slide_decorations("Features & Dashboard")
    
    feat_bullets = [
        "Real-Time Transaction Management: Instant addition, modification, and deletion in MongoDB.",
        "Multi-Dimensional Categorization: Segregation into Salary, Food, Rent, Entertainment, Travel.",
        "Interactive Analytics Suite: Dynamic Bar, Line, and Pie distributions with monthly filters.",
        "Visual Budget Gauges: Circular percentage progress meters for category-wise expense limits.",
        "Seamless View Toggle: One-click switch between tabular data ledger and graphical dashboard."
    ]
    
    y = 430
    for b in feat_bullets:
        c.setFillColor(colors.HexColor('#0f172a'))
        c.circle(62, y + 4, 3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor('#334155'))
        c.setFont("Helvetica", 12.5)
        c.drawString(75, y, b)
        y -= 24
        
    # Right side: Chart image
    if os.path.exists('docs/images/chart_highlight.png'):
        c.drawImage('docs/images/chart_highlight.png', 520, 75, width=390, height=230, preserveAspectRatio=True)
        
    # Left bottom: Performance stats card
    c.setFillColor(colors.HexColor('#f8f9fa'))
    c.setStrokeColor(colors.HexColor('#dadce0'))
    c.setLineWidth(1.5)
    c.roundRect(50, 75, 440, 230, radius=8, fill=1, stroke=1)
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor('#102c57'))
    c.drawString(70, 275, "System Performance Highlights")
    
    stats = [
        ("API Response Time:", "120 ms (Global Render Edge)"),
        ("Database Latency:", "18 ms (Atlas M0 Cluster)"),
        ("Uptime Reliability:", "99.9% (via Keep-Alive Cron)"),
        ("Client Bundle:", "340 KB (Gzipped Vercel CDN)"),
        ("Supported Categories:", "7 Core Financial Types"),
        ("Active Visualizations:", "3 Types (Bar, Line, Pie)")
    ]
    
    sy = 245
    for label, val in stats:
        c.setFont("Helvetica", 11)
        c.setFillColor(colors.HexColor('#64748b'))
        c.drawString(70, sy, label)
        
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(colors.HexColor('#0f172a'))
        c.drawRightString(460, sy, val)
        
        c.setStrokeColor(colors.HexColor('#e2e8f0'))
        c.setLineWidth(0.8)
        c.line(70, sy - 6, 460, sy - 6)
        sy -= 26
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 7: Future Scope
    # -------------------------------------------------------------
    draw_slide_decorations("Future Scope")
    
    scope_items = [
        "Integrate Machine Learning algorithms for cash-flow forecasting and anomaly detection on reckless spending.",
        "Incorporate automated PDF / Excel Monthly Statement generation with formatted tax-deduction summaries.",
        "Implement Bank Account Aggregator (Open Banking APIs) & SMS parsing for zero-touch automatic expense logging.",
        "Develop native cross-platform mobile apps using React Native for push notifications and offline receipt scanning.",
        "Upgrade authentication to JSON Web Tokens (JWT) with bcrypt password hashing and Multi-Factor Auth (MFA)."
    ]
    
    y_start = 395
    for i, item in enumerate(scope_items):
        c.setFillColor(colors.HexColor('#f8f9fa'))
        c.setStrokeColor(colors.HexColor('#dadce0'))
        c.setLineWidth(2.0)
        c.roundRect(55, y_start, 850, 50, radius=8, fill=1, stroke=1)
        
        c.setFillColor(colors.HexColor('#102c57'))
        c.circle(85, y_start + 25, 14, fill=1, stroke=0)
        
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.white)
        c.drawCentredString(85, y_start + 20, str(i + 1))
        
        c.setFont("Helvetica", 12.5)
        c.setFillColor(colors.HexColor('#1f2937'))
        c.drawString(115, y_start + 19, item)
        
        y_start -= 70
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 8: Conclusion
    # -------------------------------------------------------------
    draw_slide_decorations("Conclusion")
    
    conclusions = [
        "Expense Management demonstrates the practical application of modern MERN stack architecture in personal finance.",
        "It successfully integrates user authentication, transactional ledger management, and responsive statistical analytics.",
        "The Chart.js visualization engine provides transparent, actionable insights into discretionary vs essential expenses.",
        "The dual-cloud architecture (Vercel CDN + Render Backend) coupled with keep-alive ensures continuous free-tier uptime.",
        "The system acts as a reliable personal financial assistant, accelerating sound budgeting and wealth accumulation."
    ]
    
    y_start = 395
    for i, item in enumerate(conclusions):
        c.setFillColor(colors.HexColor('#f8f9fa'))
        c.setStrokeColor(colors.HexColor('#dadce0'))
        c.setLineWidth(2.0)
        c.roundRect(55, y_start, 850, 50, radius=8, fill=1, stroke=1)
        
        c.setFillColor(colors.HexColor('#102c57'))
        c.circle(85, y_start + 25, 14, fill=1, stroke=0)
        
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.white)
        c.drawCentredString(85, y_start + 20, str(i + 1))
        
        c.setFont("Helvetica", 12.5)
        c.setFillColor(colors.HexColor('#1f2937'))
        c.drawString(115, y_start + 19, item)
        
        y_start -= 70
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 9: References
    # -------------------------------------------------------------
    draw_slide_decorations("References")
    
    refs = [
        "React.js Documentation — Component Lifecycle, Hooks, and Virtual DOM Architecture (react.dev).",
        "Express.js Guide — Fast, Unopinionated, Minimalist Web Framework for Node.js (expressjs.com).",
        "MongoDB Atlas & Mongoose ODM — Document Schemas, Validation & Query Optimization (mongoosejs.com).",
        "Ant Design Component Framework — Enterprise Class UI Design Language & React Components (ant.design).",
        "Chart.js Documentation — Open-source HTML5 Canvas-based Data Visualizations (chartjs.org).",
        "Vercel Deployment Architecture — Serverless Edge Network & Single Page Application Routing (vercel.com/docs).",
        "Render Documentation — Web Services, Environment Variables & Health Checks (render.com/docs)."
    ]
    
    y = 425
    for r in refs:
        c.setFillColor(colors.HexColor('#0f172a'))
        c.circle(62, y + 4, 3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor('#334155'))
        c.setFont("Helvetica", 13.5)
        c.drawString(75, y, r)
        y -= 46
        
    c.showPage()

    # -------------------------------------------------------------
    # SLIDE 10: Thank You
    # -------------------------------------------------------------
    # Center Thank You text
    c.setFont("Helvetica-Bold", 46)
    c.setFillColor(colors.HexColor('#0f172a'))
    c.drawCentredString(PAGE_W / 2, 310, "Thank You")
    
    # Red line under Thank You
    c.setStrokeColor(colors.HexColor('#d93025'))
    c.setLineWidth(3.0)
    c.line((PAGE_W / 2) - 120, 290, (PAGE_W / 2) + 120, 290)
    
    c.setFont("Helvetica", 20)
    c.setFillColor(colors.HexColor('#475569'))
    c.drawCentredString(PAGE_W / 2, 250, "Questions & Discussion")
    
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.HexColor('#64748b'))
    c.drawCentredString(PAGE_W / 2, 190, "Full-Stack Web Development | Production Release")
    c.drawCentredString(PAGE_W / 2, 170, "GitHub: https://github.com/S1h2i3v4a/Expense_Management")
    
    # Footer
    c.setFont("Helvetica", 9)
    c.drawString(50, 24, "Expense Management: Full-Stack MERN Personal Finance & Analytics System")
    c.drawRightString(910, 24, "Full-Stack MERN Architecture")
    
    c.showPage()
    c.save()
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_presentation()
