# src/chatbot.py

from src.data_loader import DataLoader
from src.sentiment_analyzer import SentimentAnalyzer

class Chatbot:
    def __init__(self, data_loader, sentiment_analyzer):
        self.data_loader = data_loader
        self.sentiment_analyzer = sentiment_analyzer

    def start(self):
        while True:
            product_id = input("User: Analyze reviews for <product_id> (or type 'exit' to quit): ")
            if product_id.lower() == 'exit':
                print("Bot: Thank you for using the sentiment analysis chatbot!")
                break

            print(f"Bot: Analyzing the latest reviews for {product_id}...")
            reviews = self.data_loader.filter_reviews(product_id)

            if reviews.empty:
                print("Bot: No recent reviews found for this product.")
                continue

            analysis = self.sentiment_analyzer.analyze_reviews(reviews)
            if analysis:
                print(f"Bot: Based on {product_id} reviews, here are the top sentiments:")
                print(analysis)
            else:
                print("Bot: Sorry, an error occurred during analysis.")

            continue_prompt = input("Bot: Would you like to analyze another product? (yes/no): ")
            if continue_prompt.lower() != 'yes':
                print("Bot: Goodbye!")
                break
