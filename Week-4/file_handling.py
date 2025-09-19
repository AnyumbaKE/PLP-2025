#! /usr/bin/env python3

def modify_file(input_file, output_file):
    try:
        # Open the file & read 
        with open(input_file, "r") as f:
            content = f.read()

        # Modify file content 
        modified_content = content.upper()

        # Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Successfully modified and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# files generated
modify_file("input.txt", "output.txt")
