# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "numpy",
#     "pandas",
#     "seaborn",
#     "scikit-learn",
# ]
# ///

import marimo

__generated_with = "0.8.18-dev11"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.image(
        src="https://i.ibb.co/SVcC6bb/final.png",
        alt="Community Tutorials Banner",
        width=800,
        rounded=True,
    ).center()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        *Author of this notebook - [Srihari Thyagarajan](https://github.com/Haleshot)*
        """
    ).right()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""# Exploratory Data Analysis for the [Goodreads dataset](https://github.com/malcolmosh/goodbooks-10k-extended).""")
    return


@app.cell(hide_code=True)
def __(mo):
    download_txt = mo.download(
        data="https://raw.githubusercontent.com/malcolmosh/goodbooks-10k/master/books_enriched.csv",
        filename="goodbooks-10k-extended",
        mimetype="text/plain",
        label="Download the Dataset",
    ).center()
    download_txt
    return (download_txt,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        df1 = pd.read_csv("ratings.csv")
        df2 = pd.read_csv("books_enriched.csv")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### The datasets used in this notebook can be found [here](https://github.com/Haleshot/marimo-tutorials/tree/main/marimo-tutorials/Data-Science/Exploratory-Data-Analysis/assets).""")
    return


@app.cell
def __():
    ## This code seems to make the notebook very laggy owing to it's size and compute ability of Pyodide (2GB)

    # df1 = pd.read_csv("/datasets/catalog/ratings.csv")
    # df2 = pd.read_csv("/datasets/catalog/books_enriched.csv")
    return


@app.cell
def __():
    # mo.ui.radio.from_series(df1['user_id'])
    return


@app.cell
def __():
    # mo.plain(df1)
    return


@app.cell
def __():
    # mo.plain(df2)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Performing EDA operations on
        - `Ratings.csv` dataset (df1)
        - `Books_enriched.csv` dataset (df2)
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Initial read on the contents of the dataset
        ```python
        mo.accordion(
            {
                "Dataset 1": mo.lazy(df1.head(15)),
                "Dataset 2": mo.lazy(df2.head(15)),
            }
        )
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __():
    # df1.head()
    return


@app.cell(hide_code=True)
def __(df1, df2, mo):
    mo.accordion(
        {
            "Dataset 1": mo.lazy(df1.head(15)),
            "Dataset 2": mo.lazy(df2.head(15)),
        }
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### Describing the datasets:""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        mo.ui.tabs(
            {
                "df1": mo.lazy(mo.ui.table(df1.describe())),
                "df2": mo.lazy(mo.ui.table(df2.describe())),
            }
        )
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, df2, mo):
    mo.ui.tabs(
        {
            "df1": mo.lazy(mo.ui.table(df1.describe())),
            "df2": mo.lazy(mo.ui.table(df2.describe())),
        }
    )
    return


@app.cell(hide_code=True)
def __():
    # # df1.describe()
    # mo.ui.table(df1.describe())
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### Using mo.ui.data_explorer to get a visual editor to explore the data via plotting and intelligent recommendations""")
    return


@app.cell(hide_code=True)
def __(df1, df2, mo):
    mo.ui.tabs(
        {
            "df1": mo.lazy(mo.ui.data_explorer(df1)),
            "df2": mo.lazy(mo.ui.data_explorer(df2)),
        }
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### Collecting information using the `info()` method on the datasets""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        df1.info()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, mo):
    with mo.redirect_stdout():
        df1.info()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        df2.info()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df2, mo):
    with mo.redirect_stdout():
        df2.info()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        print("Dataset 1 (ratings.csv) contains {} rows and {} columns".format(df1.shape[0], df1.shape[1]))
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, mo):
    with mo.redirect_stdout():
        print(
            "Dataset contains {} rows and {} columns".format(
                df1.shape[0], df1.shape[1]
            )
        )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        print("Dataset 2 (books_enriched) contains {} rows and {} columns".format(df2.shape[0], df2.shape[1]))
        ```
        """
    )
    return


@app.cell
def __(df2, mo):
    with mo.redirect_stdout():
        print(
            "Dataset 2 (books_enriched) contains {} rows and {} columns".format(
                df2.shape[0], df2.shape[1]
            )
        )
    return


@app.cell
def __(mo):
    callout_kind = mo.ui.dropdown(
        label="Color",
        options=["neutral", "danger", "warn", "success", "info"],
        value="neutral",
    )
    return (callout_kind,)


@app.cell(hide_code=True)
def __(mo):
    init_eda = mo.md(
        "## Initial EDA impressions \n ### 1.	For user ratings, how many total ratings are there - 5976479 \n ### 2.	How many total users are there - 53424 \n ### 3. How many total books are there  - 10000 \n ### 4. What is the maximum and minimum rating given by the user  - Max - 5, Min - 1 \n ### 5.  How many total columns are there in dataset books_enriched.csv - 30 \n ### 6. Anything noticeable in books dataset? If Yes,what? What steps will you suggest to handle that \n ### 7.	Print the statistical summary of books dataset and write the inference from the statistics observed for numeric as well as categorical columns. - From the above, while using the info() and describe() commands, I noticed the following: \n - There are two columns for authors (authors and authors_2). \n - There exist certain values in the publication year (-1750)  \n - No pa ges available for the book to actually exist (and yet it shows as published).  \n - Certain columns and attributes are not relevant and can be dropped during the PCA, EDA and feature engineering process to utilize data for various use case scenarios. \n - For ratings_count value, we notice that the maximum value is 4780653 ratings while the minimum value is 2716 ratings."
    )
    return (init_eda,)


@app.cell(hide_code=True)
def __(init_eda, mo):
    callout = mo.callout(init_eda, kind="info")
    return (callout,)


@app.cell(hide_code=True)
def __(callout):
    callout
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        <!-- ## Initial EDA impressions

        ### 1.	For user ratings, how many total ratings are there
        - 5976479
        ### 2.	How many total users are there
        - 53424
        ### 3.	How many total books are there 
        - 10000
        ### 4.	What is the maximum and minimum rating given by the user 
        - Max - 5, Min - 1
        ### 5.  How many total columns are there in dataset books_enriched.csv
        - 30 -->
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        <!-- ### 6.	Anything noticeable in books dataset? If Yes,what? What steps will you suggest to handle that
        ### 7.	Print the statistical summary of books dataset and write the inference from the statistics observed for numeric as well as categorical columns.
        - From the above, while using the info() and describe() commands, I noticed the following:
          1. There are two columns for authors (authors and authors_2).
          2. There exist certain values in the publication year (-1750)
          3. No pages available for the book to actually exist (and yet it shows as published).
          4. Certain columns and attributes are not relevant and can be dropped during the PCA, EDA and feature engineering process to utilize data for various use case scenarios.
          5. For ratings_count value, we notice that the maximum value is 4780653 ratings while the minimum value is 2716 ratings. -->
        """
    )
    return


@app.cell(hide_code=True)
def __(df2, mo):
    with mo.redirect_stdout():
        # Statistical summary for numeric columns
        numeric_summary = df2.describe()

        # Statistical summary for categorical columns
        categorical_summary = df2.describe(include=["object"])

        print("Statistical Summary for Numeric Columns:")
        print(numeric_summary)

        print("\nStatistical Summary for Categorical Columns:")
        print(categorical_summary)

        # # Inferences
        # numeric_inferences = """
        # Numeric Columns Summary:
        # 1. average_rating: Mean rating is around 4.0 indicating a generally positive user rating for books.
        # 2. books_count: This varies widely, with some books having multiple editions (max is 4917).
        # 3. original_publication_year: The mean year is around 1982, indicating the dataset has a mix of both old and recent books.
        # 4. pages: Mean pages per book is around 336, but this varies greatly with some very short and very long books.
        # """

        # categorical_inferences = """
        # Categorical Columns Summary:
        # 1. authors: Multiple authors are common; the dataset has unique author names for many books.
        # 2. genres: Books are classified into multiple genres, indicating diverse book content.
        # 3. language_code: 'eng' is the most common language code, suggesting the majority of books are in English.
        # 4. title: Each book has a unique title, though some titles may be shared by different works.
        # """

        # print(numeric_inferences)
        # print(categorical_inferences)
    return categorical_summary, numeric_summary


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### Statistical Summary for Numeric and Categorical Columns""")
    return


@app.cell(hide_code=True)
def __(df2, mo):
    mo.ui.tabs(
        {
            "df1": mo.lazy(mo.ui.table(df2.describe())),
            "df2": mo.lazy(mo.ui.table(df2.describe(include=["object"]))),
        }
    )
    return


@app.cell(hide_code=True)
def __(mo):
    numerical_infereces = mo.md(
        " ## Inferences  \n\n ## Numeric Columns Summary:   \n ### 1. average_rating: Mean rating is around 4.0 indicating a generally positive user rating for books. \n ### 2. books_count: This varies widely, with some books having multiple editions (max is 4917).  \n ### 3. original_publication_year: The mean year is around 1982, indicating the dataset has a mix of both old and recent books. \n ### 4. pages: Mean pages per book is around 336, but this varies greatly with some very short and very long books. \n ## Categorical Columns Summary:  \n ### 1. authors: Multiple authors are common; the dataset has unique author names for many books. \n ### 2. genres: Books are classified into multiple genres, indicating diverse book content. \n ### 3. language_code: 'eng' is the most common language code, suggesting the majority of books are in English. \n ### 4. title: Each book has a unique title, though some titles may be shared by different works. "
    )
    return (numerical_infereces,)


@app.cell(hide_code=True)
def __(mo, numerical_infereces):
    _callout = mo.callout(numerical_infereces, kind="info")
    _callout
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""Making changes infered from above before doing univariate/bivariate analysis""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## Preprocessing:""")
    return


@app.cell(hide_code=True)
def __(MinMaxScaler, df2, mo, pd):
    with mo.redirect_stdout():

        def print_diagnostic(step, df):
            print(f"After {step}:")
            print(f"Shape: {df.shape}")
            print(f"Columns: {df.columns.tolist()}")
            print(f"Non-null counts:\n{df.notnull().sum()}")
            print("-" * 50)

        cleaning_df = df2.copy()
        print_diagnostic("Initial copy", cleaning_df)

        # 1. Handle missing values
        numeric_cols = ["pages", "original_publication_year"]
        for col in numeric_cols:
            cleaning_df[col].fillna(cleaning_df[col].median(), inplace=True)

        categorical_cols = [
            "isbn",
            "isbn13",
            "original_title",
            "description",
            "publishDate",
        ]
        categorical_cols_desc = [
            "Unknown",
            "Unknown",
            "Unknown Title",
            "No description available",
            "Unknown Date",
        ]
        for col, fill_value in zip(categorical_cols, categorical_cols_desc):
            cleaning_df[col].fillna(fill_value, inplace=True)

        print_diagnostic("Handling missing values", cleaning_df)

        # 2. Remove duplicate columns
        if "authors" in cleaning_df.columns and "authors_2" in cleaning_df.columns:
            if cleaning_df["authors"].equals(cleaning_df["authors_2"]):
                cleaning_df = cleaning_df.drop("authors_2", axis=1)
            else:
                print(
                    "Warning: 'authors' and 'authors_2' are not identical. Please investigate."
                )

        print_diagnostic("Removing duplicate columns", cleaning_df)

        # 3. Remove unnecessary columns
        cleaning_df = cleaning_df.drop(
            ["Unnamed: 0", "index"], axis=1, errors="ignore"
        )
        print_diagnostic("Removing unnecessary columns", cleaning_df)

        # 4. Convert data types
        if cleaning_df["original_publication_year"].notna().any():
            median_year = cleaning_df["original_publication_year"].median()
            cleaning_df["original_publication_year"] = (
                cleaning_df["original_publication_year"]
                .fillna(median_year)
                .round()
            )
            cleaning_df["original_publication_year"] = cleaning_df[
                "original_publication_year"
            ].astype("Int64")
        else:
            print(
                "Warning: 'original_publication_year' column is entirely empty. Keeping as is."
            )

        cleaning_df["isbn13"] = (
            cleaning_df["isbn13"].fillna("0").astype(str).str.replace(".0", "")
        )

        print_diagnostic("Converting data types", cleaning_df)

        # 5. Handle potential data errors
        print("Before handling data errors:")
        print(cleaning_df["pages"].describe())
        print(f"Number of books with 0 pages: {(cleaning_df['pages'] == 0).sum()}")
        print(
            f"Number of books with negative pages: {(cleaning_df['pages'] < 0).sum()}"
        )

        # Instead of removing, let's set a minimum page count
        min_pages = 1
        cleaning_df.loc[cleaning_df["pages"] < min_pages, "pages"] = min_pages

        print("\nAfter handling data errors:")
        print(cleaning_df["pages"].describe())

        print_diagnostic("Handling data errors", cleaning_df)

        # 6. Preprocess genres
        if "genres" in cleaning_df.columns:
            cleaning_df["genres"] = cleaning_df["genres"].apply(
                lambda x: eval(x) if isinstance(x, str) else x
            )
        print_diagnostic("Preprocessing genres", cleaning_df)

        # 7. Create dummy variables for language_code
        if "language_code" in cleaning_df.columns:
            cleaning_df = pd.get_dummies(
                cleaning_df, columns=["language_code"], prefix="lang"
            )
        print_diagnostic("Creating dummy variables", cleaning_df)

        # 8. Normalize numerical columns
        numerical_columns = [
            "average_rating",
            "books_count",
            "pages",
            "ratings_count",
            "work_ratings_count",
            "work_text_reviews_count",
        ]
        if not cleaning_df.empty and all(
            col in cleaning_df.columns for col in numerical_columns
        ):
            if cleaning_df[numerical_columns].notna().any().all():
                scaler = MinMaxScaler()
                cleaning_df[numerical_columns] = scaler.fit_transform(
                    cleaning_df[numerical_columns]
                )
            else:
                print(
                    "Warning: Some numerical columns contain all null values. Skipping normalization."
                )
        else:
            print(
                "Warning: DataFrame is empty or missing expected columns. Skipping normalization."
            )

        print_diagnostic("Normalizing numerical columns", cleaning_df)

        # Save the preprocessed dataset
        if not cleaning_df.empty:
            cleaning_df.to_csv("preprocessed_books.csv", index=False)
            print(
                "Preprocessing complete. Preprocessed data saved to 'preprocessed_books.csv'."
            )
        else:
            print("Error: The cleaned DataFrame is empty. No file was saved.")
    return (
        categorical_cols,
        categorical_cols_desc,
        cleaning_df,
        col,
        fill_value,
        median_year,
        min_pages,
        numeric_cols,
        numerical_columns,
        print_diagnostic,
        scaler,
    )


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 8. Perform univariate analysis""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        print("\nNumber of Ratings per User:")
        user_ratings_count = df1['user_id'].value_counts()
        print(user_ratings_count)
        ```
        """
    )
    return


@app.cell
def __(df1, mo):
    with mo.redirect_stdout():
        print("\nNumber of Ratings per User:")
        user_ratings_count = df1["user_id"].value_counts()
        print(user_ratings_count)
    return (user_ratings_count,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        sns.displot(user_ratings_count)
        plt.xlabel("Number of Ratings per User")
        plt.ylabel("Number of Users")
        plt.title("Distribution of Ratings per User in Goodreads Dataset")
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(plt, sns, user_ratings_count):
    sns.displot(user_ratings_count)
    plt.xlabel("Number of Ratings per User")
    plt.ylabel("Number of Users")
    plt.title("Distribution of Ratings per User in Goodreads Dataset")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        print("\nPublication Year Distribution:")
        pub_year_counts = df2['original_publication_year'].value_counts().sort_index()
        print(pub_year_counts)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df2, mo):
    with mo.redirect_stdout():
        print("\nPublication Year Distribution:")
        pub_year_counts = (
            df2["original_publication_year"].value_counts().sort_index()
        )
        print(pub_year_counts)
    return (pub_year_counts,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        sns.displot(df2['original_publication_year'])
        plt.xlabel("Publication Year")
        plt.ylabel("Number of Books")
        plt.title("Distribution of Publication Year in Goodreads Dataset")
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df2, plt, sns):
    sns.displot(df2["original_publication_year"])
    plt.xlabel("Publication Year")
    plt.ylabel("Number of Books")
    plt.title("Distribution of Publication Year in Goodreads Dataset")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(df1, mo):
    with mo.redirect_stdout():

        # Univariate Analysis

        # 1. Distribution of Ratings
        print("Distribution of Ratings:")
        rating_counts = df1["rating"].value_counts().sort_index()
        print(rating_counts)

        # Matplotlib histogram (optional)
        # plt.hist(df1['rating'])
        # plt.xlabel("Rating")
        # plt.ylabel("Number of Ratings")
        # plt.title("Distribution of Ratings in Goodreads Dataset")
        # plt.gca()
    return (rating_counts,)


@app.cell(hide_code=True)
def __(df1, plt, sns):
    # Seaborn histogram
    sns.displot(df1["rating"])
    plt.xlabel("Rating")
    plt.ylabel("Number of Ratings")
    plt.title("Distribution of Ratings in Goodreads Dataset")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo, user_ratings_count):
    with mo.redirect_stdout():
        # 2. Number of Ratings per User
        print("\nNumber of Ratings per User:")
        # user_ratings_count = df1['user_id'].value_counts()
        print(user_ratings_count)
    return


@app.cell(hide_code=True)
def __(plt, sns, user_ratings_count):
    # Seaborn distribution of ratings per user
    sns.displot(user_ratings_count)
    plt.xlabel("Number of Ratings per User")
    plt.ylabel("Number of Users")
    plt.title("Distribution of Ratings per User in Goodreads Dataset")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo, pub_year_counts):
    with mo.redirect_stdout():
        # 3. Publication Year Distribution (Assuming 'original_publication_year' exists)
        print("\nPublication Year Distribution:")
        # pub_year_counts = df2['original_publication_year'].value_counts().sort_index()
        print(pub_year_counts)
    return


@app.cell(hide_code=True)
def __(df2, plt, sns):
    # Seaborn distribution of publication years
    sns.displot(df2["original_publication_year"])
    plt.xlabel("Publication Year")
    plt.ylabel("Number of Books")
    plt.title("Distribution of Publication Year in Goodreads Dataset")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 9. Perform bivariate analysis""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # Bivariate Analysis

        # 1. Rating vs. Publication Year
        # Merging dataframes assuming 'book_id' is the common column

        merged_data = df2.merge(df1[['rating', 'book_id']], how='left', on='book_id')
        sns.jointplot(x='original_publication_year', y='rating', data=merged_data)
        plt.xlabel("Publication Year")
        plt.ylabel("Rating")
        plt.title("Rating vs. Publication Year in Goodreads Dataset")
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, df2, plt, sns):
    # Bivariate Analysis

    # 1. Rating vs. Publication Year
    # Merging dataframes assuming 'book_id' is the common column

    merged_data = df2.merge(df1[["rating", "book_id"]], how="left", on="book_id")
    sns.jointplot(x="original_publication_year", y="rating", data=merged_data)
    plt.xlabel("Publication Year")
    plt.ylabel("Rating")
    plt.title("Rating vs. Publication Year in Goodreads Dataset")
    plt.gca()
    return (merged_data,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 2. Rating vs. Number of Ratings per Book
        # Calculate average rating per book
        average_ratings = df1.groupby('book_id')['rating'].mean()
        _merged_data = df2.merge(average_ratings.reset_index(), how='left', on='book_id')
        _merged_data.rename(columns={'rating_x': 'rating'}, inplace=True)  # Avoid name conflicts

        sns.jointplot(x='average_rating', y='rating', data=_merged_data)
        plt.xlabel("Average Rating per Book")
        plt.ylabel("Individual User Rating")
        plt.title("Rating vs. Average Rating per Book in Goodreads Dataset")
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, df2, plt, sns):
    # 2. Rating vs. Number of Ratings per Book
    # Calculate average rating per book
    average_ratings = df1.groupby("book_id")["rating"].mean()
    _merged_data = df2.merge(
        average_ratings.reset_index(), how="left", on="book_id"
    )
    _merged_data.rename(
        columns={"rating_x": "rating"}, inplace=True
    )  # Avoid name conflicts

    sns.jointplot(x="average_rating", y="rating", data=_merged_data)
    plt.xlabel("Average Rating per Book")
    plt.ylabel("Individual User Rating")
    plt.title("Rating vs. Average Rating per Book in Goodreads Dataset")
    plt.gca()
    return (average_ratings,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Check for Missing Value and Duplicated Rows. If required correct it.
        Done in the preprocessing of data.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 11.	How is the rating for all books distributed?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 11. How is the rating for all books distributed?
        plt.figure(figsize=(10, 6))
        sns.histplot(df1['rating'], bins=10, kde=True)
        plt.title('Distribution of Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, plt, sns):
    # 11. How is the rating for all books distributed?
    plt.figure(figsize=(10, 6))
    sns.histplot(df1["rating"], bins=10, kde=True)
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 12.	How is the average rating per user distributed?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 12. How is the average rating per user distributed?
        user_avg_ratings = df1.groupby('user_id')['rating'].mean()
        plt.figure(figsize=(10, 6))
        sns.histplot(user_avg_ratings, bins=20, kde=True)
        plt.title('Distribution of Average Ratings per User')
        plt.xlabel('Average Rating')
        plt.ylabel('Count')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, plt, sns):
    # 12. How is the average rating per user distributed?
    user_avg_ratings = df1.groupby("user_id")["rating"].mean()
    plt.figure(figsize=(10, 6))
    sns.histplot(user_avg_ratings, bins=20, kde=True)
    plt.title("Distribution of Average Ratings per User")
    plt.xlabel("Average Rating")
    plt.ylabel("Count")
    plt.gca()
    return (user_avg_ratings,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 13. How many ratings does a book usually get?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 13. How many ratings does a book usually get?
        book_rating_counts = df1['book_id'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.histplot(book_rating_counts, bins=50, kde=True)
        plt.title('Distribution of Ratings Count per Book')
        plt.xlabel('Number of Ratings')
        plt.ylabel('Count')
        plt.xscale('log')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, plt, sns):
    # 13. How many ratings does a book usually get?
    book_rating_counts = df1["book_id"].value_counts()
    plt.figure(figsize=(10, 6))
    sns.histplot(book_rating_counts, bins=50, kde=True)
    plt.title("Distribution of Ratings Count per Book")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Count")
    plt.xscale("log")
    plt.gca()
    return (book_rating_counts,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 14. How many ratings does a user usually give?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 14. How many ratings does a user usually give?
        user_rating_counts = df1['user_id'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.histplot(user_rating_counts, bins=50, kde=True)
        plt.title('Distribution of Ratings Count per User')
        plt.xlabel('Number of Ratings')
        plt.ylabel('Count')
        plt.xscale('log')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(df1, plt, sns):
    # 14. How many ratings does a user usually give?
    user_rating_counts = df1["user_id"].value_counts()
    plt.figure(figsize=(10, 6))
    sns.histplot(user_rating_counts, bins=50, kde=True)
    plt.title("Distribution of Ratings Count per User")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Count")
    plt.xscale("log")
    plt.gca()
    return (user_rating_counts,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 15. Does the ratings count affect average rating?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 15. Does the ratings count affect average rating?
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='ratings_count', y='average_rating', data=cleaning_df)
        plt.title('Ratings Count vs Average Rating')
        plt.xlabel('Ratings Count')
        plt.ylabel('Average Rating')
        plt.xscale('log')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, plt, sns):
    # 15. Does the ratings count affect average rating?
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="ratings_count", y="average_rating", data=cleaning_df)
    plt.title("Ratings Count vs Average Rating")
    plt.xlabel("Ratings Count")
    plt.ylabel("Average Rating")
    plt.xscale("log")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 16. Which book has the highest rating and which book has the most ratings?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 16. Which book has the highest rating and which book has the most ratings?
        highest_rated = cleaning_df.loc[cleaning_df['average_rating'].idxmax()]
        most_rated = cleaning_df.loc[cleaning_df['ratings_count'].idxmax()]
        print(f"Highest rated book: {highest_rated['title']} (Rating: {highest_rated['average_rating']})")
        print(f"Most rated book: {most_rated['title']} (Ratings: {most_rated['ratings_count']})")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df):
    # 16. Which book has the highest rating and which book has the most ratings?
    highest_rated = cleaning_df.loc[cleaning_df["average_rating"].idxmax()]
    most_rated = cleaning_df.loc[cleaning_df["ratings_count"].idxmax()]
    print(
        f"Highest rated book: {highest_rated['title']} (Rating: {highest_rated['average_rating']})"
    )
    print(
        f"Most rated book: {most_rated['title']} (Ratings: {most_rated['ratings_count']})"
    )
    return highest_rated, most_rated


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 17. How is the relationship between the number of ratings and the average rating?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 17. How is the relationship between the number of ratings and the average rating?
        # (This is similar to question 15, but we'll use a different visualization)
        plt.figure(figsize=(10, 6))
        sns.regplot(x='ratings_count', y='average_rating', data=cleaning_df, scatter_kws={'alpha':0.5})
        plt.title('Relationship between Ratings Count and Average Rating')
        plt.xlabel('Ratings Count (log scale)')
        plt.ylabel('Average Rating')
        plt.xscale('log')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, plt, sns):
    # 17. How is the relationship between the number of ratings and the average rating?
    # (This is similar to question 15, but we'll use a different visualization)
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x="ratings_count",
        y="average_rating",
        data=cleaning_df,
        scatter_kws={"alpha": 0.5},
    )
    plt.title("Relationship between Ratings Count and Average Rating")
    plt.xlabel("Ratings Count (log scale)")
    plt.ylabel("Average Rating")
    plt.xscale("log")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 18. Who is the author with most books?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 18. Who is the author with most books?
        author_book_counts = cleaning_df['authors'].value_counts()
        print(f"Author with most books: {author_book_counts.index[0]} ({author_book_counts.iloc[0]} books)")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df):
    # 18. Who is the author with most books?
    author_book_counts = cleaning_df["authors"].value_counts()
    print(
        f"Author with most books: {author_book_counts.index[0]} ({author_book_counts.iloc[0]} books)"
    )
    return (author_book_counts,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 19. Who is the most popular author?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 19. Who is the most popular author?
        cleaning_df['total_ratings'] = cleaning_df['ratings_1'] + cleaning_df['ratings_2'] + cleaning_df['ratings_3'] + cleaning_df['ratings_4'] + cleaning_df['ratings_5']
        author_popularity = cleaning_df.groupby('authors')['total_ratings'].sum().sort_values(ascending=False)
        print(f"Most popular author: {author_popularity.index[0]} ({author_popularity.iloc[0]} total ratings)")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, mo):
    # 19. Who is the most popular author?
    cleaning_df["total_ratings"] = (
        cleaning_df["ratings_1"]
        + cleaning_df["ratings_2"]
        + cleaning_df["ratings_3"]
        + cleaning_df["ratings_4"]
        + cleaning_df["ratings_5"]
    )
    author_popularity = (
        cleaning_df.groupby("authors")["total_ratings"]
        .sum()
        .sort_values(ascending=False)
    )
    with mo.redirect_stdout():
        print(
            f"Most popular author: {author_popularity.index[0]} ({author_popularity.iloc[0]} total ratings)"
        )
    return (author_popularity,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 20. Who is the author that has good ratings book?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 20. Who is the author that has good ratings book?
        author_avg_ratings = cleaning_df.groupby('authors')['average_rating'].mean().sort_values(ascending=False)
        print(f"Author with highest average rating: {author_avg_ratings.index[0]} (Average rating: {author_avg_ratings.iloc[0]:.2f})")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, mo):
    # 20. Who is the author that has good ratings book?
    author_avg_ratings = (
        cleaning_df.groupby("authors")["average_rating"]
        .mean()
        .sort_values(ascending=False)
    )
    with mo.redirect_stdout():
        print(
            f"Author with highest average rating: {author_avg_ratings.index[0]} (Average rating: {author_avg_ratings.iloc[0]:.2f})"
        )
    return (author_avg_ratings,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 21. How is the relationship between the number of pages and the year the book was published?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 21. How is the relationship between the number of pages and the year the book was published?
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='original_publication_year', y='pages', data=cleaning_df)
        plt.title('Relationship between Publication Year and Number of Pages')
        plt.xlabel('Publication Year')
        plt.ylabel('Number of Pages')
        plt.gca()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, plt, sns):
    # 21. How is the relationship between the number of pages and the year the book was published?
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="original_publication_year", y="pages", data=cleaning_df)
    plt.title("Relationship between Publication Year and Number of Pages")
    plt.xlabel("Publication Year")
    plt.ylabel("Number of Pages")
    plt.gca()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""### 22. What genre dominates the dataset?""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ```python
        # 22. What genre dominates the dataset?
        # Assuming 'genres' is a list of genres for each book
        all_genres = [genre for genres in cleaning_df['genres'] for genre in genres]
        genre_counts = pd.Series(all_genres).value_counts()
        plt.figure(figsize=(12, 6))
        genre_counts.head(20).plot(kind='bar')
        plt.title('Top 20 Genres in the Dataset')
        plt.xlabel('Genre')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.gca()

        print(f"The dominant genre is: {genre_counts.index[0]} with {genre_counts.iloc[0]} occurrences")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(cleaning_df, mo, pd, plt):
    # 22. What genre dominates the dataset?
    # Assuming 'genres' is a list of genres for each book
    all_genres = [genre for genres in cleaning_df["genres"] for genre in genres]
    genre_counts = pd.Series(all_genres).value_counts()
    plt.figure(figsize=(12, 6))
    genre_counts.head(20).plot(kind="bar")
    plt.title("Top 20 Genres in the Dataset")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.gca()

    with mo.redirect_stdout():
        print(
            f"The dominant genre is: {genre_counts.index[0]} with {genre_counts.iloc[0]} occurrences"
        )
    return all_genres, genre_counts


@app.cell(hide_code=True)
def __(mo):
    summary = mo.md(
        r"""
        # Summary

        This project utilizes the Goodreads dataset to explore user ratings and book metadata for building a book recommendation system.

        ### Data Exploration

        We begin by examining the basic properties of the data:

        * **Number of Ratings:** A total of **5,976,479** ratings are present.
        * **Number of Users:** There are **53,424** users in the dataset.
        * **Number of Books:** The dataset contains information on **10,000** books.
        * **Rating Range:** Users assign ratings between **1 (lowest) and 5 (highest).**
        * **Book Metadata:** The `books_enriched.csv` file contains **30 columns** with details like title, authors, publication year, genres, and average rating.

        A closer look at the `books_enriched.csv` reveals missing values in some columns. These missing values were likely addressed through appropriate cleaning techniques (e.g., imputation, removal).

        ### Univariate Analysis

        Getting into the nitty-gritty's data by analyzing individual features:

        * **Rating Distribution:** The distribution of average book ratings is visualized to understand user preferences.
        * **Average Rating per User:** We explore the distribution of average ratings assigned by each user.
        * **Number of Ratings per Book:** The distribution of ratings received by different books is analyzed.
        * **Number of Ratings per User:** The distribution of ratings provided by each user is examined.

        These visualizations provide insights into user rating behavior and book popularity.

        ### Bivariate Analysis (Further Exploration Recommended)

        While not covered in this specific analysis, exploring relationships between features can be valuable:

        * **Rating vs. Publication Year:** Investigate if there's a correlation between rating and when a book was published.
        * **Number of Ratings vs. Average Rating:** Analyze if books with more ratings tend to have higher or lower average ratings.
        * **Genre vs. Average Rating:** Explore if specific genres consistently have higher or lower average ratings.

        Utilizing libraries like Seaborn, Plotly, or Altair, we can create visualizations to reveal these relationships.

        ### Conclusion

        This exploratory data analysis provided valuable insights into the Goodreads dataset. We identified user rating patterns, book characteristics, and potential relationships between features. This knowledge can be leveraged to build a recommendation system that considers user preferences, book popularity, and potential trends in ratings and genres.

        **Future Exploration:**

        The next steps could involve feature engineering, model selection, and training a recommendation system based on the findings of this analysis. By leveraging these insights, we can create a system that effectively recommends books to users based on their preferences and historical ratings.
        """
    )
    _callout = mo.callout(summary, kind="success")
    _callout
    return (summary,)


@app.cell(hide_code=True)
def __():
    # import libraries
    import marimo as mo
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler
    return MinMaxScaler, mo, np, pd, plt, sns


@app.cell(hide_code=True)
def __():
    # # Uncomment the following code to install libraries required.
    # import micropip
    # await micropip.install("numpy")
    # import numpy as np
    return


@app.cell(hide_code=True)
def __(mo):
    mo.sidebar(
        [
            mo.md("# marimo x community"),
            mo.nav_menu(
                {
                    "#/home": f"{mo.icon('lucide:home')} Home",
                    "#/about": f"{mo.icon('lucide:user')} About",
                    "https://github.com/Haleshot/marimo-tutorials/issues": f"{mo.icon('lucide:phone')} Contact",
                    "Links": {
                        "https://twitter.com/marimo_io": "Twitter",
                        "https://github.com/Haleshot/marimo-tutorials": "GitHub",
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
