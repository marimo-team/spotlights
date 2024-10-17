# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
#     "nltk==3.9.1",
#     "textstat==0.7.4",
# ]
# ///
import marimo

__generated_with = "0.9.1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import collections
    import math
    import nltk
    import textstat
    return collections, math, mo, nltk, pd, textstat


@app.cell(disabled=True)
def __(nltk):
    nltk.download('averaged_perceptron_tagger')
    return


@app.cell
def __(mo):
    mo.md(r"""#Exploring Perplexity""")
    return


@app.cell
def __(mo):
    Story_Generator = mo.ui.chat(
        mo.ai.llm.openai("gpt-4o"),
        prompts=[
            "Write a psychological thriller short story",
            "Write a horror short story",
            "Write a comedic short story",
        ],
        show_configuration_controls=True
    )
    Story_Generator
    return (Story_Generator,)


@app.cell
def __(mo):
    mo.callout("Cutomize the response you would like through modifying paramaters in the configuration", kind ='info')
    return


@app.cell
def __(Story_Generator, pd):
    Chat_Log = pd.DataFrame(Story_Generator.value)
    return (Chat_Log,)


@app.cell
def __(Chat_Log, mo):
    Story_from_Model_df = mo.sql(
        f"""
        SELECT *
        From Chat_Log
        """, output=False
    )
    return (Story_from_Model_df,)


@app.cell
def __(Story_from_Model_df, collections):
    def preprocess(text):
        return text.lower().split()

    tokens = preprocess(Story_from_Model_df['content'][1])

    def build_ngrams(tokens, n):
        ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
        return collections.Counter(ngrams)

    unigrams = build_ngrams(tokens, 1)
    bigrams = build_ngrams(tokens, 2)

    def calc_prob(ngram_count, n_minus_1_gram_count):
        probabilities = {}
        for ngram in ngram_count:
            context = ngram[:-1]
            probabilities[ngram] = ngram_count[ngram] / n_minus_1_gram_count[context] 
        return probabilities
    return bigrams, build_ngrams, calc_prob, preprocess, tokens, unigrams


@app.cell
def __(bigrams, calc_prob, unigrams):
    probabilities = calc_prob(bigrams, unigrams)
    return (probabilities,)


@app.cell
def __(math):
    def perplexity(probabilities, tokens, n):
        N = len(tokens)
        log_prob_sum = 0
        for i in range(n-1, N):
            ngram = tuple(tokens[i-n+1:i+1])
            prob = probabilities.get(ngram, 1e-10)  # Use a small value if probability is zero
            log_prob_sum += math.log(prob)
        return math.exp(-log_prob_sum / N)
    return (perplexity,)


@app.cell
def __(mo, perplexity, probabilities, tokens):
    perplexity_value = perplexity(probabilities, tokens, 2)

    mo.md(rf"Perplexity: {perplexity_value}")
    return (perplexity_value,)


@app.cell
def __(nltk, textstat):
    def calculate_fluency(text):
        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)

        pos_counts = {
            'nouns': sum(1 for word, pos in tagged if pos.startswith('NN')),
            'verbs': sum(1 for word, pos in tagged if pos.startswith('VB')),
            'adjectives': sum(1 for word, pos in tagged if pos.startswith('JJ')),
            'adverbs': sum(1 for word, pos in tagged if pos.startswith('RB'))
        }

        readability_score = textstat.flesch_reading_ease(text)

        fluency_score = (readability_score + sum(pos_counts.values())) / 2

        return {
            "fluency_score": fluency_score,
            "readability": readability_score,
            "pos_counts": pos_counts
        }
    return (calculate_fluency,)


@app.cell
def __(Story_from_Model_df, calculate_fluency, pd):
    fluency_results = calculate_fluency(Story_from_Model_df['content'][1])
    Fluency = pd.DataFrame(fluency_results)
    Fluency
    return Fluency, fluency_results


if __name__ == "__main__":
    app.run()
