# Word Cloud and Classification

## Overview

This directory aims to analyze customer tweets and identify the most frequently mentioned words, as well as classify the tweets into positive and negative categories. The classification helps prioritize efforts and address critical issues or highlight areas of excellence.

# Comment Analysis and Classification

To facilitate a comprehensive understanding of comments and their analysis, we have opted to obtain an additional database of comments from Facebook through the free version of the Facebook scraper [Apify](https://apify.com/). Consequently, we have two separate analyses for comparative purposes, each residing in a different directory within the `classification_analysis` directory.

The codebase for word cloud generation, sentiment analysis, and topic classification remains substantially similar across both analyses. The sole difference lies in the file path for the respective databases. This design choice ensures scalability, allowing for the seamless integration of new databases by simply modifying the relevant file path.

## Directory Structure

- `classification_analysis/`
    - `original_comments/`
        - `diff_words.csv`
        - `Base_HeyBanco.csv`
        - `Base_HeyBanco_Classified.csv`
        - `...`
        
    - `facebook_comments/`
        - `diff_words.csv`
        - `FacebookReviews.csv`
        - `FacebookRewiews_classified.csv`
        - `...`
    - `word_cloud.py`
    - `sentiment_analysis.py`
    - `topic_classification.py`

## Usage

To analyze a new database, follow these steps:

1. Place the new database file(s) in the `classification_analysis/` directory.
2. Modify the file path(s) in the relevant scripts (`wordCloud.py`, `banks_counter.py`, `classifier.py`, etc.) to point to the new database file(s).
3. Run the scripts as needed.

By adhering to this structure and methodology, we ensure a consistent and scalable approach to comment analysis and classification, enabling efficient comparisons and insights across multiple data sources.

## Process

1. **Data Cleaning**: The first step involved cleaning the raw data from the database to prepare it for analysis.

2. **Word Count**: A script was written to count the occurrences of each word in the cleaned data. The word counts were stored in a JSON file named `word_count.json`.

3. **Word Cloud Generation**: To visualize the most common words, a CSV file named `diff_words.csv` was created from the word count data. This file was then used as input for the [WordClouds](https://www.wordclouds.com/) website to generate a word cloud image.

4. **Classification**: An LLM (Language Learning Model) was employed to classify the customer feedback into the following categories:

<p align="center">

| Sentiment | Topics | Identifier |
|-----------|--------|-------|
| **Positive** | Good things about the app | 0 |
|           | Kudos for good customer service | 1 |
|           | Others | 2 |
| **Negative** | Problems with the app | 3 |
|           | Problems with customer service | 4 |
|           | Problems with products | 5 |
|           | Others | 6 |

</p>

## Benefits

- **Prioritization**: By identifying the most frequently mentioned words and classifying feedback as positive or negative, the team can prioritize efforts and address critical issues or areas of excellence.
- **Visualization**: The word cloud provides a visual representation of the most common words, making it easier to identify popular topics or concerns.
- **Targeted Improvements**: The classification of feedback into positive and negative categories allows for targeted improvements in specific areas, such as product development or customer service.

## Future Enhancements
- Incorporate additional data sources for a more comprehensive analysis such as Facebook post's, Reddit comments and extensive X dataframe.
- Develop interactive visualizations or dashboards for easier data exploration.

Please note that this README provides an overview of this directory. For more detailed information or specific implementation details, refer to the project documentation or codebase.
