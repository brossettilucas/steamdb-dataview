import pandas as pd
import plotly.express as px
import pandas as pd

def make_treemap_top_games(datath1,topn=17):
    top_10_reviews = datath1.nlargest(topn, 'Reviews Total')
    top_10_reviews['Tags'] = top_10_reviews['Tags'].str.split(',').apply(lambda x: x[:3] if isinstance(x, list) else [])
    top_10_reviews_dict = top_10_reviews.set_index('Title')['Tags'].to_dict()
    treemap_data = []
    for title, tags in top_10_reviews_dict.items():
        for tag in tags:
            treemap_data.append({'Title': title, 'Tag': tag, 'Reviews Total': top_10_reviews.loc[top_10_reviews['Title'] == title, 'Reviews Total'].values[0]})
    treemap_df = pd.DataFrame(treemap_data)
    treemap_df = treemap_df.sort_values(by='Reviews Total', ascending=False)
    fig = px.treemap(treemap_df, path=['Title', 'Tag'], values='Reviews Total', title='Treemap of Most Reviewed Games and Their Tags')

    return fig


def make_treemap_top_devs(datath1,topn=15):
    developer_reviews = datath1.groupby('developer')['Reviews Total'].sum().reset_index()
    top_developer_reviews = developer_reviews.sort_values(by='Reviews Total', ascending=False).reset_index(drop=True)
    top_developers = top_developer_reviews.head(topn)['developer'].tolist()
    filtered_data = datath1[datath1['developer'].isin(top_developers)].copy()
    filtered_data['Tags'] = filtered_data['Tags'].str.split(',')
    filtered_data['Tags'] = filtered_data['Tags'].apply(lambda x: x[:3] if isinstance(x, list) else [])
    developer_tags_dict = {}
    for dev, group in filtered_data.groupby('developer'):
        all_tags = [tag for tags_list in group['Tags'] for tag in tags_list]
        unique_tags = list(pd.Series(all_tags).unique())[:3]
        developer_tags_dict[dev] = unique_tags

    treemap_data = []
    for developer, tags in developer_tags_dict.items():
        total_reviews = top_developer_reviews[top_developer_reviews['developer'] == developer]['Reviews Total'].values[0]
        for tag in tags:
            treemap_data.append({'Developer': developer, 'Tag': tag, 'Total Reviews': total_reviews})

    treemap_df = pd.DataFrame(treemap_data)
    treemap_df = treemap_df.sort_values(by='Total Reviews', ascending=False)

    fig = px.treemap(treemap_df, path=['Developer', 'Tag'], values='Total Reviews',
                    title='Treemap of Most Reviewed Developers and Their Tags',
                    labels={'Total Reviews': 'Total Reviews'})

    return fig
