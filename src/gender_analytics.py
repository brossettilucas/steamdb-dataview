import plotly.express as px
import pandas as pd


def price_to_float(price_str):
    return float(price_str.replace("$", "").replace(",", ".").replace(" ", ""))


def get_scatter_genre_blobs(datath1):
    tags_series = datath1["Tags"].str.split(",").explode().str.strip()
    tags_count = tags_series.value_counts().nlargest(15).reset_index()
    tags_count.columns = ["Tag", "Count"]
    SCATTER_blobs_genres = px.scatter(
        tags_count,
        x="Count",
        y="Tag",
        size="Count",
        color="Tag",
        hover_name="Tag",
        size_max=60,
        title="Top 15 Game Genres on Steam",
    )
    return SCATTER_blobs_genres


def get_line_year(datath1, isLog=False):
    tags_series = datath1["Tags"].str.split(",").explode().str.strip()
    tags_count = tags_series.value_counts().nlargest(10).reset_index()
    tags_count.columns = ["Tag", "Count"]

    top_tags = tags_count["Tag"].tolist()

    filtered_data = datath1[
        datath1["Tags"].apply(
            lambda x: any(tag in x for tag in top_tags) if pd.notnull(x) else False
        )
    ]
    filtered_data["Release Year"] = pd.to_datetime(
        filtered_data["Release Date"], errors="coerce"
    ).dt.year
    filtered_data["Tags"] = filtered_data["Tags"].apply(
        lambda x: x.split(", ") if pd.notnull(x) else []
    )

    expanded_data = filtered_data.explode("Tags")
    expanded_data = expanded_data[expanded_data["Tags"].isin(top_tags)]

    games_per_year = (
        expanded_data.groupby(["Release Year", "Tags"]).size().reset_index(name="Count")
    )
    games_per_year = games_per_year[games_per_year["Release Year"] <= 2020]
    games_per_year = games_per_year[games_per_year["Release Year"] >= 2000]

    LINE_games_year = px.line(
        games_per_year,
        x="Release Year",
        y="Count",
        color="Tags",
        title="Quantidade de Jogos Lançados por Ano por Gênero",
        log_y=isLog,
    )
    return LINE_games_year


def get_line_indie_year(datath1):
    filtered_data = datath1[
        datath1["Tags"].apply(lambda x: "Indie" in x if pd.notnull(x) else False)
    ]
    filtered_data["Release Year"] = pd.to_datetime(
        filtered_data["Release Date"], errors="coerce"
    ).dt.year
    filtered_data["Tags"] = filtered_data["Tags"].apply(
        lambda x: x.split(", ") if pd.notnull(x) else []
    )
    expanded_data = filtered_data.explode("Tags")
    expanded_data = expanded_data[expanded_data["Tags"] == "Indie"]
    games_per_year = (
        expanded_data.groupby(["Release Year", "Tags"]).size().reset_index(name="Count")
    )
    games_per_year = games_per_year[
        (games_per_year["Release Year"] <= 2020)
        & (games_per_year["Release Year"] >= 2000)
    ]

    LINE_indie_year = px.line(
        games_per_year,
        x="Release Year",
        y="Count",
        title="Quantidade de Jogos Indie Lançados por Ano",
    )
    return LINE_indie_year
