import matplotlib.pyplot as plt
import seaborn as sns

def line_plot(data, title, xlabel, ylabel):
    plt.figure()
    data.plot()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def bar_plot(data, title):
    plt.figure()
    data.plot(kind='bar')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()


def histogram(data, column):
    plt.figure()
    sns.histplot(data[column], kde=True)
    plt.title(f"{column} Distribution")
    plt.show()


def heatmap(data):
    plt.figure()
    sns.heatmap(data.corr(numeric_only=True), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()