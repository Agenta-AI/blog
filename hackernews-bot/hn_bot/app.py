from hn_bot import hn_scraper, llm_classifier, novu_bot
from time import sleep
interests = "LLM, LLMOps, MLOps, Data science, AI, startups"

done_post_titles = []


def main():
    novu_bot.send_message("Interesting posts at HackerNews:\n")

    posts = []
    for i in range(1, 5):
        posts += hn_scraper.scrape_page(i)
    for post in posts:
        title = post["title"]
        url = post["link"]
        if llm_classifier.classify_post(title, interests) and title not in done_post_titles:
            done_post_titles.append(title)
            novu_bot.send_message(f"{title}\n{url}")


if __name__ == "__main__":
    while True:
        main()
        sleep(3600)
