import pandas as pd
import os

# Specify the input file
input_file = 'amh_translated.csv'  # Replace with your input file name

# Generate output file name by appending '_ordered'
file_name, file_extension = os.path.splitext(input_file)
output_file = f"{file_name}_ordered{file_extension}"

# Read the file
df = pd.read_csv(input_file)

# Remove the "Disgust" column
if 'Disgust' in df.columns:
    df = df.drop(columns=['Disgust'])

# Reorder the columns
desired_order = ['id', 'text', 'Anger', 'Fear', 'Joy', 'Sadness', 'Surprise']
df = df[desired_order]

# Save the updated file
df.to_csv(output_file, index=False)

print(f"Reordered file saved as {output_file}.")
