df = pd.read_csv(
    arquivo,
    encoding='latin1',
    sep=';',
    decimal=','
)

df.columns = [col.strip().lower() for col in df.columns]
df = df.rename(columns={
    'abertura': 'open',
    'máxima': 'high',
    'mínima': 'low',
    'fechamento': 'close',
    'data': 'date'
})

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df.set_index('date', inplace=True)
