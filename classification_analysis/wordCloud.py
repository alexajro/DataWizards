from collections import Counter
import re
import pandas as pd
import json
from unidecode import unidecode

def count_words_excluding_punctuation_and_conjunctions(tweets):
    # Combine all tweets into one large string
    all_tweets = ' '.join(tweets)
    # Split the string by any whitespace character, keeping emojis intact
    # Updated regex to better capture words and emojis, exclude punctuations directly
    words = re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+|\ud83c[\udf00-\udfff]|\ud83d[\udc00-\ude4f]|\ud83d[\ude80-\udeff]', all_tweets)
    
    # Define a set of unwanted characters (punctuation and common conjunctions)
    conjunctions = set([
        "y", "e", "ni", "que", "pero", "mas", "sino", "aunque", "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", 
        "en", "entre", "hacia", "hasta", "para", "por", "según", "sin", "so", "sobre", "tras", "durante", "mediante", "excepto", 
        "salvo", "incluso", "más", "menos", "mi", "el", "la", "un", "me", "ya", "es", "los", "te", "se", "su", "al", "del", "las", 
        "como", "muy", "tu", "dia", "también", "esta", "le", "les", "lo", "si", "no", "una", "uno", "o", "porque", "cuando", 
        "donde", "cual", "quien", "cómo", "qué", "quién", "cuál", "tengo", "son", "estoy", "hay", "he", "ha", "era", "fue", "ser", 
        "tener", "hacer", "poder", "decir", "este", "ese", "aquel", "estos", "esos", "aquellos", "muchas", "muchos", "poco", "pocos", 
        "algún", "alguna", "algunos", "algunas", "ningún", "ninguna", "ningunos", "ningunas", "mucho", "toda", "todo", "todas", "todos", 
        "varios", "varias", "cada", "tal", "cuyo", "cuya", "cuyos", "cuyas", "otro", "otra", "otros", "otras", "", "jajaja", "hey", "gracias", "tus", "anos", "heybanco", "yo", "saludos",
    "hola", "banco"
    ])
    
    # Remove unwanted characters and conjunctions
    filtered_words = [unidecode(word.lower()) for word in words if unidecode(word.lower()) not in conjunctions]
    
    # Count words and emojis
    word_counts = Counter(filtered_words)
    # Sort by count in descending order
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_counts

# Load the tweets
tweets_df = pd.read_csv(r'C:\Users\dilan\Documents\Github\DataWizards\classification_analysis\Base_HeyBanco.csv')

# Perform the modified word count
modified_word_count_result = count_words_excluding_punctuation_and_conjunctions(tweets_df['tweet'])

# Convert to JSON
modified_word_count_json = json.dumps(modified_word_count_result, ensure_ascii=False)

# Save the result to a JSON file
modified_word_count_path = 'word_count.json'
diff_words = 'diff_words.csv'
with open(modified_word_count_path, 'w', encoding='utf-8') as f:
    f.write(modified_word_count_json)

# Save the top words to a CSV file for easy input in word cloud generators
with open(diff_words, 'w', encoding='utf-8') as f:
    for word, count in modified_word_count_result.items():
        if count > 3:
            f.write(str(count) + ',' + word + '\n')

# Print the top 10 words and their counts
print("Top words and counts:")
for i in range(10):
    print(list(modified_word_count_result.keys())[i], list(modified_word_count_result.values())[i])
