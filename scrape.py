import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time
from bs4 import BeautifulSoup


def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        title = driver.title.strip()
        headings = [elem.text.strip() for elem in driver.find_elements(By.XPATH, "//h1 | //h2")]

        emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", page_source)))
        raw_phones = re.findall(r"\+?\d[\d\s().-]{7,}\d", page_source)
        phones = [p for p in set(raw_phones) if not re.match(r"\d{4}-\d{2}-\d{2}", p)]

        all_links = [elem.get_attribute('href') for elem in driver.find_elements(By.TAG_NAME, 'a') if elem.get_attribute('href')]

        socials = {
            name: link for link in all_links for name in ['linkedin', 'twitter', 'facebook', 'instagram']
            if name in link.lower()
        }

        desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = desc_tag["content"].strip() if desc_tag and desc_tag.get("content") else ""

        tech_keywords = []
        tech_list = ["react", "stripe", "firebase", "nextjs", "graphql"]
        lower_source = page_source.lower()
        for tech in tech_list:
            if tech in lower_source:
                tech_keywords.append(tech)

        body_text = soup.get_text(separator=" ").lower()

        return {
            "url": url,
            "title": title,
            "headings": headings,
            "emails": emails,
            "phones": phones,
            "social_links": socials,
            "meta_description": meta_desc,
            "tech_keywords_found": tech_keywords,
            "all_links": all_links,
            "full_text": body_text,
        }

    finally:
        driver.quit()


def score_lead(data):
    score = 0
    reasons = []
    tags = []

    desc_text = (
        data.get("meta_description", "") + " " +
        " ".join(data.get("headings", [])) + " " +
        data.get("full_text", "")
    ).lower()

    techs = data.get("tech_keywords_found", [])
    links = data.get("all_links", [])
    emails = data.get("emails", [])
    phones = data.get("phones", [])

    if any(word in desc_text for word in ["ai", "b2b", "saas"]):
        score += 3
        reasons.append("AI/B2B/SaaS keyword found")
        if "b2b" in desc_text:
            tags.append("B2B")

    if any("pricing" in link.lower() or "demo" in link.lower() for link in links):
        score += 2
        reasons.append("Has pricing or demo link")

    if any(t in techs for t in ["react", "stripe", "firebase"]):
        score += 2
        reasons.append("Modern tech stack used")

    extra_tech_score = max(0, len(techs) - 2)
    if extra_tech_score > 0:
        score += extra_tech_score
        reasons.append(f"Additional tech stack (+{extra_tech_score})")

    if "health" in desc_text:
        tags.append("Healthtech")

    if any(word in desc_text for word in ["stealth", "closed beta", "pre-revenue"]):
        score -= 2
        reasons.append("Stealth or early stage mentioned")

    if emails:
        score += 1
        reasons.append("Email found")

    if phones:
        score += 1
        reasons.append("Phone number found")

    return score, ", ".join(reasons), ", ".join(tags)


def scrape_and_score(url):
    """
    Main function to call from frontend.
    Returns combined scraped data + scoring.
    """
    scraped_data = scrape_website(url)
    score, reasons, tags = score_lead(scraped_data)

    return {
        "URL": scraped_data["url"],
        "Title": scraped_data["title"],
        "Score": score,
        "Reasons": reasons,
        "Tags": tags,
        "Emails": ", ".join(scraped_data["emails"]),
        "Phones": ", ".join(scraped_data["phones"]),
        "Meta Description": scraped_data["meta_description"],
        "Headings": scraped_data["headings"],
        "Social Links": scraped_data["social_links"],
        "Tech Keywords": scraped_data["tech_keywords_found"],
        "All Links": scraped_data["all_links"],
    }


def save_results_to_csv(results, filename="scored_leads.csv"):
    if not results:
        print("No results to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"✅ Results saved to {filename}")


if __name__ == "__main__":
    # For batch mode if needed
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(f"Scraping single URL: {url}")
        result = scrape_and_score(url)
        print(result)
    else:
        print("Run with python scrape.py <url> to scrape a single site")
