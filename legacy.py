
# def get_avg_dists_legacy(dev_spy):
#     tag_years,tag_prices,tag_scores,tag_reviewcount, dev_years ,dev_prices ,dev_scores ,dev_reviewcount ,datath1 , datath2 , datath4 ,datath5 , datath6 = build_dictionaries(dev_spy)
#     # Calcular a média dos preços para cada tag
#     tag_avg_prices = {}
#     for tag, price_dict in tag_prices.items():
#         total_price = 0
#         total_count = 0
#         for price_str, count in price_dict.items():
#             price = price_to_float(price_str)
#             total_price += price * count
#             total_count += count
#         avg_price = total_price / total_count if total_count > 0 else 0
#         tag_avg_prices[tag] = avg_price
    

#     tag_frequencies = {}
#     for tag, years in tag_years.items():
#         total = 0
#         for count in years.values():
#             total += count
#         tag_frequencies[tag] = total

#     top_tags = sorted(tag_frequencies, key=tag_frequencies.get, reverse=True)

#     # Filtrar os dados de preços para incluir apenas os X gêneros mais frequentes
#     filtered_tag_prices = {}
#     for tag in tag_prices:
#         if tag in top_tags:
#             filtered_tag_prices[tag] = tag_prices[tag]

#     # Calcular a média dos preços para cada um dos 25 gêneros mais frequentes
#     tag_avg_prices = {}
#     for tag, price_dict in filtered_tag_prices.items():
#         total_price = 0
#         total_count = 0
#         for price_str, count in price_dict.items():
#             price = price_to_float(price_str)
#             total_price += price * count
#             total_count += count
#         avg_price = total_price / total_count if total_count > 0 else 0
#         tag_avg_prices[tag] = avg_price

#     # Converter os dados em um DataFrame para visualização
#     price_data = [{'Tag': tag, 'Average Price': avg_price} for tag, avg_price in tag_avg_prices.items()]
#     price_df = pd.DataFrame(price_data)

#     # Verificar os dados
#     print(price_df.head(3))
#     print(price_df.columns)
#     price_df = price_df.sort_values(by=['Average Price'], ascending=True)

#     # Criar um histograma interativo
#     #fig = px.histogram(price_df, x='Tag', y='Average Price', title='Distribuição dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Average Price':'Preço Médio'})
#     HISTOGRAM_avg_price = px.histogram(price_df, x='Average Price',y='Tag', title='Distribuição dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Average Price':'Preço Médio'})
#     HISTOGRAM_avg_price.update_layout(width=1000, height=2000)


#     tag_histogram = {}
#     for tag in tag_prices:
#         if len(tag_prices[tag]) > 50:
#             avg = 0
#             for price in tag_prices[tag]:
#                 avg += tag_prices[tag][price]*float(price[1:])
#                 tag_histogram[tag] = avg/len(tag_prices[tag])
#     sorted_tag_histogram = sorted(tag_histogram.items(), key=lambda item: item[1], reverse=True)

#     # Calcular a soma total dos preços médios
#     total_avg_price = sum(tag_avg_prices.values())
#     print(total_avg_price)
#     # Normalizar os preços médios dividindo pelo total de todos os preços
#     tag_normalized_prices = {tag: price / total_avg_price for tag, price in tag_avg_prices.items()}


#     # Converter os dados em um DataFrame para visualização
#     price_data = [{'Tag': tag, 'Normalized Price': tag_normalized_prices[tag]} for tag in tag_avg_prices]
#     price_df = pd.DataFrame(price_data)


#     print(price_df.head(22))
#     print(price_df.columns)

#     BAR_price_genre = px.bar(price_df, x='Tag', y='Normalized Price', title='Distribuição Normalizada dos Preços Médios de Lançamento por Gênero', labels={'Tag':'Gênero', 'Normalized Price':'Preço Normalizado'})
#     #fig.update_layout(width=1000, height=2000)


#     # Calcular a média dos scores para cada gênero
#     tag_avg_scores = {}
#     for tag, scores_dict in tag_scores.items():
#         total_score = 0
#         total_count = 0
#         for year, score in scores_dict.items():
#             total_score += score
#             total_count += 1
#         avg_score = total_score / total_count if total_count > 0 else 0
#         tag_avg_scores[tag] = avg_score

#     # Calcular a soma total dos scores médios
#     total_avg_score = sum(tag_avg_scores.values())

#     # Normalizar os scores médios dividindo pelo total de todos os scores
#     tag_normalized_scores = {tag: score / total_avg_score for tag, score in tag_avg_scores.items()}

#     # Converter os dados em um DataFrame para visualização
#     score_data = [{'Tag': tag, 'Average Score': tag_avg_scores[tag], 'Normalized Score': tag_normalized_scores[tag]} for tag in tag_avg_scores]
#     score_df = pd.DataFrame(score_data)


#     BAR_score_genre = px.bar(score_df, x='Tag', y='Normalized Score', title='Distribuição Normalizada dos Scores Médios por Gênero (Dividido pela Soma Total)', labels={'Tag':'Gênero', 'Normalized Score':'Score Normalizado'})
 