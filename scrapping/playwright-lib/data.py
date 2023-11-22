import csv
import os


def get_popular_companies_ulrs(limit: int, page: int = 1) -> list:
    path = r"./websites.csv"

    companies_urls = read_csv(path)

    for i, company in enumerate(companies_urls):
        companies_urls[i] = add_https_to_url(company[1])

    companies_urls = cropp_data(companies_urls, limit, page)
    return companies_urls


def cropp_data(data: list, limit: int, page: int) -> list:
    """
    Crop the given data based on the specified limit and page.

    Args:
        data (list): The input data to be cropped.
        limit (int): The maximum number of items per page.
        page (int): The page number.

    Returns:
        list: The cropped data based on the limit and page.
    """
    start = (page-1)*limit
    end = start + limit
    return data[start:end]


def read_csv(path: str) -> list:
    with open(path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def add_https_to_url(url: str) -> str:
    # check if contains http or https
    if (url.startswith("http://") or url.startswith("https://")):
        return url
    else:
        return f"https://{url}"
