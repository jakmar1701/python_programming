import numpy as np
import pandas as pd


def load_data(path):
    """
    Load data from a CSV file into a Pandas DataFrame.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    DataFrame: The loaded data.
    """
    df = pd.read_csv(path)
    print(f"Data loaded from {path}.")
    return df


def drop_empty_rows(df):
    """
    Drop rows in a DataFrame that have less than 2 non-NA values.

    Parameters:
    df (DataFrame): The input DataFrame.

    Returns:
    DataFrame: The DataFrame after dropping rows.
    """
    print("Analyzing missing values in rows...")
    missing_values = df.isna().sum(axis=1).sort_values(ascending=False)
    print("Missing values in row (top 10 most empty rows): ")
    print(missing_values.head(10))
    print("Removing all rows that have less than 2 non-NA values.\n")
    df.dropna(thresh=2, inplace=True)
    print(f"Rows after removal: {df.shape[0]}")
    return df


def replace_missing_with_group_mean(df, col):
    """
    Replace missing values in a specified column of a DataFrame with the mean of their group of Level value.

    Parameters:
    df (DataFrame): The input DataFrame.
    col (str): The column in which to replace missing values.

    Returns:
    Series: The specified column after replacing missing values.
    """
    print(f"Replacing missing values in the '{col}' column with the group mean based on the 'Level' column.")
    mean_values_in_level_groups = df.groupby("Level")[col].mean()
    df[col] = df[col].fillna(df.Level.map(mean_values_in_level_groups))
    print("Replacement complete.")
    return df[col]


def scatter_plots(df, pairs):
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']

    ax = None
    for i, (x, y) in enumerate(pairs):
        # Use modulo operator to cycle through colors list
        color = colors[i % len(colors)]
        ax = df.plot.scatter(x=x, y=y, color=color, ax=ax, label=f'{x} vs {y}', marker='.')
    ax.set(xlabel='x')
    ax.set(ylabel='y')
    ax.legend()


def plot_polyfit_scatter(df, col_x, col_y, degree=3):
    """
    Plots a scatter plot of actual vs. predicted values based on a polynomial fit.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.
    col_x (str): The name of the column to use as the x-axis (independent variable).
    col_y (str): The name of the column to use as the y-axis (dependent variable).
    degree (int): The degree of the polynomial fit.

    Returns:
    ax: The axes with the scatter plot.
    """
    filtered_df = df[[col_x, col_y]].dropna()
    params = np.polyfit(
        x=filtered_df[col_x],
        y=np.exp(filtered_df[col_y]),
        deg=degree
    )
    filtered_df[f'{col_y}_pred'] = np.log(np.polyval(p=params, x=filtered_df[col_x]))
    ax = filtered_df.plot.scatter(x=col_x, y=col_y)
    filtered_df.plot.scatter(x=col_x, y=f'{col_y}_pred', color='red', marker='.', ax=ax)

    return params


def display_polynomial_equation(params):
    """
    Prints the polynomial equation based on the provided coefficients.

    This function generates a human-readable string representation of a polynomial equation,
    given the polynomial coefficients. The coefficients are assumed to be in the order
    of decreasing powers.

    Parameters:
    params (list or array): A list or array of polynomial coefficients.
        The first element corresponds to the highest degree, and the last to the constant term.

    Returns:
    None: This function only prints the polynomial equation and does not return any value.
    """
    equation = "y = " + " + ".join([f"({coef:.3f} * x^{i})" for i, coef in enumerate(params[::-1])])
    print("Polynomial Equation:", equation)


def calculate_polynomial_equation(df, col, params):
    """
    Calculate and add a column to the DataFrame with predicted values based on a polynomial equation.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.
    col (str): The name of the column used as the independent variable in the polynomial equation.
    params (list or array): Coefficients of the polynomial equation.

    Returns:
    DataFrame: The original DataFrame with an added column for predicted values.
    """
    df[f'{col}_pred'] = np.log(np.polyval(p=params, x=df[col]))
    return df


def describe(df):
    """
    Generate descriptive statistics for a DataFrame.

    Parameters:
    df (DataFrame): The pandas DataFrame to describe.

    Returns:
    DataFrame: A DataFrame containing count, mean, standard deviation, min, quartiles, and max for each column.
    """
    stats = pd.concat([
        df.count(),
        df.mean(),
        df.std(),
        df.min(),
        df.quantile(q=0.25),
        df.quantile(q=0.5),
        df.quantile(q=0.75),
        df.max()
    ], axis=1)
    stats.columns = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    # Transpose the DataFrame to have the same orientation as in pd.DataFrame.describe method
    stats = stats.T

    return stats


def detect_repeated_rows(df):
    """
    Detect and report the number of duplicated rows in a DataFrame.

    Parameters:
    df (DataFrame): The pandas DataFrame to check for duplicates.

    Returns:
    None: Prints a message indicating the number of duplicated rows.
    """
    duplicates = df.duplicated()
    if duplicates.any():
        num_duplicates = duplicates.sum()
        message = f"There are {num_duplicates} duplicated rows in the DataFrame."
    else:
        message = "There are no duplicated rows in the DataFrame."
    print(message)
