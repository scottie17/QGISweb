import jieba
import os

# Step 1: Set the input and output folders
input_folder = '/Users/zhangfengyue/Desktop/Digital Studies of Chinese Culture/hands-on-2/text1-20'  # Replace with your input folder path
output_folder = '/Users/zhangfengyue/Desktop/Digital Studies of Chinese Culture/hands-on-2/textjieba'  # Replace with your output folder path

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 2: Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_jieba.txt")

        # Step 3: Read the content of the file
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Step 4: Perform word segmentation
        words = jieba.cut(text)

        # Step 5: Join the segmented words with spaces
        segmented_text = ' '.join(words)

        # Step 6: Write the segmented text to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(segmented_text)

        print(f"Word segmentation complete for {filename}. Results saved to {output_file}")

print("All files processed successfully.")