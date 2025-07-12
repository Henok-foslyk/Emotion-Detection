import csv
import sys

# Map relevant labels to their emotions
emotion_map = {1: "Anger", 4: "Fear", 5: "Joy", 6: "Sadness", 7: "Surprise"}
relevant_labels = set(emotion_map.keys())  # Only these labels are considered

# Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: python3 script.py input_file.tsv")
    sys.exit(1)

# Get input file from command-line argument
input_file = sys.argv[1]
output_file = "xed_fixed.csv"

# Process the file
with open(input_file, "r") as tsv_file, open(output_file, "w", newline="") as csv_file:
    tsv_reader = csv.reader(tsv_file, delimiter="\t")
    csv_writer = csv.writer(csv_file)

    # Write header
    header = ["Sentence", "Anger", "Fear", "Joy", "Sadness", "Surprise"]
    csv_writer.writerow(header)

    for row in tsv_reader:
        # Skip malformed rows
        if len(row) < 2:
            continue
        
        # Extract sentence and annotations
        sentence, annotations = row
        annotations = map(int, annotations.split(","))

        # Initialize binary flags for relevant emotions
        emotion_flags = {emotion: 0 for emotion in emotion_map.values()}

        # Set flags for relevant labels
        for label in annotations:
            if label in relevant_labels:
                emotion_flags[emotion_map[label]] = 1

        # Write to the CSV if at least one relevant label exists
        if any(emotion_flags.values()):
            csv_writer.writerow(
                [sentence] + [emotion_flags["Anger"], emotion_flags["Fear"], emotion_flags["Joy"], 
                              emotion_flags["Sadness"], emotion_flags["Surprise"]]
            )

print(f"Processed data saved to {output_file}")
