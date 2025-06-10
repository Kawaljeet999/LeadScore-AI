# AI Lead Intelligence Platform with Modern UI
import streamlit as st
import pandas as pd
import json
from scrape import scrape_and_score

# Page Config
st.set_page_config(
    page_title="AI Lead Intelligence Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #2e005b 0%, #4f0080 100%) !important;
    color: #f1f1f1;
}

.header-container {
    background: rgba(255, 255, 255, 0.07);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.main-title {
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(to right, #b06ab3, #4568dc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}
.subtitle {
    font-size: 1.3rem;
    color: #ddd;
}

.input-container, .results-container, .data-card, .download-section {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(20px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    color: #fff;
}

.score-badge {
    display: inline-block;
    padding: 1rem 2rem;
    border-radius: 50px;
    font-weight: bold;
    font-size: 1.5rem;
    animation: pulse 2s infinite;
    margin-bottom: 2rem;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
.score-high { background: #00c6ff; }
.score-medium { background: #ff758c; }
.score-low { background: #fddb92; color: #000; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="main-title">🚀 Lead Genius: AI Powered Website Intelligence</div>
    <p class="subtitle">Enter any website to see how strong it is as a lead. Scored with AI. Visualized beautifully.</p>
</div>
""", unsafe_allow_html=True)

# Input
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 🌐 Enter Website URL")
    url = st.text_input("Website", placeholder="https://example.com", label_visibility="collapsed")
    if st.button("Analyze Website 🚀", use_container_width=True):
        if not url.strip():
            st.error("⚠️ Please enter a valid URL")
        else:
            progress = st.progress(0)
            status = st.empty()
            try:
                status.text("🔍 Scraping site...")
                progress.progress(25)
                result = scrape_and_score(url.strip())
                status.text("🤖 Scoring lead...")
                progress.progress(90)
                status.text("✅ Complete!")
                progress.progress(100)

                score = result['Score']
                badge_class = "score-high" if score >= 7 else "score-medium" if score >= 4 else "score-low"
                emoji = "🔥" if score >= 7 else "⚡" if score >= 4 else "📊"

                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="score-badge {badge_class}">
                    {emoji} Lead Score: {score}/10
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("📧 Emails", len(result.get('Emails', '').split(',')))
                col2.metric("🔗 Socials", len(result.get('Social Links', {})))
                col3.metric("🛠️ Tech", len(result.get('Tech Keywords', [])))
                col4.metric("🌐 Links", len(result.get('All Links', [])))

                if result.get('Emails'):
                    st.markdown('<div class="data-card">', unsafe_allow_html=True)
                    st.markdown("**📧 Emails Found:**")
                    for email in result['Emails'].split(',')[:5]:
                        st.markdown(f"- {email.strip()}")
                    st.markdown('</div>', unsafe_allow_html=True)

                if result.get('Social Links'):
                    st.markdown('<div class="data-card">', unsafe_allow_html=True)
                    st.markdown("**🔗 Social Links:**")
                    for k, v in result['Social Links'].items():
                        st.markdown(f"- [{k.title()}]({v})")
                    st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="download-section">', unsafe_allow_html=True)
                st.markdown("**📁 Download Lead Data:**")
                d1, d2 = st.columns(2)
                with d1:
                    st.download_button("📄 JSON", data=json.dumps(result, indent=2), file_name="lead.json", mime="application/json", use_container_width=True)
                with d2:
                    st.download_button("📊 CSV", data=pd.DataFrame([result]).to_csv(index=False), file_name="lead.csv", mime="text/csv", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                progress.empty()
                status.empty()
                st.error(f"❌ {e}")
