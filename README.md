# 🚀 Lead Scraper & Scoring Tool  

This project is a **Python-based lead scraping and scoring tool**. It uses **Selenium + BeautifulSoup** to extract data from websites, then applies a **scoring system** to rank potential leads based on tech stack, keywords, and contact availability.  

The tool is designed to help with **lead generation, B2B prospecting, and market research** by automatically collecting and evaluating useful information from websites.  

---

## 📌 Features  

✅ Scrapes website metadata and content:
- Page **Title**  
- **Headings (H1 & H2)**  
- **Meta description**  
- **Full text content**  

✅ Extracts contact details:  
- Emails 📧  
- Phone numbers 📱  

✅ Detects & tags social media profiles:  
- LinkedIn, Twitter, Facebook, Instagram  

✅ Finds **tech stack keywords** (React, Stripe, Firebase, Next.js, GraphQL)  

✅ Collects all hyperlinks  

✅ Lead **scoring system** based on:  
- AI / B2B / SaaS mentions  
- Pricing/Demo links  
- Modern tech stack usage  
- Contact info presence  
- Early-stage/stealth indicators  

✅ Saves results to **CSV** for easy processing  

---

## ⚙️ Installation  

Make sure you have **Python 3.8+** installed.  

```bash
# Clone the repo
git clone https://github.com/yourusername/lead-scraper.git
cd lead-scraper

# Install dependencies
pip install -r requirements.txt
```

### Requirements (`requirements.txt`)  

```
selenium
beautifulsoup4
```

👉 You’ll also need **ChromeDriver** installed and available in PATH.  

---

## ▶️ Usage  

### 1. Run for a single website  

```bash
python scrape.py https://example.com
```

Output example:  

```json
{
  "URL": "https://example.com",
  "Title": "Example Company - AI SaaS Platform",
  "Score": 6,
  "Reasons": "AI/B2B/SaaS keyword found, Has pricing or demo link, Modern tech stack used, Email found",
  "Tags": "B2B",
  "Emails": "contact@example.com",
  "Phones": "+1 555 123 4567",
  "Meta Description": "We provide AI-driven SaaS solutions...",
  "Headings": ["Welcome to Example", "Our Services"],
  "Social Links": {"linkedin": "https://linkedin.com/company/example"},
  "Tech Keywords": ["react", "stripe"],
  "All Links": [...]
}
```

---

### 2. Save multiple results to CSV  

Modify your script to run on multiple URLs and save:  

```python
results = []
urls = ["https://example.com", "https://another.com"]

for u in urls:
    results.append(scrape_and_score(u))

save_results_to_csv(results, "scored_leads.csv")
```

Output: `scored_leads.csv` will contain structured lead data.  

---

## 📊 Scoring Logic  

| Condition                                | Points |
|------------------------------------------|--------|
| Contains **AI / B2B / SaaS** keyword     | +3     |
| Has **pricing/demo** link                | +2     |
| Uses **modern tech (React/Stripe/etc.)** | +2     |
| Additional tech stack found              | +1+    |
| Email found                              | +1     |
| Phone number found                       | +1     |
| Mentions **stealth / closed beta**       | −2     |

This produces a **lead quality score** to help prioritize outreach.  

---

## 📂 Project Structure  

```
.
├── scrape.py              # Main scraper & scoring script
├── requirements.txt       # Dependencies
├── scored_leads.csv       # (Generated) CSV results
└── README.md              # Documentation
```

---

## 🚀 Future Improvements  

- Add **async scraping** for faster batch runs  
- Integrate with **CRM systems (HubSpot, Salesforce)**  
- Expand **tech keyword detection**  
- Detect funding rounds & company size  

---

## 📜 License  

MIT License – free to use, modify, and distribute.  
