'''
Program: saveToHtml.py
Description: A script that saves a specified url to the html_library directory as an HTML file.
Author: Matthew Ao
Usage: 
> python saveToHtml.py [-h] link folder Filename
  - link: The URL to be saved as an HTML file.
  - folder: The target subfolder to save the file in. Acceptable options: biology, chemistry, documents, firearms, handbook, toxicology. Do not include any backslashes.
  - filename: Specify the file name to be saved as. Do not include the .html extension.

For efficient use, paste the link, folder, and filename arguments on separate lines in saveToHtml.txt and run the following command from the command line: 

  > python saveToHtml.py @saveToHtml.txt
'''

# Import libraries
from bs4 import BeautifulSoup
import requests
import argparse
import os
import sys

# Create argument parser 
parser = argparse.ArgumentParser(prog='saveToHtml', description='Save a webpage as an HTML file in the html_library directory.', fromfile_prefix_chars='@')

# Add Link argument
parser.add_argument('Link', metavar='link', type=str, help='The URL to be saved as an HTML file.')

# Add Folder argument
parser.add_argument('Folder', metavar='folder', type=str, help='The target subfolder to save the file in. Acceptable options: biology, chemistry, documents, firearms, handbook, toxicology. Do not include any backslashes.')

# Add Filename argument
parser.add_argument('Filename', metavar='filename', type=str, help='Specify the file name to be saved as. Do not include the .html extension.')

# Parse the arguments 
args = parser.parse_args()

# Get the requested webpage
url = args.Link
page = requests.get(url)

# Check if request was successful; if not, terminate program
if not page.status_code==200:
  print('An error occurred in requesting the specified URL.')
  sys.exit()

# Set target folder path based on Folder argument
input_path = 'html_library/' + args.Folder

# Check if path exists; if not, terminate program
if not os.path.isdir(input_path):
  print('The target folder specified does not exist')
  sys.exit()

# Set file path based on Filename argument
filename = args.Filename
file_path = input_path + '/' + filename + '.html'

# Save the webpage as a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# Parse out the content in the main div
parsed_html = soup.find('div', class_='col-md-9 col-md-push-3')

# Save parsed HTML object as .html file in specified file path
with open(file_path, 'w') as f:
  f.write(parsed_html.prettify())