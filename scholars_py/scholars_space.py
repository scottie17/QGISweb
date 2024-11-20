import os
# Specify input and output folders
input_folder = '/Users/zhangfengyue/Desktop/Digital Studies of Chinese Culture/hands-on-2/text1-20'
output_folder = '/Users/zhangfengyue/Desktop/Digital Studies of Chinese Culture/hands-on-2/textspace'
# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Process all txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_spaced.txt")

        try:
            # Read the content of the input file
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                content = input_file.read()

            # Add a space between each character
            spaced_content = ' '.join(content)

            # Write the spaced content to the output file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(spaced_content)

            print(f"Processing complete for {filename}. Output saved to {output_file_path}")

        except FileNotFoundError:
            print(f"Error: The file {filename} was not found in the input folder.")
        except IOError as e:
            print(f"Error: An I/O error occurred while processing {filename}: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {filename}: {str(e)}")

print("All files processed.")