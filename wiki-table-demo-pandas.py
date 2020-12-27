import pandas as pd
wiki_url = 'https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives'
dfs = pd.read_html(wiki_url)
df = dfs[6]
df.to_csv('congress_table.csv', index=False, encoding='utf-8')