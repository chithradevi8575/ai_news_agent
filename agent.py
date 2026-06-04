from news_fetch import get_news
from ai_report import generate_report
from word_report import create_doc
from email_send import send_email

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
    main()