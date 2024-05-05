# Word Cloud and Classification

## Overview

This directory aims to analyze customer tweets and identify the most frequently mentioned words, as well as classify the tweets into positive and negative categories. The classification helps prioritize efforts and address critical issues or highlight areas of excellence.

## Process

1. **Data Cleaning**: The first step involved cleaning the raw data from the database to prepare it for analysis.

2. **Word Count**: A script was written to count the occurrences of each word in the cleaned data. The word counts were stored in a JSON file named `word_count.json`.

3. **Word Cloud Generation**: To visualize the most common words, a CSV file named `diff_words.csv` was created from the word count data. This file was then used as input for the [WordClouds](https://www.wordclouds.com/) website to generate a word cloud image.
<p align="center">
<img src="wordcloud.png" alt="WordCloud from Data Base" style="width:500px;height:auto;">
</p>

4. **Classification**: An LLM (Language Learning Model) was employed to classify the customer feedback into the following categories:
    - **Positive**
        - Good things about the app
        - Kudos for good customer service
    - **Negative**
        - Problems with the app
        - Problems with customer service

## Benefits

- **Prioritization**: By identifying the most frequently mentioned words and classifying feedback as positive or negative, the team can prioritize efforts and address critical issues or areas of excellence.
- **Visualization**: The word cloud provides a visual representation of the most common words, making it easier to identify popular topics or concerns.
- **Targeted Improvements**: The classification of feedback into positive and negative categories allows for targeted improvements in specific areas, such as product development or customer service.

## Future Enhancements

- Implement sentiment analysis to further refine the classification of feedback.
- Incorporate additional data sources for a more comprehensive analysis.
- Develop interactive visualizations or dashboards for easier data exploration.

Please note that this README provides an overview of this directory. For more detailed information or specific implementation details, refer to the project documentation or codebase.