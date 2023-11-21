import asyncio
import httpx
from bs4 import BeautifulSoup
import time
from scrapping.utils.urls import get_companies_urls


async def download_site(session, url, h1_list):
    async with session.get(url) as response:
        content_length = response.content_length
        print("Read {0} from {1}".format(content_length, url))

        if (content_length is None):
            return

        # Parse HTML content
        html_content = await response.text()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the text from the first h1 element
        h1_element = soup.find('h1')
        if h1_element:
            h1_text = h1_element.get_text(strip=True)
            h1_list.append(h1_text)  # Append h1 text to the list
        else:
            print("No h1 element found")


async def download_all_sites(sites):
    h1_list = []  # Create a list to store h1 text
    async with httpx.AsyncClient() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url, h1_list))
            tasks.append(task)
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Print exceptions
        for result in results:
            if isinstance(result, Exception):
                print(f"Error: {result}")

    print(h1_list)

if __name__ == "__main__":
    total_processed = 0
    start_time = time.time()

    for sites_batch in get_companies_urls(20, 100, 1):
        total_processed += len(sites_batch)
        asyncio.get_event_loop().run_until_complete(download_all_sites(sites_batch))

        duration = time.time() - start_time
        print(f"Processed {total_processed} sites in {duration} seconds")

    print(f"Downloaded {total_processed} sites in {duration} seconds")
