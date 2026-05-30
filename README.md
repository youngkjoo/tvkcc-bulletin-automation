# TVKCC Bulletin Automation System

## Project Overview
The **TVKCC Bulletin Automation System** is a high-fidelity web publishing pipeline designed to transform the manual Korean church bulletin workflow into an automated, mobile-friendly English web archive. The system scrapes the latest bulletin data from the St. Paul Chong Korean Catholic Community (TVKCC) website, translates it using AI-driven style guides, and publishes it as a newspaper-style HTML page served via GitHub Pages.

---

## 🚀 Key Features

### 1. High-Fidelity Design
- **Traditional Newspaper Layout**: Mimics the olive and gold aesthetic of the original Korean bulletin.
- **Two-Column Grid**: Announcements are automatically balanced across two columns for readability.
- **Responsive & Print-Ready**: Optimized for mobile browsing with a dedicated "Print/Save as PDF" feature for physical distribution.

### 2. Automated Publishing Workflow
- **Smart Translation**: Maintains consistency using `bulletin_style_guide.md` for strict formatting rules and `bulletin_announcement_catalog.md` for recurring announcement templates. These guides were developed by processing over 3 years of historical bulletin data.
- **Human-in-the-Loop Review**: A dedicated review step allows for easy edits to the Markdown draft before the final HTML is generated and published.
- **Continuous Improvement**: The system automatically updates the style guide and announcement catalog based on feedback and manual edits made during the weekly review.
- **Automated Archive**: Generates weekly HTML files and updates the `index.html` archive list automatically.

### 3. Integrated Parish Features
- **Online Giving**: Dedicated QR code section linking directly to the church's online giving portal.
- **Pope's Intentions**: Monthly integration of the Pope's prayer intentions.
- **Parish Leadership**: Dynamic header section containing current pastor and council personnel contacts.
- **Navigation System**: Interlinked "Previous Week" and "Next Week" buttons on every page for easy browsing of past bulletins.

---

## 📂 Repository Structure

```text
├── README.md                   # Project documentation (PRD)
├── tvkcc_bulletin.md           # Master workflow instructions
├── bulletin_style_guide.md     # Strict rules for translation
├── bulletin_announcement_catalog.md # Reusable templates
├── drafts/                     # Weekly translation drafts (Markdown files)
└── docs/                       # Web root folder served by GitHub Pages
    ├── index.html              # Main archive/landing page (2026 Bulletins)
    ├── style.css               # Shared design system (typography, colors, layout)
    ├── bulletins/              # Directory containing weekly English HTML pages
    └── assets/                 # Shared media (Logo, QR codes, icons)
        ├── tvkcc_logo.png      # Official church logo
        ├── qr_donate.png       # Online giving QR code
        └── qr_confirmation.png # Sacrament of Confirmation registration QR code
```

---

## 🛠️ Fine-Tuned Layout Details

Through multiple iterations, the following layout refinements have been standardized:

### **Header Section**
- **Logo**: Positioned on the left (`tvkcc_logo.png`).
- **Personnel List**: Positioned on the right, listing Pastor, Council President, District Leader, and Bereavement Society Head with contact numbers.
- **Title Bar**: Olive-background bar displaying the Sunday Liturgy Title and Issue Number.

### **Core Schedule (Page 1)**
- **Mass Table**: Combined table for Mass times (Korean/English/Weekday), Confession, and Devotions.
- **Devotions Included**: Legion of Mary, Ultreya, Secular Franciscan Order, and Holy Hour.
- **Dynamic Schedule**: Priest schedule and "Please Pray For" names box are placed directly below the Mass table for high visibility.

### **Announcement Grid**
- **Multi-Column**: Announcements are split into two columns.
- **Bullet Styling**: Standardized dots (`*` in markdown, `○` in HTML) for clean rendering across all devices.

---

## ⚙️ How to Run the Weekly Update

To execute the weekly publishing process, trigger the assistant with the following command:

> **"@tvkcc_bulletin.md Execute the weekly bulletin translation."**

The assistant will:
1.  Scrape the latest PDF from the website.
2.  Extract the Sunday liturgy title from `bible.usccb.org`.
3.  Retrieve the monthly Pope's prayer intention.
4.  Generate a Markdown translation draft for review.
5.  Generate the final styled HTML page.
6.  Update `index.html` with the new entry.
7.  Commit and push all changes to the GitHub repository.

---



## ⚖️ Maintenance Notes
- **Logo/Personnel**: If church leadership changes, update the reference template in `bulletins/2026-05-03.html`.
- **URLs**: The current online giving URL is `https://www.tvkcc.org/onlinegiving/`.
- **CSS**: The `style.css` file uses `--olive` and `--gold` variables to maintain the church's brand colors.
