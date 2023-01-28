import requests
from bs4 import BeautifulSoup
#functions!!!!
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
	    packages.append(f'https://pypi.org/project/{package_element.text.strip()}')

    return packages

def scrape_js(query):
  # Make a request to the NPMJs search page
    response = requests.get("https://npmjs.com/search?q=" + query)

  # Parse the HTML content
    web = BeautifulSoup(response.content, "html.parser")

  # Find all the h3 elements that contain the package names
    package_elements = web.find_all(class_='db7ee1ac fw6 f4 black-90 dib lh-solid ma0 no-underline hover-black')

  # Extract the package names 
  packages = []
  for package_element in package_elements:
	  packages.append(f'https://npmjs.com/package/{package_element.text.strip().split()[0]}')

    return packages
