from setup import build_dictionaries
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

def price_to_float(price_str):
    return float(price_str.replace('$', '').replace(',', '.').replace(' ', ''))



def get_avg_dists(dev_spy):
    tag_years,tag_prices,tag_scores,tag_reviewcount, dev_years ,dev_prices ,dev_scores ,dev_reviewcount ,datath1 , datath2 , datath4 ,datath5 , datath6 = build_dictionaries(dev_spy)

    # Calcular a média dos preços para cada tag
    tag_avg_prices = {}
    for tag, price_dict in tag_prices.items():
        total_price = 0
        total_count = 0
        for price, count in price_dict.items():
            total_price += price * count
            total_count += count
        avg_price = total_price / total_count if total_count > 0 else 0
        tag_avg_prices[tag] = avg_price

    tag_frequencies = {}
    for tag, years in tag_years.items():
        total = 0
        for count in years.values():
            total += count
        tag_frequencies[tag] = total

    top_tags = sorted(tag_frequencies, key=tag_frequencies.get, reverse=True)

    # Filtrar os dados de preços para incluir apenas os X gêneros mais frequentes
    filtered_tag_prices = {}
    for tag in tag_prices:
        if tag in top_tags:
            filtered_tag_prices[tag] = tag_prices[tag]

    # Calcular a média dos preços para cada um dos 25 gêneros mais frequentes
    tag_avg_prices = {}
    for tag, price_dict in filtered_tag_prices.items():
        total_price = 0
        total_count = 0
        for price, count in price_dict.items():
            total_price += price * count
            total_count += count
        avg_price = total_price / total_count if total_count > 0 else 0
        tag_avg_prices[tag] = avg_price

    # Converter os dados em um DataFrame para visualização
    price_data = [{'Tag': tag, 'Average Price': avg_price} for tag, avg_price in tag_avg_prices.items()]
    price_df = pd.DataFrame(price_data)

    # Verificar os dados
    price_df = price_df.sort_values(by=['Average Price'], ascending=True)

    # Criar um histograma interativo
    #fig = px.histogram(price_df, x='Tag', y='Average Price', title='Distribuição dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Average Price':'Preço Médio'})
    HISTOGRAM_dist_avg_price_genre = px.histogram(price_df, x='Average Price',y='Tag', title='Distribuição dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Average Price':'Preço Médio'})
    HISTOGRAM_dist_avg_price_genre.update_layout(width=1000, height=2000)
    

    # Calcular a soma total dos preços médios
    total_avg_price = sum(tag_avg_prices.values())
    # Normalizar os preços médios dividindo pelo total de todos os preços
    tag_normalized_prices = {tag: price / total_avg_price for tag, price in tag_avg_prices.items()}


    # Converter os dados em um DataFrame para visualização
    price_data = [{'Tag': tag, 'Normalized Price': tag_normalized_prices[tag]} for tag in tag_avg_prices]
    price_df = pd.DataFrame(price_data)


    BAR_dist_normal_avg_price_genre = px.bar(price_df, x='Tag', y='Normalized Price', title='Distribuição Normalizada dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Normalized Price':'Preço Normalizado'})
    #fig.update_layout(width=1000, height=2000)
    



    # Calcular a média dos scores para cada gênero
    tag_avg_scores = {}
    for tag, scores_dict in tag_scores.items():
        total_score = 0
        total_count = 0
        for year, score in scores_dict.items():
            total_score += score
            total_count += 1
        avg_score = total_score / total_count if total_count > 0 else 0
        tag_avg_scores[tag] = avg_score

    # Calcular a soma total dos scores médios
    total_avg_score = sum(tag_avg_scores.values())

    # Normalizar os scores médios dividindo pelo total de todos os scores
    tag_normalized_scores = {tag: score / total_avg_score for tag, score in tag_avg_scores.items()}

    # Converter os dados em um DataFrame para visualização
    score_data = [{'Tag': tag, 'Average Score': tag_avg_scores[tag], 'Normalized Score': tag_normalized_scores[tag]} for tag in tag_avg_scores]
    score_df = pd.DataFrame(score_data)


    BAR_dist_normal_score_genre = px.bar(score_df, x='Tag', y='Normalized Score', title='Distribuição Normalizada dos Scores Médios por Gênero (Dividido pela Soma Total)', labels={'Tag':'Gênero', 'Normalized Score':'Score Normalizado'})



    tag_frequencies = {}
    for tag, years in tag_years.items():
        total = 0
        for count in years.values():
            total += count
        tag_frequencies[tag] = total

    top_tags = sorted(tag_frequencies, key=tag_frequencies.get, reverse=True)[:25]

    # Filtrar os scores para incluir apenas os X gêneros mais frequentes
    filtered_tag_scores = {}
    for tag in tag_scores:
        if tag in top_tags:
            filtered_tag_scores[tag] = tag_scores[tag]

    # Calcular a média dos preços para cada um dos 25 gêneros mais frequentes
    tag_avg_scores = {}
    for tag, scores_dict in filtered_tag_scores.items():
        total_score = 0
        total_count = 0
        for year, score in scores_dict.items():
            total_score += score
            total_count += 1
        avg_score = total_score / total_count if total_count > 0 else 0
        tag_avg_scores[tag] = avg_score


    # Calcular a soma total dos scores médios
    total_avg_score = sum(tag_avg_scores.values())

    # Normalizar os scores médios dividindo pelo total de todos os scores
    tag_normalized_scores = {tag: score / total_avg_score for tag, score in tag_avg_scores.items()}

    # Converter os dados em um DataFrame para visualização
    score_data = [{'Tag': tag, 'Average Score': tag_avg_scores[tag], 'Normalized Score': tag_normalized_scores[tag]} for tag in tag_avg_scores]
    score_df = pd.DataFrame(score_data)



    # Criar um gráfico de barras interativo para os scores normalizados
    BAR_normal_score_genre_div = px.bar(score_df, x='Tag', y='Normalized Score', title='Distribuição Normalizada dos Scores Médios por Gênero (Dividido pela Soma Total)', labels={'Tag':'Gênero', 'Normalized Score':'Score Normalizado'})


    # Converter os dados em um DataFrame para visualização
    price_data = [{'Tag': tag, 'Average Price': avg_price} for tag, avg_price in tag_avg_prices.items()]
    price_df = pd.DataFrame(price_data)


    # Criar um histograma interativo
    HISTOGRAM_dist_avg_price_genre_2 = px.histogram(price_df.head(25), x='Average Price', y='Tag', title='Distribuição dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Average Price':'Preço Médio'})




    tags_series = datath1['Tags'].str.split(',').explode().str.strip()
    top_genres = tags_series.value_counts().head(25)

    genres = top_genres.index.tolist()
    counts = top_genres.values.tolist()

    # plt.figure(figsize=(10, 10))
    # plt.barh(genres, counts, color='skyblue')
    # plt.xlabel('Frequência')
    # plt.title('Top 25 Gêneros Mais Frequentes')
    # plt.gca().invert_yaxis()
    # plt.show()


    tags_count = tags_series.value_counts().nlargest(15).reset_index()
    tags_count.columns = ['Tag', 'Count']
    SCATTER_blobs_genres = px.scatter(tags_count, x='Count', y='Tag', size='Count', color='Tag',
                    hover_name='Tag', size_max=60, title='Top 15 Game Genres on Steam')
    

        

    tags_count = tags_series.value_counts().nlargest(10).reset_index()
    tags_count.columns = ['Tag', 'Count']

    top_tags = tags_count['Tag'].tolist()

    filtered_data = datath1[datath1['Tags'].apply(lambda x: any(tag in x for tag in top_tags) if pd.notnull(x) else False)]
    filtered_data['Release Year'] = pd.to_datetime(filtered_data['Release Date'], errors='coerce').dt.year
    filtered_data['Tags'] = filtered_data['Tags'].apply(lambda x: x.split(', ') if pd.notnull(x) else [])

    expanded_data = filtered_data.explode('Tags')
    expanded_data = expanded_data[expanded_data['Tags'].isin(top_tags)]

    games_per_year = expanded_data.groupby(['Release Year', 'Tags']).size().reset_index(name='Count')
    games_per_year = games_per_year[games_per_year['Release Year'] <= 2020]
    games_per_year = games_per_year[games_per_year['Release Year'] >= 2000]

    LINE_games_year = px.line(games_per_year, x='Release Year', y='Count', color='Tags', title='Quantidade de Jogos Lançados por Ano por Gênero', log_y= True)


    # Filtrar os dados para a tag 'Indie'
    filtered_data = datath1[datath1['Tags'].apply(lambda x: 'Indie' in x if pd.notnull(x) else False)]

    # Extrair o ano de lançamento
    filtered_data['Release Year'] = pd.to_datetime(filtered_data['Release Date'], errors='coerce').dt.year

    # Explodir a coluna 'Tags' para ter uma linha por tag
    filtered_data['Tags'] = filtered_data['Tags'].apply(lambda x: x.split(', ') if pd.notnull(x) else [])
    expanded_data = filtered_data.explode('Tags')

    # Filtrar para manter apenas a tag 'Indie'
    expanded_data = expanded_data[expanded_data['Tags'] == 'Indie']

    games_per_year = expanded_data.groupby(['Release Year', 'Tags']).size().reset_index(name='Count')
    games_per_year = games_per_year[(games_per_year['Release Year'] <= 2020) & (games_per_year['Release Year'] >= 2000)]


    LINE_indie_year = px.line(games_per_year, x='Release Year', y='Count', title='Quantidade de Jogos Indie Lançados por Ano')

    return (HISTOGRAM_dist_avg_price_genre, 
            BAR_dist_normal_avg_price_genre , 
            BAR_dist_normal_score_genre,
            BAR_normal_score_genre_div,
            HISTOGRAM_dist_avg_price_genre_2,
            # gráfico de top 15 generos em matplotlib deve ser refeito em plotly,
            SCATTER_blobs_genres,
            LINE_games_year,            
            LINE_indie_year
            )