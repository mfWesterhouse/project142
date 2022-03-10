import pandas
import numpy

df = pd.read_csv("shared_articles.csv")

total_events = df['eventType']
df['total events'] = total_events
df = df.sort_values('total events', ascending=True)
