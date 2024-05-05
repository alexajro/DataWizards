import pandas as pd
import json

# Define the potential competence banks
banks = ["nu ", "bbva", "santander", "rappicard", "hsbc", "citibanamex", "banamex", "uala", "uala_mex", "nubank", "bancomer", "bancoppel", "banregio", "afirme"]

# Load the tweets
tweets_df = pd.read_csv(r'C:\Users\dilan\Documents\Github\DataWizards\classification_analysis\Base_HeyBanco.csv')

# Count the number of tweets that mention each bank
bank_counts = {bank: 0 for bank in banks}

for tweet in tweets_df['tweet']:
    for bank in banks:
        if bank in tweet.lower():
            bank_counts[bank] += 1

# Sort by count in descending order
sorted_bank_counts = dict(sorted(bank_counts.items(), key=lambda item: item[1], reverse=True))

# Print the results
print("Bank mentions:")
other_mention_count = 0
for bank, count in sorted_bank_counts.items():
    print(bank, count)
    other_mention_count += count
print("Total times other banks mentioned:", other_mention_count)

# Convert to JSON
bank_counts_json = json.dumps(bank_counts, ensure_ascii=False)
with open('banks.json', 'w', encoding='utf-8') as f:
    f.write(bank_counts_json)

# Compute the percentage of tweets that mention any bank
total_tweets = len(tweets_df)
other_mention_count = 0

for tweet in tweets_df['tweet']:
    if any(bank in tweet.lower() for bank in banks):
        other_mention_count += 1

percentage = other_mention_count / total_tweets * 100
print("Percentage of tweets that mention any bank:", round(percentage,2), "%")