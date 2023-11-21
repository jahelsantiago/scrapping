from playwright.sync_api import sync_playwright
from threading import Thread
from scrapping.utils.urls import get_popular_companies_ulrs
import time

COMPANIES_PER_THRED = 62


def run1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 1", page.query_selector('h1').inner_text())

        page.close()


def run2():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 2", page_url, page.url, h1.inner_text())
            else:
                print("thred 2", page_url, page.url, "no h1")

        page.close()


def run3():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 3", page_url, page.url, h1.inner_text())
            else:
                print("thred 3", page_url, page.url, "no h1")

        page.close()


def run4():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 4", page_url, page.url, h1.inner_text())
            else:
                print("thred 4", page_url, page.url, "no h1")

        page.close()


def run5():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 5", page.query_selector('h1').inner_text())

        page.close()


def run6():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 6", page_url, page.url, h1.inner_text())
            else:
                print("thred 6", page_url, page.url, "no h1")

        page.close()


def run7():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 7", page_url, page.url, h1.inner_text())
            else:
                print("thred 7", page_url, page.url, "no h1")

        page.close()


def run8():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 8", page_url, page.url, h1.inner_text())
            else:
                print("thred 8", page_url, page.url, "no h1")

        page.close()


def run9():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 9", page.query_selector('h1').inner_text())

        page.close()


def run10():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 10", page_url, page.url, h1.inner_text())
            else:
                print("thred 10", page_url, page.url, "no h1")

        page.close()


def run11():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 11", page_url, page.url, h1.inner_text())
            else:
                print("thred 11", page_url, page.url, "no h1")

        page.close()


def run12():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 12", page_url, page.url, h1.inner_text())
            else:
                print("thred 12", page_url, page.url, "no h1")

        page.close()


def run13():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 13", page.query_selector('h1').inner_text())

        page.close()


def run14():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 14", page_url, page.url, h1.inner_text())
            else:
                print("thred 14", page_url, page.url, "no h1")

        page.close()


def run15():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)
            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 16", page_url, page.url, h1.inner_text())
            else:
                print("thred 16", page_url, page.url, "no h1")

        page.close()


def run16():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        pages_list = get_popular_companies_ulrs(COMPANIES_PER_THRED)
        for page_url in pages_list:
            page.goto(page_url)

            # print h1 element
            h1 = page.query_selector('h1')
            if h1:
                print("thred 16", page_url, page.url, h1.inner_text())
            else:
                print("thred 16", page_url, page.url, "no h1")

        page.close()


def main():
    start = time.time()

    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t3 = Thread(target=run3)
    t4 = Thread(target=run4)
    t5 = Thread(target=run5)
    t6 = Thread(target=run6)
    t7 = Thread(target=run7)
    t8 = Thread(target=run8)
    t9 = Thread(target=run9)
    t10 = Thread(target=run10)
    t11 = Thread(target=run11)
    t12 = Thread(target=run12)
    t13 = Thread(target=run13)
    t14 = Thread(target=run14)
    t15 = Thread(target=run15)
    t16 = Thread(target=run16)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

    end = time.time()

    print(f"Time taken {end-start}")


if __name__ == "__main__":
    main()
