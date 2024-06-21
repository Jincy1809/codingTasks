# Import libraries and modules
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load in .csv file and convert to a pandas dataframe
df = pd.read_csv("amazon_product_reviews.csv")

# Preprocess the text data
# Select the relevant column and retrieve its data
# This column 'reviews.text' represents the feature variable containing the product reviews we will use for sentiment analysis
reviews_data = df['reviews.text']

# Remove all missing values that contain NaN in the reviews.text column
clean_data = df['reviews.text'].dropna()

# Load the spacy model to perform nlp
nlp = spacy.load('en_core_web_sm')

# Add text blob to the pipeline of the nlp, so we can get polarity. 
"""
Polarity is preferred here since the reviews are unlabelled, 
making it difficult to predict sentiment based on similarity.
"""
nlp.add_pipe('spacytextblob')

# Create a function for sentiment analysis
# Define a function that takes a product review as input and predicts its sentiment
def sentiment_prediction(review):
    # Process the review text using SpaCy
    doc = nlp(review)

    # Remove stop words, convert to lowercase, and strip whitespace.
    clean_tokens = [token.text.lower().strip() for token in doc if not token.is_stop]

    # Join cleaned tokens back into a string
    cleaned_review = ' '.join(clean_tokens)

    # Process the cleaned review text using SpaCy
    cleaned_doc = nlp(cleaned_review)

    # Get the polarity
    polarity = cleaned_doc._.blob.polarity

    # Set a threshold for polarity score which determines if something is positive, negative or neutral
    # We shall select a value of 0.3333333333 to split the three categories evenly. One can increase these values if
        # one wants to see only strong sentiment scores appear for positive and negative.
    if polarity >= 0.3333333333:
        return 'Positive'
    elif polarity <= -0.3333333333:
        return 'Negative'
    else:
        return 'Neutral'  # Anything not in the range is neutral


# Apply the cleaning steps to the entire clean_data variable
cleaned_reviews_data = clean_data.apply(sentiment_prediction)

# Test model on sample product reviews
sample_product_reviews = ["I absolutely love this product. It's amazing!",
                  "The product was average and delivery was slow. Ok at best.",
                  "I hated this! Never buying again.",
                  "I liked it... Maybe a bit over priced but a good product overall.",
                  "Would recommend to a friend."]

# Verifying accuracy in predicting sentiment
# Loop through each review and print sentiment
for sample_review in sample_product_reviews:
    predicted_sentiment = sentiment_prediction(sample_review)
    print(f'The predicted sentiment is: {predicted_sentiment}')