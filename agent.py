import threading
from flask import Flask
import os
import time

# Unga original functions/imports
from news_fetch import get_news
from ai_report import generate_report
from word_report import create_doc
from email_send import send_email

# --- Render-gaga oru Dummy Flask Web Server ---
app = Flask(__name__)

@app.route('/')
def home():
    return "AI News Agent is running smoothly in the background!"

def run_flask():
    # Render supply panra Port-la server-a run panrom
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
# ----------------------------------------------

def main():
    print("\n🔄 Fetching AI News...\n")

    news = get_news()

    print("=" * 80)
    print("TOP 10 AI NEWS HEADLINES")
    print("=" * 80)

    for i, item in enumerate(news, 1):
        print(f"\n{i}. {item['title']}")
        print(f"Link: {item['link']}")

    titles = [n["title"] for n in news]

    print("\n🧠 Generating AI Report...\n")

    ai_text = generate_report(titles)

    print("=" * 80)
    print("OVERALL SUMMARY & HIGHLIGHTS")
    print("=" * 80)
    print(ai_text)

    print("\n📄 Creating Word Report...")
    file_path = create_doc(news, ai_text)

    print("📧 Sending Email...")
    send_email(file_path, news)

    print("\n🎉 DONE SUCCESSFULLY!")

if __name__ == "__main__":
    # 1. First, Flask server-a oru thani thread-la background-la start panrom
    # Idhanala Render port check pass aagidhum, error varadhu!
    threading.Thread(target=run_flask, daemon=True).start()
    
    # 2. Unga original AI Agent code-a run panrom
    main()
    
    # 3. Code mudinjadhuku அப்றம் Render service closed aagama iruka continuous keep-alive loop
    print("\n💤 AI Agent entering background sleep mode...")
    while True:
        time.sleep(3600)