import csv


def get_popular_companies_ulrs(limit: int) -> list:
    path = "scrapping/data/websites.csv"
    companies_urls = read_csv(path)

    for i, company in enumerate(companies_urls):
        companies_urls[i] = add_https_to_url(company[1])

    companies_urls = companies_urls[:limit]
    return companies_urls


def get_companies_urls(batch_lenght: int, limit: int, page: int) -> list:
    path = "scrapping/data/companies-url.csv"
    companies_urls = read_csv(path)
    for i, company in enumerate(companies_urls):
        companies_urls[i] = add_https_to_url(company[0])

    companies_urls = cropp_data(companies_urls, limit, page)

    # return a list of utls with max length of batch_size
    batch_number = int(len(companies_urls)/batch_lenght)
    for i in range(batch_number):
        yield companies_urls[i*batch_lenght:(i+1)*batch_lenght]


def get_companies_urls_from_csv(limit=100) -> list:
    path = "scrapping/data/companies-url.csv"
    companies_urls = read_csv(path)
    for i, company in enumerate(companies_urls):
        companies_urls[i] = add_https_to_url(company[0])
    companies_urls = companies_urls[:limit]
    return companies_urls


def read_csv(path: str) -> list:
    with open(path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def cropp_data(data: list, limit: int, page: int) -> list:
    start = (page-1)*limit
    end = start + limit
    return data[start:end]


def add_https_to_url(url: str) -> str:
    # check if contains http or https
    if (url.startswith("http://") or url.startswith("https://")):
        return url
    else:
        return f"https://{url}"
