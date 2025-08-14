import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np


def log_converter(datath6_c):
    datath6_c["Reviews Total"] = np.log10(datath6_c["Reviews Total"].replace(0, np.nan))
    datath6_c["Revenue Estimated"] = np.log10(
        datath6_c["Revenue Estimated"].replace(0, np.nan)
    )
    datath6_c.dropna(subset=["Reviews Total"], inplace=True)
    return datath6_c


def build_histogram(datath1_c, datath6_c):
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=[
            "Launch Price",
            "Number of Reviews",
            "Revenue Estimated",
            "Release Date",
        ],
    )
    fig.add_trace(
        go.Histogram(
            x=datath1_c["Launch Price"],
            name="Launch Price",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Histogram(x=datath6_c["Reviews Total"], name="Number of Reviews"),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Histogram(x=datath6_c["Revenue Estimated"], name="Revenue"), row=2, col=1
    )
    fig.add_trace(
        go.Histogram(x=datath1_c["Release Date"], name="Release"), row=2, col=2
    )

    return fig


def build_scatter_matrix(datath1_c, outliers=False):
    spooky_men_id = 2204850
    cs_id = 730
    # pubg_id = 578080
    main_outliers_ids = [spooky_men_id, cs_id]
    dataNoOutliers = datath1_c[-datath1_c["App ID"].isin(main_outliers_ids)]

    target_dists = [
        "Reviews Total",
        "Reviews Score Fancy",
        "Launch Price",
        "Revenue Estimated",
    ]
    fig = px.scatter_matrix(
        datath1_c if outliers else dataNoOutliers,
        dimensions=target_dists,
        labels={
            "Reviews Total": "reviews",
            "Reviews Score Fancy": "score(%)",
            "Launch Price": "price",
            "Revenue Estimated": "revenue",
        },
        title="Correlation between attributes with outliers",
    )
    return fig


def build_heat_plot(dataCopy):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    days = [x for x in range(1, 32)]

    dataCopy["Release Date"] = pd.to_datetime(dataCopy["Release Date"], errors="coerce")
    dataCopy["Month"] = dataCopy["Release Date"].dt.month_name()
    dataCopy["Day"] = dataCopy["Release Date"].dt.day.astype(int)
    dayGroupedData = (
        dataCopy.groupby(["Month", "Day"])
        .size()
        .reset_index()
        .pivot(index="Month", columns="Day")
        .fillna(0)
    )
    dayGroupedData = dayGroupedData.reindex(index=months)
    dayGroupedData = dayGroupedData.astype(int)
    dayGroupedData = dayGroupedData.to_numpy()
    dateDataframe = pd.DataFrame(data=dayGroupedData, index=months, columns=days)
    fig = px.imshow(
        dateDataframe,
        x=dateDataframe.columns,
        y=dateDataframe.index,
        labels=dict(x="Day", y="Month", color="Number of games launched"),
    )
    fig.update_xaxes(side="bottom")
    return fig


def build_dev_fig(devdf):
    devdf = devdf.sort_values(by=["average price"], ascending=True)
    devprice = px.bar(
        devdf,
        x="Average Price",
        y="Developer Name",
        orientation="h",
        labels={"Developer Name": "name", "Average Price": "average price"},
    )
    devdf = devdf.sort_values(by=["average score"], ascending=True)
    devscore = px.bar(
        devdf,
        x="Average Score",
        y="Developer Name",
        orientation="h",
        labels={"Developer Name": "name", "Average Score": "average score"},
    )
    devdf = devdf.sort_values(by=["average review count"], ascending=True)
    devreview = px.bar(
        devdf,
        x="Average Review Count",
        y="Developer Name",
        orientation="h",
        labels={
            "Developer Name": "name",
            "Average Review Count": "average review count",
        },
    )
    return devprice, devscore, devreview
