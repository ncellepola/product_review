# src/sentiment_analyzer.py
from openai import OpenAI
import os
import json
import ast

class SentimentAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def analyze_reviews(self, reviews):
        # Limit to 10 reviews or fewer
        reviews = reviews.head(10)
        reviews_text = "\n".join([f"- {text}" for text in reviews['Text']])

        print("\n=== Reviews Being Sent to LLM ===")
        print(reviews_text)
        print("=================================\n")

        # First LLM call: Identify top 3 sentiment categories
        categories = self.get_top_categories(reviews_text)

        if not categories:
            print("No categories were identified.")
            return None

        # Initialize results
        analysis = {
            "Product_ID": reviews['ProductId'].iloc[0] if 'ProductId' in reviews.columns else "N/A",
            "total_reviews": len(reviews),
            "average_rating": reviews['Score'].mean(),
            "top_sentiments": []
        }

        # For each category, get detailed analysis
        for category in categories:
            sentiment_detail = self.get_category_sentiment(reviews_text, category)
            if sentiment_detail:
                analysis['top_sentiments'].append(sentiment_detail)
            else:
                print(f"Failed to get sentiment details for category: {category}")

        return analysis

    def get_top_categories(self, reviews_text):
        prompt = (
            "From the following product reviews, identify the top 3 sentiment categories as a Python list.\n\n"
            "Reviews:\n"
            f"{reviews_text}\n\n"
            "Provide the list in this format:\n"
            '["Category1", "Category2", "Category3"]\n'
            "If fewer than 3 categories are found, provide as many as are available."
        )

        print("\n=== Prompt for Top Categories ===")
        print(prompt)
        print("=================================\n")

        try:
            response = self.client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.7)

            categories_text = response.choices[0].message.content.strip()
            print("\n=== Response for Top Categories ===")
            print(categories_text)
            print("===================================\n")

            # Parse the categories from the response
            categories = ast.literal_eval(categories_text)
            if isinstance(categories, list):
                return categories
            else:
                print("Parsed categories are not a list.")
                return []
        except Exception as e:
            print(f"Error getting categories: {e}")
            return []

    def get_category_sentiment(self, reviews_text, category):
        prompt = (
            f"Analyze the sentiment for the category '{category}' in the following product reviews.\n\n"
            "For this category, provide:\n"
            "- Overall sentiment (positive/negative/mixed)\n"
            "- Common themes as a list\n"
            "- An example review\n"
            "- Confidence score as a percentage\n\n"
            "Reviews:\n"
            f"{reviews_text}\n\n"
            "Provide the output in valid JSON format as shown below:\n"
            "{{\n"
            '  "category": "{category}",\n'
            '  "sentiment": "positive/negative/mixed",\n'
            '  "confidence": number,\n'
            '  "themes": ["string"],\n'
            '  "example_review": "string"\n'
            "}}"
        )

        print(f"\n=== Prompt for Category '{category}' ===")
        print(prompt)
        print("========================================\n")

        try:
            response = self.client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.7)
            sentiment_text = response.choices[0].message.content.strip()
            print(f"\n=== Response for Category '{category}' ===")
            print(sentiment_text)
            print("===========================================\n")

            # Parse the JSON output
            sentiment_detail = json.loads(sentiment_text)
            return sentiment_detail
        except json.JSONDecodeError as jde:
            print(f"JSON decoding error for category '{category}': {jde}")
            return None
        except Exception as e:
            print(f"Error getting sentiment for category '{category}': {e}")
            return None
