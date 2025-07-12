from google.cloud import translate_v2 as translate
import csv
import sys
import os

def translate_to_english(text):
    client = translate.Client()
    result = client.translate(text, target_language="en")
    return result['translatedText']

def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, \
             open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            
            header = next(reader)
            writer.writerow(header)

            
            for row in reader:
                row_id = row[0]          
                sentence = row[1]       
                labels = row[2:]        
                try:
                    translated_sentence = translate_to_english(sentence)
                except Exception as e:
                    print(f"Error translating sentence '{sentence}': {e}")
                    translated_sentence = sentence  

                writer.writerow([row_id, translated_sentence] + labels)
        
        print(f"Translation complete. Output saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translate.py <input_csv_file>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = os.path.splitext(input_csv)[0] + "_translated.csv"

    process_csv(input_csv, output_csv)
