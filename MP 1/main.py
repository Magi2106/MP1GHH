from src.loader import load_csv
from src.cleaner import clean_df
from src.anonymizer import anonymize
from src.visualizer import plot_hist

# Load data
df = load_csv('data/data.csv')

# Clean
df = clean_df(df)

# Anonymize
df = anonymize(df, 'email')

# Visualize
plot_hist(df, 'age')