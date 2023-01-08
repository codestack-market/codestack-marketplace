import requests
from bs4 import BeautifulSoup

def scrape_py(query):
  # Make a request to the PyPI search page
  response = requests.get("https://pypi.org/search/?q=" + query)

  # Parse the HTML content
  web = BeautifulSoup(response.content, "html.parser")

  # Find all the h3 elements that contain the package names
  package_elements = web.find_all(class_='package-snippet__name')

  # Extract the package names 
  packages = []
  for package_element in package_elements:
    packages.append(f'https://pypi.com/project/{package_element.text.strip().split()[0]}')

  return packages

