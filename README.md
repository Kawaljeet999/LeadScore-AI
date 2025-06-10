
# 🚀 LeadScore AI - Smart Lead Intelligence Scraper

**LeadScore AI** is a web scraping and scoring tool built using Selenium, BeautifulSoup, and Python. It intelligently extracts data from startup or business websites and scores them based on indicators such as modern tech stacks, keywords like "AI" or "B2B", and presence of emails, phone numbers, social links, and more.

---

## 🔥 Features

- 🌐 Scrapes website title, meta description, headings, full text
- 📧 Extracts emails and phone numbers
- 🔗 Finds all links including LinkedIn, Twitter, Facebook, etc.
- 🧠 Scores websites based on:
  - Keywords like **AI**, **B2B**, **SaaS**
  - Use of modern tech like **React**, **Firebase**, **Stripe**
  - Presence of pricing/demo pages
  - Availability of contact info (emails, phones)
- 🏷️ Automatically tags companies (e.g., Healthtech, B2B)
- 📦 Saves results in a clean CSV file
- 💻 Headless browser support for fast and invisible scraping

---

## 🛠 Tech Stack

- **Python 3.11+**
- **Selenium 4.33**
- **BeautifulSoup 4**
- **Pandas**
- **Streamlit (for UI integration)**
- Headless Chrome for automation

---

## 📸 Demo

👉 [Live Demo (Coming Soon)](https://your-demo-link.com)

---

## 🧪 How It Works

1. Open any startup website.
2. The scraper fetches the full HTML and parses useful content.
3. A scoring algorithm evaluates the site based on:
   - Keywords
   - Modern tech usage
   - Links and metadata
4. Final data is saved to a CSV or shown in the Streamlit app.

---

## 🚀 Run Locally

### 📦 Requirements

```bash
pip install -r requirements.txt
```

### ▶️ Usage

#### Run from CLI

```bash
python scrape.py https://example.com
```

#### Run with Streamlit UI

```bash
streamlit run app.py
```

---

## 📄 Output

- Results include:
  - Title, Meta Description
  - Emails, Phones
  - Social Links, Tags
  - Score and Scoring Reasons
- Output CSV: `scored_leads.csv`

---

## 🌍 Deployment (Optional)

To deploy on platforms like **Streamlit Cloud**:

1. Push code to GitHub.
2. Create a `requirements.txt` (already done).
3. Deploy on [Streamlit Cloud](https://streamlit.io/cloud).
4. Add demo link to this README.

---

## 🧠 Ideal For

- Lead generation teams
- Startup analysts
- Investors doing due diligence
- Marketing teams targeting SaaS, B2B, or AI-based tools

---

## 👨‍💻 Author

- Made with ❤️ by Kawaljeet Singh
- [LinkedIn](https://www.linkedin.com/in/kawaljeet)

---

## 🪪 License

Licensed under the Apache 2.0 License.
