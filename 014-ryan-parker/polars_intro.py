import marimo

__generated_with = "0.9.7"
app = marimo.App(
    app_title="Polars intro",
    layout_file="layouts/polars_intro.slides.json",
    css_file="../custom.css",
)


@app.cell
def __(mo):
    mo.md(
        r"""
        # Intro to [polars](https://pola.rs)

        A brief introduction to the incredible `polars` dataframe library.

        ![polars logo](https://raw.githubusercontent.com/pola-rs/polars-static/master/banner/polars_github_banner.svg)

        Created by: [Ryan Parker](https://github.com/rparkr), August 2024. Last updated in October 2024.

        This demo is a [marimo notebook](https://marimo.io/), so it is interactive and reactive -- try experimenting with the widgets later on!
        """
    )
    return


@app.cell
async def __(mo):
    from pathlib import Path

    import polars as pl
    import download_data

    callout_download = None
    # Download data
    if not Path("data").exists():
        callout_download = mo.callout(
            kind="info", value="Downloading NYC Taxi and weather data"
        )
        await download_data.download_taxi_data()
        download_data.download_weather_data()
        download_data.download_weather_codes()
    callout_download
    return Path, callout_download, download_data, pl


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Data analysis in Python
        As an interpreted language with an easy-to-read syntax, Python is fantastic for data analysis, where rapid iteration enables exploration and accelerates development.

        Since its first release in 2008, [pandas](https://pandas.pydata.org/docs/) has been the de-facto standard for data analysis in Python, but in recent years other libraries have been created which offer distinct advantages. Some of those include:

        - [cuDF](https://docs.rapids.ai/api/cudf/stable/): GPU-accelerated dataframe operations with pandas API support
        - [modin](https://modin.readthedocs.io/en/stable/): pandas API running on distributed compute using [Ray](https://www.ray.io/) or [Dask](https://www.dask.org/) as a backend
        - [ibis](https://ibis-project.org/): dataframe library supporting dozens of backends (including pandas, polars, DuckDB, and many SQL databases)
        - [DuckDB](https://duckdb.org/): in-process database engine for running SQL queries on local or remote data
        - [temporian](https://temporian.readthedocs.io/en/stable/): efficient data processing for timeseries data
        - [polars](https://pola.rs/): ultra-fast dataframe library written in Rust
        - and others...
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        # Polars advantages
        - Easy to use
        - Parallelized across all CPU cores
        - Zero dependencies
        - Built on the Apache Arrow in-memory data format: enables zero-copy interoperability with other libraries (e.g., DuckDB, Snowflake)
        - Handles datasets larger than RAM
        - Powerful query optimizer
        - Fully compatible with scikit-learn and a growing ecosystem of other libraries, thanks to the [Dataframe Interchange Protocol](https://data-apis.org/dataframe-protocol/latest/) and [narwhals](https://github.com/narwhals-dev/narwhals)

        - {mo.icon('fluent-mdl2:rust-language-logo')} written in [Rust](https://rust-lang.org), a compiled language that has experienced rapid adoption since its first stable release in 2015 thanks to its C/C++ performance, concurrency, and memory safety
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        # Key concepts

        Polars uses the Apache Arrow in-memory data format, which is column-oriented. The primary data structures for polars are Series and DataFrames, similar to pandas.

        Apache Arrow supports many useful data types (many more than those which are supported by NumPy), so you can perform fast, vectorized operations on all kinds of data (nested JSON `structs`, strings, datetimes, etc.)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Contexts
        In Polars, a _context_ refers to the data available to operate on.

        The primary contexts are:

        **Selection**:

        - `.select()`: choose a subset of columns and perform operations on them
        - `.with_columns()`: add to the columns already available

        **Filtering**:

        - `.filter()`: filter the data using boolean conditions on row values

        **Aggregation**:

        - `.group_by()`: perform aggregations on groups of values
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Expressions

        _Expressions_ are the operations performed in Polars, things like:

        - `.sum()`
        - `.len()`
        - `.mean().over()...`
        - `when().then().otherwise()`
        - `.str.replace()`
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Lazy vs. Eager mode
        - `scan_csv()` vs. `read_csv()`

        ### Recommendation: use Lazy mode
        - In Lazy mode, Polars will optimize the query plan
        """
    )
    return


@app.cell
def __(mo):
    mo.vstack(
        [
            mo.md(
                r"""
                # Plugin ecosystem
                You can create custom expressions to use in Polars, which will also be vectorized and run in parallel like standard Polars expressions. If there's an operation you'd like to run on your data, chances are someone has already implemented it and it's just a `pip install` away. Here are [some examples](https://docs.pola.rs/user-guide/expressions/plugins/#community-plugins)...
                """
            ),
            mo.accordion(
                {
                    "### [`polars_ds`](https://github.com/abstractqqq/polars_ds_extension)": (
                        r"""
                        Polars extension for data science tasks

                        - A combination of functions and operations from scikit-learn, SciPy, and edit distance
                        - Polars is the only dependency (unless you want to create plots; that adds Plotly as a dependency)
                        - Can create bar plots within dataframe outputs (HTML `__repr__` in a notebook) -- like sparklines, and similar to what is available in pandas' advanced dataframe styling options
                        """
                    ),
                    "### [`polars_distance`](https://github.com/ion-elgreco/polars-distance)": (
                        r"""
                        Distance calculations (e.g., word similarity) in polars. Also includes haversine distance (lat/lon), cosine similarity, etc.
                        """
                    ),
                    "### [`polars_reverse_geocode`](https://github.com/MarcoGorelli/polars-reverse-geocode)": (
                        r"""
                        Offline reverse geocoding: find a city based on provided lat/lon; using an offline lookup table
                        """
                    ),
                    "### Tutorial: [how to create a polars plugin](https://marcogorelli.github.io/polars-plugins-tutorial/)": (
                        r"""
                        You can create your own plugin! This tutorial teaches you enough Rust to write a polars plugin, which can published to PyPI and installed by other Polars users.
                        """
                    ),
                }
            ),
        ]
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        # Final thoughts

        ## Upgrade weekly
        ⭐ Polars development [advances rapidly](https://github.com/pola-rs/polars/releases), so I recommend upgrading often (weekly) to get the latest features

        ## Try it out
        The best way to learn is by doing. Try using Polars any time you create a new notebook or start a new project.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        # Resources
        - [Polars user guide](https://docs.pola.rs/user-guide/migration/pandas/): fantastic guide to learning Polars alongside helpful explanations
        - [Coming from `pandas`](https://docs.pola.rs/user-guide/migration/pandas/): are you familiar with `pandas` and want to learn the differences you'll notice when switching to polars? This guide translates common concepts to help you.
          - [This series of articles from 2022](https://kevinheavey.github.io/modern-polars/) demonstrates some operations in pandas and polars, side-by-side. _Polars development advances rapidly, so many of the concepts covered in that series are already different. Still it will help you get a general feel for the flow of using Polars compared to pandas._
        - [Polars Python API](https://docs.pola.rs/api/python/stable/reference/index.html): detailed info on every expression, method, and function in Polars. I recommend browsing this list to get a feel for what Polars can do.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.vstack(
        [
            mo.md(r"""
    # Demo
    In this section, I demonstrate basic Polars usage on the NYC Taxi Yellow Cab dataset. You can find more information about that dataset on the [NYC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
    """),
            mo.accordion(
                {
                    "## Data dictionary (from the [PDF file published by NYC Trip Record Data](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf))": r"""
    1. **VendorID**: A code indicating the TPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.
    2. **tpep_pickup_datetime**: The date and time when the meter was engaged
    3. **tpep_dropoff_datetime**: The date and time when the meter was disengaged
    4. **Passenger_count**: The number of passengers in the vehicle. This is a driver-entered value.
    5. **Trip_distance**: The elapsed trip distance in miles reported by the taximeter
    6. **PULocationID**: TLC Taxi Zone in which the taximeter was engaged
        - [See here](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) for a map of the TLC Taxi Zones
    7. **DOLocationID**: TLC Taxi Zone in which the taximeter was disengaged
    8. **RateCodeID**: The final rate code in effect at the end of the trip.
        - 1 = Standard rate
        - 2 = JFK
        - 3 = Newark
        - 4 = Nassau or Westchester
        - 5 = Negotiated fare
        - 6 = Group ride
    9. **Store_and_fwd_flag**: This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server
        - Y = store and forward trip
        - N = not a store and forward trip
    10. **Payment_type**: A numeric code signifying how the passenger paid for the trip
        - 1 = Credit card
        - 2 = Cash
        - 3 = No charge
        - 4 = Dispute
        - 5 = Unknown
        - 6 = Voided trip
    11. **Fare_amount**: The time-and-distance fare calculated by the meter
    12. **Extra**: Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.
    13. **MTA_tax**: $0.50 MTA tax that is automatically triggered based on the metered rate in use
    14. **Improvement_surcharge**: $0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.
    15. **Tip_amount**: Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.
    16. **Tolls_amount**: Total amount of all tolls paid in trip.
    17. **Total_amount**: The total amount charged to passengers. Does not include cash tips
    18. **Congestion_Surcharge**: Total amount collected in trip for NYS congestion surcharge.
    19. **Airport_fee**: $1.25 for pick up only at LaGuardia and John F. Kennedy Airports
    """
                }
            ),
        ]
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Lazy-load the data
        Polars can read Parquet files (local or hosted on a network), determine their schema (columns and data types), apply filter pushdowns, and download only the data that is needed for the operations being performed.

        ```python
        import polars as pl

        # Create a dataframe from a collection of parquet files
        df = pl.scan_parquet("data/yellow_tripdata_*.parquet)
        ```
        """
    )
    return


@app.cell
def __(mo, pl):
    _md = mo.md(
        """
        Let's check the schema:

        ```python
        # Polars will scan the data and return
        # the column names and datatypes
        df.collect_schema()

        # If the file is stored locally, you can
        # also read the schema without collecting fist
        pl.read_parquet_schema("path/to/a/local/file.parquet")
        ```
        """
    )

    # Create a LazyFrame that will use the data from all the files specified above
    df = pl.scan_parquet("data/yellow_tripdata_*.parquet")
    _output = mo.plain(df.collect_schema())
    mo.vstack([_md, _output])
    return (df,)


@app.cell
def __(df, mo, pl):
    _md = mo.md(
        """
        **Preview the first few rows:**

        ```python
        df.head(n=10).collect()
        ```
        """
    )

    with pl.Config(tbl_cols=20, tbl_width_chars=1000, thousands_separator=True):
        _output = mo.plain_text(df.head(n=10).collect())

    mo.vstack([_md, _output])
    return


@app.cell
def __(df, mo, pl):
    _md = mo.md(
        """
        **You can also preview the first few rows like this:**

        ```python
        df.collect().glimpse()
        ```
        """
    )

    with mo.capture_stdout() as buffer:
        with pl.Config(thousands_separator=True):
            df.collect().glimpse()
    _output = mo.plain_text(buffer.getvalue())
    print(buffer.getvalue())
    mo.vstack([_md, _output, "Full list:", buffer.getvalue().strip().split("\n")])
    return (buffer,)


@app.cell
def __(df, pl):
    with pl.Config(thousands_separator=True):
        df.collect().glimpse()
    return


@app.cell
def __(df, mo, pl):
    _month_list = (
        df.select(month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m"))
        .group_by("month")
        .agg(num_trips=pl.len())
        .filter(pl.col("num_trips") > 100)  # Remove erroneous timestamps
        .unique()
        .sort(by="month")
        .collect()
        .to_series()
        .to_list()
    )
    print(_month_list)
    month_selection = mo.ui.multiselect(value=_month_list, options=_month_list)
    return (month_selection,)


@app.cell
def __(df, mo, month_selection, pl):
    _md = mo.md(
        f"""
        ## Explore the data

        **Find the average cost per trip, by month**

        Month selection: {month_selection}

        Note that the operations below are performed in parallel across all available CPU cores, and that only the data needed will be downloaded.

        In this case, since I have filtered to {len(month_selection.value)} months, only the files with those months of data will be accessed. Also notice that only 5 columns are accessed, since those are the ones I have requested.
        """
    )

    query_plan = (
        df.with_columns(month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m"))
        .filter(pl.col("month").is_in(month_selection.value))
        .group_by(pl.col("month"))
        .agg(
            num_trips=pl.len(),  # count the number of trips
            cost_per_trip=pl.col("total_amount").mean(),
            avg_passengers_per_trip=pl.col("passenger_count").mean(),
            avg_distance=pl.col("trip_distance").mean(),
            num_airport_trips=(pl.col("Airport_fee") > 0).sum(),
        )
    )
    _output = mo.plain_text(
        query_plan.explain(format="plain")  # see also: format="tree"
    )
    _output_with_streaming = mo.plain_text(query_plan.explain(streaming=True))

    _accordion = mo.accordion(
        {
            "Here's a way we could answer this question in Polars": mo.md(
                rf""" 
                Let's see this in Polars:

                ```python
                query_plan = (
                    df.with_columns(month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m"))
                    .filter(pl.col("month").is_in({month_selection.value}))
                    .group_by(pl.col("month"))
                    .agg(
                        num_trips=pl.len(),  # count the number of trips
                        cost_per_trip=pl.col("total_amount").mean(),
                        avg_passengers_per_trip=pl.col("passenger_count").mean(),
                        avg_distance=pl.col("trip_distance").mean(),
                        num_airport_trips=(pl.col("Airport_fee") > 0).sum(),
                    )
                )
                ```
                """
            ),
            "Let's see how Polars will optimize this query": mo.md(
                r"""
                ```python
                # Show the optimized query plan:
                query_plan.explain()
                ```
                """
            ),
            "Query plan": _output,
            "You can also run this in streaming mode for memory-constrained environments": mo.md(
                r"""
                ```python
                query_plan.explain(streaming=True)
                ```
                """
            ),
            "Query plan with streaming": _output_with_streaming,
        }
    )


    mo.vstack([_md, _accordion])
    return (query_plan,)


@app.cell
def __(mo, month_selection, pl, query_plan):
    _md = mo.md(
        rf"""
        ### Perform the calculation ("collect")

        Month selection: {month_selection}

        ```python
        df_avg = query_plan.collect().sort(by=pl.col("month"))
        ```

        Some options to `.collect()`: `engine="cpu"`, `streaming=False`, `background=False`
        """
    )

    df_avg = query_plan.collect().sort(by=pl.col("month"))

    with pl.Config(tbl_cols=20, tbl_width_chars=1000, thousands_separator=True):
        _output = mo.plain_text(df_avg)

    mo.vstack([_md, _output])
    return (df_avg,)


@app.cell
def __(df, mo, month_selection, pl):
    _md = mo.md(
        f"""
        ## How does trip count vary by hour of the day?

        Months: {month_selection}
        """
    )

    _result = (
        df.with_columns(
            month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m"),
            hour=pl.col("tpep_pickup_datetime").dt.hour(),
        )
        .filter(pl.col("month").is_in(month_selection.value))
        .group_by(["month", "hour"])
        .agg(
            num_trips=pl.len(),  # count the number of trips
        )
        .filter(pl.col("num_trips") > 100)  # exclude erroneous timestamps
        .sort(by=["month", "hour"], descending=[False, False])
    )

    _plot = _result.collect().plot.line(x="hour", y="num_trips", color="month")

    _accordion = mo.accordion(
        {
            "Let's see this in Polars:": mo.md(
                rf""" 
                ```python
                result = (
                    df.with_columns(
                        month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m"),
                        hour=pl.col("tpep_pickup_datetime").dt.hour(),
                    )
                    .filter(pl.col("month").is_in({month_selection.value}))
                    .group_by(["month", "hour"])
                    .agg(
                        num_trips=pl.len(),  # count the number of trips
                    )
                    .filter(pl.col("num_trips") > 100)  # exclude erroneous timestamps
                    .sort(by=["month", "hour"], descending=[False, False])
                )

                # Plot with Altair
                plot = (
                    result
                    .collect()
                    .plot.line(
                        x="hour",
                        y="num_trips",
                        color="month"
                    )
                )
                ```
                """
            ),
        }
    )

    mo.vstack([_md, _accordion, _plot])
    return


@app.cell
def __():
    # Explore the weather codes:
    import json

    with open("data/weather_codes.json", mode="rt", encoding="utf8") as json_file:
        weather_codes_dict = json.load(json_file)

    with open("data/weather.json", mode="rt", encoding="utf8") as json_file:
        weather_data_dict = json.load(json_file)
    return json, json_file, weather_codes_dict, weather_data_dict


@app.cell
def __(df, pl):
    # import polars.selectors as cs  # for "column selectors"

    # Load the weather codes data and convert to a LazyFrame
    weather_codes = (
        pl.read_json("data/weather_codes.json")
        .unpivot()
        .select(pl.col("variable").alias("weather_code"), pl.col("value"))
        .unnest("value")
        # Expand the descriptions for night only,
        # which uses "clear" rather than "sunny"
        .unnest("night")
        .select(
            [
                # Must be the same data type (Int64) for joining
                pl.col("weather_code").cast(pl.Int64),
                pl.col("description").alias("weather_description"),
            ]
        )
    ).lazy()  # must be a LazyFrame to join with another LazyFrame

    # Get the names of the weather variables, so their lists can be "exploded"
    # down the rows of the LazyFrame
    data_fields = (
        pl.scan_ndjson("data/weather.json")
        .select("hourly_units")
        .collect()  # you have to .collect() to access a Series
        .to_series()  # the .struct accessor is available only for Series
        .struct.fields  # .fields holds the keys (column names, after unnesting)
    )

    # LazyFrame with weather data and weather descriptions
    df_weather = (
        pl.scan_ndjson("data/weather.json")
        .unnest("hourly")  # expand a dict into columns
        .explode(
            columns=data_fields,  # expand a list into rows
            # Alternatively, using column selectors:
            # columns=cs.by_name(data_fields)
        )
        .select(data_fields)
        .join(weather_codes, on="weather_code")
        .with_columns(
            # Replace the "time" column and update its
            # datatype so it can be joined to the trip data
            pl.col("time").cast(pl.Datetime(time_unit="ns")),
        )
        .sort(by="time")
    )

    # Combine with the Taxi data
    # for a join_asof, both DataFrames need to
    # be sorted by the join_asof key
    df_combined = df.sort("tpep_pickup_datetime").join_asof(
        df_weather,
        left_on="tpep_pickup_datetime",
        right_on="time",
        # Use the weather data closest to the time of pickup
        strategy="nearest",  # alternatives: "backward", "forward"
        tolerance="2h",  # weather data must be within 2 hours of trip time
    )
    return data_fields, df_combined, df_weather, weather_codes


@app.cell
def __(df_combined, df_weather, mo, weather_codes_dict, weather_data_dict):
    _md = mo.md(
        r"""
        ## How does weather impact trips?

        For this analysis, we'll take advantage of Polar's ability to load and join multiple data types and join them together using approximate timestamp matching -- all using "lazy," optimized computations.

        The time zone for both taxi trip data and weather is **America/New_York**.

        > [Weather data from Open-Meteo.com](https://open-meteo.com/), weather codes from [stellasphere](https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c).
        """
    )


    _accordion = mo.accordion(
        {
            "Here's the plain JSON weather data": weather_data_dict,
            "And here are the weather codes": weather_codes_dict,
            "Let's load the weather data in Polars": (
                """
                ```python
                # This is also a LazyFrame (you can tell from `scan_`)
                # LazyFrame with weather data and weather descriptions
                df_weather = (
                    pl.scan_ndjson("data/weather.json")
                    .unnest("hourly")  # expand a dict into columns
                    .explode(
                        columns=data_fields,  # expand a list into rows
                    )
                    .select(data_fields)
                    .join(weather_codes, on="weather_code")
                    .with_columns(
                        # Replace the "time" column and update its
                        # datatype so it can be joined to the trip data
                        pl.col("time").cast(pl.Datetime(time_unit="ns")),
                    )
                    .sort(by="time")
                )
                ```
                """
            ),
            "Here's what the data looks like": df_weather.head(100).collect(),
            "Combine with the Taxi trips data": (
                """
                ```python
                # for a join_asof, both DataFrames need to
                # be sorted by the join_asof key
                df_combined = df.sort("tpep_pickup_datetime").join_asof(
                    df_weather,
                    left_on="tpep_pickup_datetime",
                    right_on="time",
                    # Use the weather data closest to the time of pickup
                    strategy="nearest",  # alternatives: "backward", "forward"
                    tolerance="2h",  # weather data must be within 2 hours of trip time
                )
                ```
                """
            ),
            "Preview the combined dataset": df_combined.head(100).collect(),
            "Here's the Polars code for the weather codes and data fields": (
                """
                ```python
                # Load the weather codes data and convert to a LazyFrame
                weather_codes = (
                    pl.read_json("data/weather_codes.json")
                    .unpivot()
                    .select(pl.col("variable").alias("weather_code"), pl.col("value"))
                    .unnest("value")
                    # Expand the descriptions for night only,
                    # which uses "clear" rather than "sunny"
                    .unnest("night")
                    .select(
                        [
                            # Must be the same data type (Int64) for joining
                            pl.col("weather_code").cast(pl.Int64),
                            pl.col("description").alias("weather_description"),
                        ]
                    )
                ).lazy()  # must be a LazyFrame to join with another LazyFrame
                
                # Get the names of the weather variables, so their lists can be "exploded"
                # down the rows of the LazyFrame
                data_fields = (
                    pl.scan_ndjson("data/weather.json")
                    .select("hourly_units")
                    .collect()  # you have to .collect() to access a Series
                    .to_series()  # the .struct accessor is available only for Series
                    .struct.fields  # .fields holds the keys (column names, after unnesting)
                )
                ```
                """
            ),
        }
    )

    mo.vstack([_md, _accordion])
    return


@app.cell
def __(mo, weather_codes):
    weather_selection = mo.ui.multiselect.from_series(
        weather_codes.select("weather_description").collect().to_series(),
        label="",
        value=["Clear", "Rain"],
    )
    return (weather_selection,)


@app.cell
def __(df_combined, mo, pl, weather_selection):
    _md = mo.md(
        f"""
        ### How much does weather impact average cost?

        Weather to compare: {weather_selection}
        """
    )

    _result = (
        df_combined.with_columns(
            month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m")
        )
        .group_by(["month", "weather_description"])
        .agg(
            num_trips=pl.len(),
            cost_per_person=pl.col("total_amount").sum()
            / pl.col("passenger_count").sum(),
        )
        .filter(pl.col("num_trips") > 100)
        # Filter based on our selection
        # Joins are highly optimized and can be faster than .is_in()
        .join(
            pl.LazyFrame({"weather_description": weather_selection.value}),
            on="weather_description",
        )
        .sort(by=["month", "weather_description"])
    )

    _plot_bar = _result.collect().plot.bar(
        x="month",
        y="cost_per_person",
        color="weather_description",
        xOffset="weather_description",
    )

    _plot_line = _result.collect().plot.line(
        x="month",
        y="num_trips",
        color="weather_description",
    )
    # Show the plots side by side (use + to layer on top of one another)
    _plot = _plot_bar | _plot_line

    _accordion = mo.accordion(
        {
            "Polars operations": (
                """
                ```python
                result = (
                    df_combined.with_columns(
                        month=pl.col("tpep_pickup_datetime").dt.strftime("%Y-%m")
                    )
                    .group_by(["month", "weather_description"])
                    .agg(
                        num_trips=pl.len(),
                        cost_per_person=pl.col("total_amount").sum()
                        / pl.col("passenger_count").sum(),
                    )
                    .filter(pl.col("num_trips") > 100)
                    # Filter based on our selection
                    # Joins are highly optimized and can be faster than .is_in()
                    .join(
                        pl.LazyFrame({"weather_description": weather_selection.value}),
                        on="weather_description",
                    )
                    .sort(by=["month", "weather_description"])
                )
                ```
                """
            ),
            "Let's check the query plan (**`result.explain()`**)": mo.plain_text(
                _result.explain()
            ),
            "Now, we'll visualize this with an interactive plot": (
                """
                ```python
                plot_bar = result.collect().plot.bar(
                    x="month",
                    y="cost_per_person",
                    color="weather_description",
                    xOffset="weather_description",
                )
                
                plot_line = result.collect().plot.line(
                    x="month",
                    y="num_trips",
                    color="weather_description",
                )
                # Show the plots side by side (use + to layer on top of one another)
                plot = plot_bar | plot_line
                ```
                """
            ),
        }
    )

    mo.vstack([_md, _accordion, _plot])
    return


@app.cell
def __(mo):
    mo.md(
        """
        # Keep exploring!
        Polars has many additional powerful features. Try exploring with some of them through this dataset and what you find on Polars' [User Guide](https://docs.pola.rs/) and [API reference](https://docs.pola.rs/api/python/stable/reference/index.html).
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()