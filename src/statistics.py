def basic_stats(series):
    return {
        "mean": series.mean(),
        "median": series.median(),
        "std": series.std()
    }


def correlation(df, cols):
    return df[cols].corr()