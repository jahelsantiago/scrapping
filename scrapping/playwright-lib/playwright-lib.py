from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from threading import Thread
from data import get_popular_companies_ulrs
import time

NUMBER_OF_THREADS = 10
COMPANIES_PER_THRED = 62
PAGE = 1


def create_run_function(thred_number: int):
    def run():
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()

            pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED, PAGE)
            for page_url in pages_list:
                try:
                    page.goto(page_url)
                except PlaywrightTimeoutError:
                    print(f"thread {thred_number}, {page_url} - error")
                    continue
                except Exception as e:
                    print(f"thread {thred_number}, {page_url} - error: {e}")
                    continue
                # print web page title
                try:
                    title = page.title()
                    print(f"Thread {thred_number} - {title}")
                except Exception as e:
                    print(f"thread {thred_number}, {page_url} - error: {e}")
                    continue



            page.close()
    return run


def main():
    start = time.time()

    # create threads
    threads = []
    for i in range(NUMBER_OF_THREADS):
        threads.append(Thread(target=create_run_function(i+1)))

    # start threads
    for thread in threads:
        thread.start()

    # join threads
    for thread in threads:
        thread.join()

    end = time.time()

    print(f"Time taken {end-start}")


if __name__ == "__main__":
    main()
