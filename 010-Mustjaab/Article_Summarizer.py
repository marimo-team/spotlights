# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "beautifulsoup4==4.12.3",
#     "nltk==3.9.1",
#     "requests==2.32.3",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(rf"<h1><center> Summarize that Article! </h1> </center></h1>")
    return


@app.cell
def __():
    import marimo as mo
    import nltk
    import requests
    from bs4 import BeautifulSoup
    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.probability import FreqDist
    from nltk.corpus import stopwords
    from string import punctuation
    import heapq
    return (
        BeautifulSoup,
        FreqDist,
        SentimentIntensityAnalyzer,
        heapq,
        mo,
        nltk,
        punctuation,
        requests,
        sent_tokenize,
        stopwords,
        word_tokenize,
    )


@app.cell
def __(mo):
    Article = mo.ui.text(label='Article:',
                         value="https://www.cbc.ca/news/politics/hackers-threat-national-security-1.6949645").form()

    Points = mo.ui.number(5,10,label='Number of Bullet Points:')
    return Article, Points


@app.cell
def __(Article, Points, mo):
    mo.hstack([
        Article,
        Points
    ])
    return


@app.cell
def __(Article, mo):
    mo.stop(Article.value is None, mo.md("Submit an article continue"))
    return


@app.cell
def __(Article, BeautifulSoup, requests):
    Article_url = Article.value

    def CBC_article_reader(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the HTML elements containing the news article content
            article_content = soup.find('div', class_='story')

            # Extract text from the article content
            text = article_content.get_text(separator=' ')
            return text
    return Article_url, CBC_article_reader


@app.cell
def __(Article_url, CBC_article_reader):
    article_text = CBC_article_reader(Article_url)
    return (article_text,)


@app.cell
def __(
    FreqDist,
    Points,
    SentimentIntensityAnalyzer,
    article_text,
    heapq,
    punctuation,
    sent_tokenize,
    stopwords,
    word_tokenize,
):
    tokens = word_tokenize(article_text.lower())  


    stop_words = set(stopwords.words('english') + list(punctuation))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Step 3: Calculate word frequencies
    word_freq = FreqDist(filtered_tokens)


    tfidf = {}
    for word, freq in word_freq.items():
        tfidf[word] = freq * (len(tokens) / word_freq[word])


    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(article_text)['compound']


    summary = []
    sentences = sent_tokenize(article_text)


    sentence_scores = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        score = sentiment_score * sum(tfidf[word] for word in words if word in tfidf)
        sentence_scores[sentence] = score

    num_sentences_in_summary = Points.value  
    summary_sentences = heapq.nlargest(num_sentences_in_summary, sentence_scores, key=sentence_scores.get)


    bulleted_summary = ['- ' + sentence for sentence in summary_sentences]
    final_summary = '\n'.join(bulleted_summary)
    return (
        bulleted_summary,
        filtered_tokens,
        final_summary,
        freq,
        num_sentences_in_summary,
        score,
        sentence,
        sentence_scores,
        sentences,
        sentiment_score,
        sia,
        stop_words,
        summary,
        summary_sentences,
        tfidf,
        tokens,
        word,
        word_freq,
        words,
    )


@app.cell
def __(mo):
    mo.md("""<h2> Final Summary </h2>""")
    return


@app.cell
def __(final_summary, mo):
    mo.md(rf"{final_summary}")
    return


if __name__ == "__main__":
    app.run()
