import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(df, column):
    sns.histplot(df[column], kde=True)
    plt.show()