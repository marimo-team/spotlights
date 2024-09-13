import marimo

__generated_with = "0.4.2"
app = marimo.App()


@app.cell
def __(battles):
    battles
    return


@app.cell
def __(math, np, pd):
    def compute_mle_elo(df, SCALE=400, BASE=10, INIT_RATING=1000):
        from sklearn.linear_model import LogisticRegression
        models = pd.concat([df["model_a"], df["model_b"]]).unique()
        models = pd.Series(np.arange(len(models)), index=models)

        # duplicate battles
        df = pd.concat([df, df], ignore_index=True)
        p = len(models.index)
        n = df.shape[0]

        X = np.zeros([n, p])
        X[np.arange(n), models[df["model_a"]]] = +math.log(BASE)
        X[np.arange(n), models[df["model_b"]]] = -math.log(BASE)

        # one A win => two A win
        Y = np.zeros(n)
        Y[df["winner"] == "model_a"] = 1.0

        # one tie => one A win + one B win
        # find tie + tie (both bad) index
        tie_idx = (df["winner"] == "tie") | (df["winner"] == "tie (bothbad)")
        tie_idx[len(tie_idx)//2:] = False
        Y[tie_idx] = 1.0

        lr = LogisticRegression(fit_intercept=False, penalty=None, tol=1e-8)
        lr.fit(X,Y)

        elo_scores = SCALE * lr.coef_[0] + INIT_RATING

        # set anchor as mixtral = 1114
        if "mixtral-8x7b-instruct-v0.1" in models.index:
            elo_scores += 1114 - elo_scores[models["mixtral-8x7b-instruct-v0.1"]]
        return pd.Series(elo_scores, index = models.index).sort_values(ascending=False)
    return compute_mle_elo,


@app.cell
def __(pd, tqdm):
    def get_bootstrap_result(battles, func_compute_elo, num_round):
        rows = []
        for i in tqdm(range(num_round), desc="bootstrap"):
            rows.append(func_compute_elo(battles.sample(frac=1.0, replace=True)))
        df = pd.DataFrame(rows)
        return df[df.median().sort_values(ascending=False).index]
    return get_bootstrap_result,


@app.cell
def __(defaultdict):
    def compute_online_elo(battles, K=4, SCALE=400, BASE=10, INIT_RATING=1000):
        rating = defaultdict(lambda: INIT_RATING)

        for rd, model_a, model_b, winner in battles[['model_a', 'model_b', 'winner']].itertuples():
            ra = rating[model_a]
            rb = rating[model_b]
            ea = 1 / (1 + BASE ** ((rb - ra) / SCALE))
            eb = 1 / (1 + BASE ** ((ra - rb) / SCALE))
            if winner == "model_a":
                sa = 1
            elif winner == "model_b":
                sa = 0
            elif winner == "tie" or winner == "tie (bothbad)":
                sa = 0.5
            else:
                raise Exception(f"unexpected vote {winner}")
            rating[model_a] += K * (sa - ea)
            rating[model_b] += K * (1 - sa - eb)

        # calibrate llama-13b to 800
        delta = (800-rating["llama-13b"])
        for model in battles["model_a"].unique():
            rating[model] += delta

        return rating
    return compute_online_elo,


@app.cell
def __(battles, compute_online_elo, pd):
    def preety_print_model_ratings(ratings):
        df = pd.DataFrame([
            [n, ratings[n]] for n in ratings.keys()
        ], columns=["Model", "Elo rating"]).sort_values("Elo rating", ascending=False).reset_index(drop=True)
        # df["Elo rating"] = (df["Elo rating"] + 0.5).astype(int)
        df.index = df.index + 1
        return df

    online_elo_ratings = compute_online_elo(battles)
    preety_print_model_ratings(online_elo_ratings)
    return online_elo_ratings, preety_print_model_ratings


@app.cell
def __(battles, compute_mle_elo, preety_print_model_ratings):
    elo_mle_ratings = compute_mle_elo(battles)
    preety_print_model_ratings(elo_mle_ratings)
    return elo_mle_ratings,


@app.cell
def __(battles, compute_mle_elo, get_bootstrap_result, np):
    BOOTSTRAP_ROUNDS = 100

    np.random.seed(42)
    bootstrap_elo_lu = get_bootstrap_result(battles, compute_mle_elo, BOOTSTRAP_ROUNDS)
    return BOOTSTRAP_ROUNDS, bootstrap_elo_lu


@app.cell
def __(defaultdict, np, pd):
    def predict_win_rate(elo_ratings, SCALE=400, BASE=10, INIT_RATING=1000):
        names = sorted(list(elo_ratings.keys()))
        wins = defaultdict(lambda: defaultdict(lambda: 0))
        for a in names:
            for b in names:
                ea = 1 / (1 + BASE ** ((elo_ratings[b] - elo_ratings[a]) / SCALE))
                wins[a][b] = ea
                wins[b][a] = 1 - ea

        data = {
            a: [wins[a][b] if a != b else np.NAN for b in names]
            for a in names
        }

        df = pd.DataFrame(data, index=names)
        df.index.name = "model_a"
        df.columns.name = "model_b"
        return df.T
    return predict_win_rate,


@app.cell
def __(bootstrap_elo_lu, predict_win_rate, px):
    win_rate = predict_win_rate(dict(bootstrap_elo_lu.quantile(0.5)))
    ordered_models = win_rate.mean(axis=1).sort_values(ascending=False).index
    ordered_models = ordered_models[:30]
    fig = px.imshow(win_rate.loc[ordered_models, ordered_models],
                    color_continuous_scale='RdBu', text_auto=".2f",
                    title="Predicted Win Rate Using Elo Ratings for Model A in an A vs. B Battle")
    fig.update_layout(xaxis_title="Model B",
                      yaxis_title="Model A",
                      xaxis_side="top", height=900, width=900,
                      title_y=0.07, title_x=0.5)
    fig.update_traces(hovertemplate=
                      "Model A: %{y}<br>Model B: %{x}<br>Win Rate: %{z}<extra></extra>")
    fig
    return fig, ordered_models, win_rate


@app.cell
def __():
    from collections import defaultdict
    import json, math, gdown
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import sklearn
    from tqdm import tqdm
    import requests
    pd.options.display.float_format = '{:.2f}'.format
    return (
        defaultdict,
        gdown,
        json,
        math,
        np,
        pd,
        px,
        requests,
        sklearn,
        tqdm,
    )


@app.cell
def __(pd, requests):
    url = "https://storage.googleapis.com/arena_external_data/public/clean_battle_20240419.json"
    response = requests.get(url)

    with open('local_file_name.json', 'wb') as file:
        file.write(response.content)

    # load the JSON data from the local file
    with open('local_file_name.json', 'r') as file:
        battles = pd.read_json(file).sort_values(ascending=True, by=["tstamp"])
    return battles, file, response, url


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()