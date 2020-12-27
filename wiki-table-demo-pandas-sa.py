import pandas as pd
wiki_url = 'https://en.wikipedia.org/wiki/South_Africa_national_rugby_union_team'
dfs = pd.read_html(wiki_url, match='Club/province')
print(f'Total Tables: {len(dfs)}')
print(len(dfs))
df = dfs[0]
print(df)
df.to_csv('rugby_sa.csv', index=False, encoding='utf-8')