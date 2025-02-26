# main_bot.py

from flask import Flask, render_template, request
import logging


class MainBot:
    def __init__(self):
        self.app = Flask(__name__)
        self.bots = {
            "blog_writer": "AI Content Generation & Marketing Bots/blog_writer_bot/app.py",
            "content_moderation": "AI Content Generation & Marketing Bots/content_moderation_bot/image_moderator.py",
            "ad_generator": "AI E-Commerce Automation/ad_generator_bot/ad_generator.py",
            "crypto_grid": "AI Trading Bots/crypto_grid_bot/app.py",
            "identity_protection": "AI-Powered Cybersecurity & Ethical Hacking Tool/identity_protection_bot/monitor.py"
        }

    def access_bot(self, bot_name):
        if bot_name in self.bots:
            # Logic to access the specific bot
            print(f"Accessing {bot_name} bot...")
            # Here you would import and run the bot's functionality
        else:
            print("Bot not found.")

    def access_bot(self, bot_name):
        if bot_name in self.bots:
            # Logic to access the specific bot
            print(f"Accessing {bot_name} bot...")
            # Here you would import and run the bot's functionality
        else:
            print("Bot not found.")

    def run(self):
        @self.app.route('/access_bot')
        def access_bot_route():
            bot_name = request.args.get('name')
            self.access_bot(bot_name)
            return f"Accessed {bot_name} bot."
        def access_bot_route():
            bot_name = request.args.get('name')
            self.access_bot(bot_name)
            return f"Accessed {bot_name} bot."
        @self.app.route('/')
        def index():
            return render_template('index.html')  # Main dashboard

        self.app.run(debug=True)

if __name__ == "__main__":
    main_bot = MainBot()
    main_bot.run()
    def __init__(self):
        self.bots = {
            "blog_writer": "AI Content Generation & Marketing Bots/blog_writer_bot/app.py",
            "content_moderation": "AI Content Generation & Marketing Bots/content_moderation_bot/image_moderator.py",
            "ad_generator": "AI E-Commerce Automation/ad_generator_bot/ad_generator.py",
            "crypto_grid": "AI Trading Bots/crypto_grid_bot/app.py",
            "identity_protection": "AI-Powered Cybersecurity & Ethical Hacking Tool/identity_protection_bot/monitor.py"
        }

    def access_bot(self, bot_name):
        if bot_name in self.bots:
            # Logic to access the specific bot
            print(f"Accessing {bot_name} bot...")
            # Here you would import and run the bot's functionality
        else:
            print("Bot not found.")

if __name__ == "__main__":
    main_bot = MainBot()
    # Example of accessing a bot
    main_bot.access_bot("blog_writer")
