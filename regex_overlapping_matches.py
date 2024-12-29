import re

# The string to search in
# text = "onetwothreefourfivesixseveneightnine123456789"
text = "fiveight"

# Regular expression pattern to find digits or words from "one" to "nine"

# overlapping matches are not included
pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'

# include overlapping matches
pattern_include_overlap = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

# Find all matches in the text
matches = re.findall(pattern, text)
print(matches)

matches = re.findall(pattern_include_overlap, text)
print(matches)
