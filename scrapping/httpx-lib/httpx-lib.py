import asyncio
import httpx
from scrapping.utils.urls import get_companies_urls_from_csv
import time


async def fetch():
    async with httpx.AsyncClient() as client:
        companies = get_companies_urls_from_csv(100)
        print(companies)
        reqs = [client.get(company) for company in companies]

        resps = []
        for req in reqs:
            try:
                resp = await req
                resps.append(resp)
            except Exception as e:
                pass

        print(resps)


if __name__ == "__main__":
    time_start = time.time()
    asyncio.run(fetch())
    time_end = time.time()

    print(f"Downloaded sites in {time_end - time_start} seconds")
