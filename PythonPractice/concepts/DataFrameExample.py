# pandas is a third-party library for working with structured, tabular data.
# The `try` block lets this example still start even when pandas is not installed;
# the ImportError is handled below with a clear message instead of a traceback.
try:
    import pandas as pd
except ImportError:
    # Use None as a marker so main() can detect that pandas is unavailable.
    pd = None


def main() -> None:
    """Create a small table and demonstrate common DataFrame operations.

    A DataFrame is pandas' two-dimensional table: it has labeled columns and
    rows, much like a spreadsheet or a database table.
    """
    if pd is None:
        # Stop before using pandas if its import failed. Installing the package
        # in the Python environment that runs this script resolves this case.
        print("pandas is not installed. In the activated virtual environment, run: python3 -m pip install pandas")
        return

    # A dictionary is a convenient way to describe a table: each key becomes
    # a column name, and each list supplies that column's values from top to
    # bottom. The lists must contain the same number of values (one per row).
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
    }

    # pandas converts the dictionary into a labeled, two-dimensional table.
    # It aligns values by their list positions and creates a row index (0, 1, 2).
    df = pd.DataFrame(data)

    # Printing a DataFrame displays its row index, column labels, and values.
    print("DataFrame:")
    print(df)

    # Indexing with one column label returns that column as a pandas Series,
    # which is a one-dimensional labeled collection of values.
    print("\nAges column:")
    print(df["Age"])

    # Comparisons on a Series are vectorized: pandas checks every age at once
    # and returns a True/False value for each row. Assigning those values under
    # a new label adds a derived column without an explicit loop.
    df["IsAdult"] = df["Age"] >= 18
    print("\nWith IsAdult column:")
    print(df)

    # describe() computes a set of common descriptive statistics for numeric
    # data, including count, mean, standard deviation, minimum, quartiles, and
    # maximum. It summarizes the Age column in this example.
    print("\nAge stats:")
    print(df["Age"].describe())

    # Export the table as a comma-separated-values (CSV) file. CSV is a simple
    # text format that spreadsheet programs and many other tools can read.
    output_csv = "example_dataframe.csv"
    # index=False omits pandas' generated row labels from the file; otherwise,
    # they would be written as an extra first column in the CSV.
    df.to_csv(output_csv, index=False)
    print(f"\nSaved to {output_csv}")


# This condition is true when the file is run directly, but false when it is
# imported as a module by another Python file. The guard prevents main() from
# running automatically on import.
if __name__ == "__main__":
    main()
