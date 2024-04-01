import csv

def generate_csv(data, filename):
  """Generates a CSV file with the provided data."""
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Column 1", "Column 2", "Column 3"])  # Header row
    writer.writerows(data)  # Write data rows

# Example data
data = [
  [1, "Value A", True],
  [2, "Value B", False],
  [3, "Value C", True],
]

# Generate CSV file
generate_csv(data, "generated_data.csv")
print("CSV file generated: generated_data.csv")
