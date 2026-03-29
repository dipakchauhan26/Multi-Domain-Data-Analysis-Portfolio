def group_sum(df, group_col, value_col):
    return df.groupby(group_col)[value_col].sum()


def group_mean(df, group_col, value_col):
    return df.groupby(group_col)[value_col].mean()


def value_counts(df, column):
    return df[column].value_counts()