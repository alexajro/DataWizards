import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

def load_data(file_path):
    try:
        tweets_df = pd.read_csv(file_path)
        return tweets_df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def sentiment_analysis(tweets_df):
    for tweet in tweets_df['tweet']:
        completion = client.chat.completions.create(
            model="gpt-4-turbo-2024-04-09",
            temperature=0.6,
            messages=[
            {"role": "system", "content": "You are an expert in sentimental analysis. You have a dataset of tweets and you want to perfectly classify the sentiment of the tweets."},
            {"role": "user", "content": f"Classify the sentiment of the tweets between tripple marks in categories: [positive, negative, neutral].\n Return ONLY the category without anything else.\nIf you can't classify the sentiment of the tweet, you can use the category: [neutral].\n\nTweet: {tweet}"},
            ]
        )
        sentiment = completion.choices[0].message.content
        tweets_df.loc[tweets_df['tweet'] == tweet, 'sentiment'] = sentiment
        print(sentiment)
    return tweets_df

def topic_classification(tweet, sentiment):
    if sentiment == 'positive':
        template = f"Classify the topic of the tweet between tripple marks in categories: ['Good things about the app': 0,  'Kudos for good customer service': 1].\n Return ONLY the number of the category without anything else.\nIf you can't classify the topic of the tweet, you can use the category: ['Others': 2].\n\nTweet: '''{tweet}''' "
    elif sentiment == 'negative':
        template = f"Classify the topic of the tweet between tripple marks in categories: ['Problems with the app': 3,  'Problems with customer service': 4, 'Problems with products': 5].\n Return ONLY the number of the category without anything else.\nIf you can't classify the topic of the tweet, you can use the category: ['Others': 6].\n\nTweet: '''{tweet}''' "
    
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        temperature=0.6,
        messages=[
        {"role": "system", "content": "You are an expert in topic analysis. You have a dataset of tweets and you want to perfectly classify the topic of the tweets."},
        {"role": "user", "content": f"{template}\n\nTweet: {tweet}"},
        ]
    )
    category = completion.choices[0].message.content
    print(category)
    return category


def main():
    # Load data
    db_path = r'C:\Users\dilan\Documents\Github\DataWizards\classification_analysis\FacebookReviews\FacebookReviews.csv'
    tweets_df = load_data(db_path)
    
    # Sentiment analysis
    tweets_df = sentiment_analysis(tweets_df)

    # # Adding a 'category' column if not already present (initialize as None)
    # if 'category' not in tweets_df.columns:
    #     tweets_df['category'] = None

    # # Topic classification with sentiment analysis
    # for idx, row in tweets_df.iterrows():
    #     sentiment = row['sentiment']
    #     if sentiment == 'positive':
    #         category = topic_classification(row['tweet'], 'positive')
    #         tweets_df.at[idx, 'category'] = category
    #     elif sentiment == 'negative':
    #         category = topic_classification(row['tweet'], 'negative')
    #         tweets_df.at[idx, 'category'] = category
    #     else:# Optionally handle neutral or other sentiments if necessary
    #         print(f"Skipping row with sentiment: neutral. No topic classification needed.")

    #     # Print progress every 100 iterations to monitor progress without too much clutter
    #     print(f"Processed {idx+1} rows")
    
    new_db_path = r'C:\Users\dilan\Documents\Github\DataWizards\classification_analysis\FacebookReviews\FacebookReviews_classified.csv'
    tweets_df.to_csv(new_db_path, index=False)
    print("Data saved to", new_db_path)



if __name__ == '__main__':
    try:
        # Load LLM API key and instance client
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        client = OpenAI(api_key=api_key)
        main()
    except Exception as e:
        print(f"Error: {e}")