input_filename = "06.Project Input File.txt"
merge_filename = "06.Project Merge File.txt"
output_filename = "06.Project Output File.txt"
merge_marker = "Insert Merge File Here"

input_record_count = 0
merge_record_count = 0
output_record_count = 0

try:
    with open(input_filename, 'r') as infile, \
         open(merge_filename, 'r') as mergefile, \
         open(output_filename, 'w') as outfile:

        # Copy lines from input file until the merge marker is found
        for line in infile:
            input_record_count += 1
            output_record_count += 1
            if merge_marker in line:
                # Write the line containing the marker
                outfile.write(line)
                
                # Copy lines from merge file
                for merge_line in mergefile:
                    merge_record_count += 1
                    output_record_count += 1
                    outfile.write(merge_line)
                # After merging, continue with the rest of the input file
                break 
            else:
                outfile.write(line)

        # Continue copying lines from the input file if not all were processed before the merge
        for line in infile:
            input_record_count += 1
            output_record_count += 1
            outfile.write(line)

except FileNotFoundError:
    print(f"Error: One or more files not found. Ensure '{input_filename}', '{merge_filename}', and '{output_filename}' exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Number of records in {input_filename}: {input_record_count}")
print(f"Number of records in {merge_filename}: {merge_record_count}")
print(f"Number of records in {output_filename}: {output_record_count}")