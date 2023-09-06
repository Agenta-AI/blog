# HackerNews AI Bot 🤖

This repository contains a Python-based AI bot designed to notify you of interesting posts on Hacker News, tailored to your interests. 

To see how this bot was built, and how to use it, check out the [accompanying blog post](https://www.novu.com/blog/ai-bot-hacker-news/).

By leveraging Beautifulsoup for web scraping, Agenta with GPT3.5 for AI processing, and Novu integrated with Discord for notifications, this bot reduces the need to constantly check Hacker News, ensuring you never miss out on relevant articles.

## Features

- **Automated Scanning:** Set to check Hacker News every hour.
- **Custom Alerts:** Based on your predefined interests.
- **Discord Notifications:** Get direct links to the articles you care about in your Discord channel.

## Quick Start

To set up the bot:

1. Update `novu_bot.py` with the required credentials:
   ```python
   NOVU_API_KEY = "<Your_Novu_API_Key>"
   WEBHOOK_URL = "<Your_Discord_Webhook_URL>"
   ```

2. In `llm_classifier.py`, set the Agenta endpoint:
   ```python
   AGENTA_ENDPOINT = "<Your_Agenta_Endpoint_URL>"
   ```

3. Install the required packages:
   ```bash
   poetry install
   ```
4. Run the bot:
   ```bash
   python app.py
   ```

## License

[MIT](https://opensource.org/licenses/MIT)

---

If you find this project useful, please consider us a ⭐ on GitHub! https://github.com/agenta-ai/agenta. 
Your support means a lot!

