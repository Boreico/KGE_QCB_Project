import pandas as pd
import argparse


def transpose_tsv(input_file, output_file):
    # Read the TSV file
    df = pd.read_csv(input_file, sep='\t', index_col=0)

    # Transpose the dataframe
    df_transposed = df.transpose()

    # Save the transposed dataframe
    df_transposed.to_csv(output_file, sep='\t')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transpose a TSV file with row and column names.")
    parser.add_argument("input_file", help="Path to the input TSV file")
    parser.add_argument("output_file", help="Path to save the transposed TSV file")

    args = parser.parse_args()

    transpose_tsv(args.input_file, args.output_file)
