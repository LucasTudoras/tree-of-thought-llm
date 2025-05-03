import pandas as pd

def filter_mate_in_2(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)

    # Keep only rows that contain "mateIn2" in the 'Themes' column
    filtered_df = df[df['Themes'].str.contains("mateIn2", na=False)]

    # Keep only the 'FEN' and 'Moves' columns
    result_df = filtered_df[['FEN', 'Moves']]

    # Save to a new CSV file
    result_df.to_csv(output_csv, index=False)

def main():
    input_file = "mate1_only.csv"     # Change this to your input file name
    output_file = "mate2_filtered.csv"  # Desired output file name
    filter_mate_in_2(input_file, output_file)
    print(f"Filtered mate-in-2 puzzles saved to: {output_file}")

if __name__ == "__main__":
    main()
