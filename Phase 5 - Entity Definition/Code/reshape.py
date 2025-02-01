import pandas as pd
import argparse


def reshape_tsv(input_file, output_file):
    # Read the TSV file
    df = pd.read_csv(input_file, sep='\t')

    # Melt the dataframe to long format
    df_melted = df.melt(id_vars=["sampleID"], var_name="Taxonomy", value_name="relative_abundance")

    # Save the reshaped dataframe
    df_melted.to_csv(output_file, sep='\t', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reshape a TSV file from wide to long format.")
    parser.add_argument("input_file", help="Path to the input TSV file")
    parser.add_argument("output_file", help="Path to save the reshaped TSV file")

    args = parser.parse_args()

    reshape_tsv(args.input_file, args.output_file)
