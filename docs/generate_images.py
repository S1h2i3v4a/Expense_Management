import os
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
os.makedirs(IMG_DIR, exist_ok=True)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('docs/images', exist_ok=True)

# -------------------------------------------------------------------------
# 1. GENERATE DFD DIAGRAM (docs/images/dfd_diagram.png)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 8), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Title Banner
title_box = patches.FancyBboxPatch((4.2, 7.2), 5.6, 0.6, boxstyle="round,pad=0.1",
                                  facecolor='#e0e7ff', edgecolor='#4f46e5', linewidth=2)
ax.add_patch(title_box)
ax.text(7.0, 7.5, "Data Flow Diagram (DFD) - Expense Management",
        fontsize=14, fontweight='bold', color='#312e81', ha='center', va='center')

# Entity 1: User / Browser
user_box = patches.FancyBboxPatch((0.5, 2.8), 2.2, 3.2, boxstyle="round,pad=0.1",
                                  facecolor='#f0fdf4', edgecolor='#16a34a', linewidth=2)
ax.add_patch(user_box)
ax.add_patch(plt.Circle((1.6, 5.0), 0.35, color='#16a34a'))
ax.add_patch(patches.Ellipse((1.6, 4.2), 1.0, 0.6, color='#16a34a'))
ax.text(1.6, 3.4, "End User\n(Web Browser)", fontsize=11, fontweight='bold',
        color='#15803d', ha='center', va='center')

# Process 1: Form Validation
p1_box = patches.FancyBboxPatch((3.5, 4.2), 2.5, 1.8, boxstyle="round,pad=0.1",
                                facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2)
ax.add_patch(p1_box)
ax.add_patch(plt.Circle((4.75, 5.6), 0.22, color='#2563eb'))
ax.text(4.75, 5.6, "1", color='white', fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(4.75, 4.9, "Input Validation\n& State Handling", fontsize=11, fontweight='bold',
        color='#1d4ed8', ha='center', va='center')
ax.text(4.75, 4.4, "(AntD Form Validation,\nFormat Check, Sanitization)", fontsize=8,
        color='#475569', ha='center', va='center')

# Process 2: REST Engine
p2_box = patches.FancyBboxPatch((7.0, 4.2), 2.5, 1.8, boxstyle="round,pad=0.1",
                                facecolor='#faf5ff', edgecolor='#9333ea', linewidth=2)
ax.add_patch(p2_box)
ax.add_patch(plt.Circle((8.25, 5.6), 0.22, color='#9333ea'))
ax.text(8.25, 5.6, "2", color='white', fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(8.25, 4.9, "Express REST API\nEngine", fontsize=11, fontweight='bold',
        color='#7e22ce', ha='center', va='center')
ax.text(8.25, 4.4, "(Router, CORS Middleware,\nControllers Business Logic)", fontsize=8,
        color='#475569', ha='center', va='center')

# Data Store: MongoDB
db_box = patches.FancyBboxPatch((10.5, 4.2), 2.8, 1.8, boxstyle="round,pad=0.1",
                                facecolor='#fff1f2', edgecolor='#e11d48', linewidth=2)
ax.add_patch(db_box)
ax.text(11.9, 5.5, "MongoDB Atlas", fontsize=12, fontweight='bold',
        color='#be123c', ha='center', va='center')
ax.text(11.9, 4.9, "Collections:\n• users (Credentials)\n• transections (Ledger)", fontsize=9,
        color='#334155', ha='center', va='center')

# Process 3: Analytics
p3_box = patches.FancyBboxPatch((5.0, 1.2), 4.5, 1.6, boxstyle="round,pad=0.1",
                                facecolor='#f0fdfa', edgecolor='#0d9488', linewidth=2)
ax.add_patch(p3_box)
ax.add_patch(plt.Circle((7.25, 2.45), 0.22, color='#0d9488'))
ax.text(7.25, 2.45, "3", color='white', fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(7.25, 1.85, "Chart.js Analytics & Summary Engine", fontsize=11, fontweight='bold',
        color='#0f766e', ha='center', va='center')
ax.text(7.25, 1.45, "(Bar, Line & Pie Visualizations + Categorical Metrics)", fontsize=8.5,
        color='#475569', ha='center', va='center')

# Arrows
arrow_style = dict(arrowstyle="->,head_width=0.4,head_length=0.6", linewidth=2)
# User -> P1
ax.annotate("", xy=(3.5, 5.1), xytext=(2.7, 5.1), arrowprops=dict(**arrow_style, color='#16a34a'))
ax.text(3.1, 5.3, "User Input", fontsize=8.5, color='#15803d', ha='center')

# P1 -> P2
ax.annotate("", xy=(7.0, 5.1), xytext=(6.0, 5.1), arrowprops=dict(**arrow_style, color='#2563eb'))
ax.text(6.5, 5.3, "Valid JSON", fontsize=8.5, color='#1d4ed8', ha='center')

# P2 -> DB
ax.annotate("", xy=(10.5, 5.3), xytext=(9.5, 5.3), arrowprops=dict(**arrow_style, color='#9333ea'))
ax.text(10.0, 5.5, "CRUD Query", fontsize=8.5, color='#7e22ce', ha='center')

# DB -> P2
ax.annotate("", xy=(9.5, 4.7), xytext=(10.5, 4.7), arrowprops=dict(**arrow_style, color='#e11d48'))
ax.text(10.0, 4.45, "Result Sets", fontsize=8.5, color='#be123c', ha='center')

# P2 -> P3
ax.annotate("", xy=(7.8, 2.8), xytext=(7.8, 4.2), arrowprops=dict(**arrow_style, color='#0d9488'))
ax.text(8.4, 3.5, "JSON Ledger", fontsize=8.5, color='#0f766e', ha='center')

# P3 -> User
ax.annotate("", xy=(2.7, 3.6), xytext=(5.0, 2.0),
            arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", linewidth=2, color='#16a34a',
                            connectionstyle="arc3,rad=-0.15"))
ax.text(3.6, 2.6, "Rendered UI & Dynamic Charts", fontsize=8.5, color='#15803d', ha='center')

# Legend
leg_box = patches.FancyBboxPatch((11.2, 0.8), 2.3, 2.6, boxstyle="round,pad=0.08",
                                 facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(leg_box)
ax.text(12.35, 3.1, "Legend", fontsize=10, fontweight='bold', color='#1e293b', ha='center')

ax.add_patch(patches.Rectangle((11.4, 2.5), 0.35, 0.22, facecolor='#f0fdf4', edgecolor='#16a34a'))
ax.text(11.9, 2.61, "External Entity", fontsize=8, color='#475569', va='center')

ax.add_patch(patches.Rectangle((11.4, 2.0), 0.35, 0.22, facecolor='#eff6ff', edgecolor='#2563eb'))
ax.text(11.9, 2.11, "Process Module", fontsize=8, color='#475569', va='center')

ax.add_patch(patches.Rectangle((11.4, 1.5), 0.35, 0.22, facecolor='#fff1f2', edgecolor='#e11d48'))
ax.text(11.9, 1.61, "Data Store (DB)", fontsize=8, color='#475569', va='center')

ax.annotate("", xy=(11.75, 1.15), xytext=(11.4, 1.15), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=2))
ax.text(11.9, 1.15, "Data Flow", fontsize=8, color='#475569', va='center')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'dfd_diagram.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Created docs/images/dfd_diagram.png")

# -------------------------------------------------------------------------
# 2. GENERATE SPENDING CHART HIGHLIGHT (docs/images/chart_highlight.png)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4.2), dpi=200)
categories = ['Salary', 'Food', 'Rent', 'Travel', 'Shopping', 'Bills']
amounts = [45000, 8500, 15000, 4200, 6300, 5100]
colors = ['#10b981', '#f59e0b', '#3b82f6', '#8b5cf6', '#ec4899', '#ef4444']

bars = ax.bar(categories, amounts, color=colors, width=0.6, edgecolor='#1e293b', linewidth=1)
ax.set_ylabel('Amount (₹)', fontsize=10, fontweight='bold', color='#1e293b')
ax.set_title('Category-wise Financial Breakdown', fontsize=12, fontweight='bold', color='#0f172a', pad=12)
ax.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 700, f'₹{int(yval)}',
            ha='center', va='bottom', fontsize=8, fontweight='bold', color='#334155')

ax.set_ylim(0, 52000)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'chart_highlight.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Created docs/images/chart_highlight.png")

# -------------------------------------------------------------------------
# 3. GENERATE FLOWCHART (docs/images/flowchart.png)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 11), dpi=200)
ax.set_xlim(0, 8)
ax.set_ylim(0, 11)
ax.axis('off')

def draw_pill(y, text, color='#eff6ff', border='#2563eb'):
    box = patches.FancyBboxPatch((1.8, y), 4.4, 0.7, boxstyle="round,pad=0.1",
                                facecolor=color, edgecolor=border, linewidth=2)
    ax.add_patch(box)
    ax.text(4.0, y + 0.35, text, fontsize=10, fontweight='bold', color='#1e293b', ha='center', va='center')

def draw_start_end(y, text):
    box = patches.FancyBboxPatch((2.6, y), 2.8, 0.6, boxstyle="round,pad=0.25",
                                facecolor='#e0e7ff', edgecolor='#4338ca', linewidth=2)
    ax.add_patch(box)
    ax.text(4.0, y + 0.3, text, fontsize=11, fontweight='bold', color='#312e81', ha='center', va='center')

def draw_diamond(y, text):
    # Diamond decision
    diamond = patches.Polygon([[4.0, y + 0.8], [5.8, y + 0.4], [4.0, y], [2.2, y + 0.4]],
                             closed=True, facecolor='#fef3c7', edgecolor='#d97706', linewidth=2)
    ax.add_patch(diamond)
    ax.text(4.0, y + 0.4, text, fontsize=9.5, fontweight='bold', color='#78350f', ha='center', va='center')

# Nodes
draw_start_end(10.0, "Start")
draw_pill(8.8, "Open Expense Management App\n(Vercel SPA Client)")
draw_pill(7.6, "User Authentication\n(Login / Register via MongoDB)")
draw_pill(6.4, "Display Dashboard\n(Transactions Table & Metrics)")
draw_diamond(4.8, "User Action?\n(Add / Edit / Filter / Delete)")
draw_pill(3.4, "Process Request via Express API\n(Validate & Mutate MongoDB Ledger)")
draw_pill(2.0, "Recompute Analytics & Re-render\n(Update Chart.js & Category Totals)")
draw_start_end(0.6, "End / Idle")

# Arrows
arr = dict(arrowstyle="->,head_width=0.35,head_length=0.5", linewidth=2, color='#1e293b')
ax.annotate("", xy=(4.0, 9.5), xytext=(4.0, 10.0), arrowprops=arr)
ax.annotate("", xy=(4.0, 8.3), xytext=(4.0, 8.8), arrowprops=arr)
ax.annotate("", xy=(4.0, 7.1), xytext=(4.0, 7.6), arrowprops=arr)
ax.annotate("", xy=(4.0, 5.6), xytext=(4.0, 6.4), arrowprops=arr)
ax.annotate("", xy=(4.0, 4.1), xytext=(4.0, 4.8), arrowprops=arr)
ax.annotate("", xy=(4.0, 2.7), xytext=(4.0, 3.4), arrowprops=arr)
ax.annotate("", xy=(4.0, 1.2), xytext=(4.0, 2.0), arrowprops=arr)

# Loop back arrow from Process 3 to Dashboard
ax.annotate("", xy=(6.2, 6.75), xytext=(6.2, 2.35),
            arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", linewidth=2, color='#0d9488',
                            connectionstyle="arc3,rad=-0.4"))
ax.text(7.3, 4.5, "Live UI\nSync", fontsize=9, fontweight='bold', color='#0d9488', ha='center')

ax.text(4.0, 0.15, "Fig. 4.1: Flowchart of the Expense Management System",
        fontsize=10.5, fontweight='bold', color='#0f172a', ha='center')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'flowchart.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Created docs/images/flowchart.png")

# -------------------------------------------------------------------------
# 4. GENERATE UI MOCKUPS (docs/images/ui_fig1.png and ui_fig2.png)
# -------------------------------------------------------------------------
# UI Fig 1: Transactions Table
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Header bar
ax.add_patch(patches.Rectangle((0.2, 5.2), 9.6, 0.7, facecolor='#1e293b'))
ax.text(0.5, 5.55, "Expense Management — Transactions Ledger", color='white', fontsize=11, fontweight='bold', va='center')
ax.text(8.8, 5.55, "User: DemoUser", color='#94a3b8', fontsize=9, va='center')

# Controls row
ax.add_patch(patches.Rectangle((0.2, 4.5), 9.6, 0.55, facecolor='#f1f5f9'))
ax.text(0.4, 4.77, "Filter Category: [ All Categories v ]", fontsize=8.5, color='#334155', va='center')
ax.text(3.6, 4.77, "Sort by: [ Date v ]", fontsize=8.5, color='#334155', va='center')
ax.text(5.5, 4.77, "Order: [ Newest v ]", fontsize=8.5, color='#334155', va='center')
ax.add_patch(patches.FancyBboxPatch((7.6, 4.6), 2.0, 0.35, boxstyle="round,pad=0.04", facecolor='#2563eb', edgecolor='none'))
ax.text(8.6, 4.77, "+ Add Transaction", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

# Table headers
ax.add_patch(patches.Rectangle((0.2, 3.9), 9.6, 0.45, facecolor='#e2e8f0'))
ax.text(0.5, 4.12, "Date", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')
ax.text(2.2, 4.12, "Amount (₹)", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')
ax.text(3.8, 4.12, "Category", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')
ax.text(5.4, 4.12, "Reference", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')
ax.text(7.0, 4.12, "Description", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')
ax.text(8.8, 4.12, "Actions", fontweight='bold', fontsize=8.5, color='#0f172a', va='center')

# Table rows
rows = [
    ("2026-11-01", "₹ 45,000", "salary", "NEFT-9912", "Monthly Salary Credit", "Edit | Delete"),
    ("2026-11-02", "₹ 15,000", "expense", "Rent-Nov", "House Rent Payment", "Edit | Delete"),
    ("2026-11-03", "₹ 2,450", "food", "Swiggy-301", "Groceries & Dinner", "Edit | Delete"),
    ("2026-11-04", "₹ 1,200", "travel", "Uber-8812", "Client Site Travel", "Edit | Delete"),
    ("2026-11-05", "₹ 3,500", "entertainment", "BookMyShow", "Weekend Outing", "Edit | Delete")
]

for idx, r in enumerate(rows):
    y = 3.35 - (idx * 0.55)
    bg = '#ffffff' if idx % 2 == 0 else '#f8fafc'
    ax.add_patch(patches.Rectangle((0.2, y), 9.6, 0.55, facecolor=bg, edgecolor='#f1f5f9'))
    ax.text(0.5, y + 0.27, r[0], fontsize=8, color='#475569', va='center')
    ax.text(2.2, y + 0.27, r[1], fontsize=8.5, fontweight='bold', color='#0f172a', va='center')
    cat_color = '#dcfce7' if r[2] == 'salary' else '#fee2e2'
    text_color = '#15803d' if r[2] == 'salary' else '#b91c1c'
    ax.add_patch(patches.FancyBboxPatch((3.7, y + 0.12), 1.2, 0.32, boxstyle="round,pad=0.04", facecolor=cat_color, edgecolor='none'))
    ax.text(4.3, y + 0.27, r[2].upper(), fontsize=7, fontweight='bold', color=text_color, ha='center', va='center')
    ax.text(5.4, y + 0.27, r[3], fontsize=8, color='#475569', va='center')
    ax.text(7.0, y + 0.27, r[4], fontsize=8, color='#475569', va='center')
    ax.text(8.8, y + 0.27, r[5], fontsize=8, color='#2563eb', va='center')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'ui_fig1.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Created docs/images/ui_fig1.png")

# UI Fig 2: Analytics Dashboard
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Header bar
ax.add_patch(patches.Rectangle((0.2, 5.2), 9.6, 0.7, facecolor='#0f172a'))
ax.text(0.5, 5.55, "Analytics & Category Insights Dashboard", color='white', fontsize=11, fontweight='bold', va='center')
ax.text(8.8, 5.55, "Chart Type: Bar", color='#94a3b8', fontsize=9, va='center')

# Controls
ax.add_patch(patches.Rectangle((0.2, 4.5), 9.6, 0.55, facecolor='#f8fafc'))
ax.text(0.4, 4.77, "Category: [ All Categories v ]", fontsize=8.5, color='#334155', va='center')
ax.text(4.2, 4.77, "Chart: (•) Bar  ( ) Line  ( ) Pie", fontsize=8.5, color='#334155', va='center')
ax.text(7.4, 4.77, "Range: (•) Monthly  ( ) Daily", fontsize=8.5, color='#334155', va='center')

# Card 1: Mini Bar Chart
ax.add_patch(patches.FancyBboxPatch((0.4, 0.4), 5.4, 3.8, boxstyle="round,pad=0.08", facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5))
ax.text(3.1, 3.9, "Monthly Spending Trends (₹)", fontsize=9.5, fontweight='bold', color='#1e293b', ha='center')

# Draw bars inside Card 1
months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
vals = [18, 24, 21, 29, 26, 32]
for i, (m, v) in enumerate(zip(months, vals)):
    x = 0.8 + (i * 0.8)
    h = (v / 35.0) * 2.5
    ax.add_patch(patches.Rectangle((x, 0.9), 0.5, h, facecolor='#3b82f6', edgecolor='#1d4ed8'))
    ax.text(x + 0.25, 0.7, m, fontsize=7.5, ha='center', color='#475569')
    ax.text(x + 0.25, 0.9 + h + 0.1, f'{v}k', fontsize=7, fontweight='bold', ha='center', color='#1e293b')

# Card 2: Circular Progress Gauges
ax.add_patch(patches.FancyBboxPatch((6.1, 0.4), 3.6, 3.8, boxstyle="round,pad=0.08", facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5))
ax.text(7.9, 3.9, "Category Distribution", fontsize=9.5, fontweight='bold', color='#1e293b', ha='center')

cats = [("FOOD", "24%", "#f59e0b", 2.9), ("RENT", "38%", "#3b82f6", 1.9), ("TRAVEL", "15%", "#8b5cf6", 0.9)]
for name, pct, clr, cy in cats:
    ax.add_patch(plt.Circle((6.8, cy), 0.35, color=clr, alpha=0.2))
    ax.add_patch(plt.Circle((6.8, cy), 0.30, color='white'))
    ax.text(6.8, cy, pct, fontsize=8, fontweight='bold', color=clr, ha='center', va='center')
    ax.text(7.4, cy + 0.08, name, fontsize=8.5, fontweight='bold', color='#1e293b')
    ax.text(7.4, cy - 0.12, "Monthly Budget", fontsize=7, color='#64748b')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'ui_fig2.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Created docs/images/ui_fig2.png")
