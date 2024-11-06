# Sentiment Analysis Chatbot

Analyze product reviews for sentiment using OpenAI's GPT models. This application allows users to input a product ID and receive an analysis of customer reviews, identifying top sentiment categories, overall sentiments, common themes, and more.

## Table of Contents
- [Features]()
- [Requirements]()
- [Installation]()
- [Configurations]()
- [Usage]()

## Features


- Sentiment Analysis: Analyze customer reviews to identify sentiments.
- Top Categories: Extract top sentiment categories based on reviews.
- Common Themes: Identify common themes within each sentiment category.
- Example Reviews: Provide example reviews for each category.
- Average Rating: Calculate the average rating for the product.
- Interactive Interface: User-friendly Streamlit app for easy interaction.


## Requirements
- Python: Version 3.7 or higher.
- OpenAI python library
- Streamlit
- Docker

## Installation
1. Clone the Repository

bash
Copy code
git clone https://github.com/ncellepola/ aamzon_sentiment_analysis.git and
cd aamzon_sentiment_analysis


2. Create a Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install Required Packages


```
pip install -r requirements.txt

```


4. Download data set to the /data folder in the project  ( #This is already done, and data is in the /data folder)

```
import kagglehub

# Download latest version
path = kagglehub.dataset_download("arhamrumi/amazon-product-reviews")

print("Path to dataset files:", path)
```

5.  Create a .env File  ( # Already created )
Create a .env file in the root directory of the project and add your API key:

```
OPENAI_API_KEY=your-api-key
```

# Usage

IMPORTANT : Make sure Docker-Desktop is runing

```  docker-compose up --build    ```

Copy and paste the url in the browser

http://0.0.0.0:8501

And try entering productID to see the sentiment

ex- B0009XLVG0, B001GVISJM, B001GVISJM
