import unittest
from scrapping.utils.urls import get_companies_urls


def test_get_companies():
    companies_urls = get_companies_urls()
    print(companies_urls)
    assert False


if __name__ == "__main__":
    unittest.main()
