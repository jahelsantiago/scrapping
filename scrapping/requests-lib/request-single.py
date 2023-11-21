import requests
from bs4 import BeautifulSoup
from scrapping.utils.urls import get_companies_urls
import time     


def get_h1_from_url(url):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        print(f"Read {len(response.content)} from {url}")

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text from the first h1 element
        h1_element = soup.find('h1')
        if h1_element:
            h1_text = h1_element.get_text(strip=True)
            return h1_text
        else:
            return "No h1 element found"

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    time_start = time.time()

    h1 = []

    for index, sites_batch in enumerate(get_companies_urls(10, 100, 1)):
        for url in sites_batch:
            print("processing: ", url)
            h1_ellemnt = get_h1_from_url(url)
            if h1_ellemnt:
                h1.append(h1_ellemnt)

        print(f"Processed {index*20} sites in {time.time() - time_start} seconds")        

    time_end = time.time()

    print(f"Downloaded sites in {time_end - time_start} seconds")
    print(f"Correctly downloaded {len(h1)} sites")
    print(h1)
