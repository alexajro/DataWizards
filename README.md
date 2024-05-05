# HeyBanco Challenge 2024 - Team DataWizards

Welcome to the GitHub repository for the DataWizards team's submission for the 2024 Datathon. This repository contains all the resources, analyses, and documentation for our project, which focuses on comprehensive data analysis of comments from various platforms.

## Overview

### Challenge Definition

Our project revolves around analyzing a significant dataset of comments sourced from various platforms. The goal is to derive insightful analyses and propose actionable strategies. The scope of the analysis is broad, allowing for flexibility in addressing various areas if the problem is well defined and the solution is effectively articulated, analyzing the data, and scaling the proposals.


## Project Documentation

### Ideation Phase

Our brainstorming session can be accessed through this Canva document:
- [Brainstorming Ideas](https://www.canva.com/design/DAGESbJzl4E/CY9ZLfvFDUQV_iJKFDOoKQ/edit?utm_content=DAGESbJzl4E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Final Presentation

Our final presentation outlining our findings and proposals is available here:
- [Final Presentation](https://www.canva.com/design/DAGESY6ceHs/cvg3EZSEOP5V00WMWE0UpA/edit?utm_content=DAGESY6ceHs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Analysis Insights

### Sentimental Analysis

Located in the `classification_analysis` directory, this analysis seeks to uncover customer sentiments, identifying areas of strength and opportunities for improvement through sentiment categorization and temporal analysis. Visual insights are provided in the form of word clouds and sentiment timelines.

#### Visualization

<div align="center">
    <table>
        <tr>
            <th>X Comments</th>
            <th>Facebook Reviews</th>
        </tr>
        <tr>
            <td><img src='classification_analysis/XReviwes/wordcloud.png' alt='Word Cloud for X Comments' style='width:300px'></td>
            <td><img src='classification_analysis/FacebookReviews/wordcloud.png' alt='Word Cloud for Facebook Reviews' style='width:300px'></td>
        </tr>
        <tr>
            <td><img src='classification_analysis/XReviwes/Tweets por Sentimiento.jpg' alt='Sentiment Analysis for X Comments'  style='width:300px'></td>
            <td><img src='classification_analysis/FacebookReviews/FacebookReviewsPorSentimiento.png' alt='Sentiment Analysis for Facebook Reviews' style='width:300px'></td>
        </tr>
    </table>
</div>

### Topic Analysis

<div align="center">
    <img src='classification_analysis/XReviwes/Tweets por Categoria.png' alt='Topic Analysis for Tweets'>
</div>

### Temporal Analysis

This section delves into the temporal dynamics of comments and reviews. Detailed analyses and visualizations are available in the `temporal_analysis` directory. Key visualizations include hourly heat maps for both Facebook and X comments, showcasing the frequency of interactions over different times of the day.

#### Hourly Heat Maps

The following heat maps illustrate the hourly distribution of comments for a better understanding of user engagement patterns.

<div align="center">
    <table>
        <tr>
            <th>X Comments</th>
            <th>Facebook Reviews</th>
        </tr>
        <tr>
            <td><img src='temporal_analysis/Heat Map for X Comments.jpg' alt='Heat Map for X Comments' style='width:300px'></td>
            <td><img src='temporal_analysis/Heat Map for Facebook Reviews.jpg' alt='Heat Map for Facebook Reviews' style='width:350px'></td>
        </tr>
    </table>
</div>

In addition to the heat maps, due to the limited temporal data available from the X dataset, we expanded our analysis to include a monthly bar graph for Facebook reviews, providing insights into review trends over several months.

#### Monthly Trends in Facebook Reviews

Below is a bar graph depicting monthly trends in Facebook reviews, which helps identify peak periods of user activity and sentiment shifts.

<div align="center">
    <img src='temporal_analysis/Monthly Bar Graph Facebook Reviews.jpg' alt='Monthly Bar Graph for Facebook Reviews' style='width:500px'>
</div>


## Conclusions

Detailed conclusions from our analyses are included in the final presentation document. These conclusions provide strategic insights into customer behavior patterns and recommend actionable steps for business improvement.
