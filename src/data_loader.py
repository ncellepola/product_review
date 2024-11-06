# src/data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("Data file not found.")
            self.data = pd.DataFrame()

    def filter_reviews(self, product_id, num_reviews=10):
        if self.data is None:
            self.load_data()

        # Filter by ProductId and make a copy
        product_reviews = self.data[self.data['ProductId'] == product_id].copy()
        print(f"Total reviews for product {product_id}: {len(product_reviews)}")

        # Handle missing or incomplete reviews
        product_reviews = product_reviews.dropna(subset=['Text', 'Score'])

        # Get up to num_reviews
        selected_reviews = product_reviews.head(num_reviews)

        return selected_reviews[['ProductId', 'Score', 'Text', 'Time']]
