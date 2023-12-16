import asyncio
import httpx


async def fetch_url(url):  # fetch the content of a given URL using httpx.
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text, url


async def main():  # create a list of URLs to scrape and then asynchronously executes the fetch_url for each URL using asyncio.gather.
    urls = [
        'https://finance.yahoo.com',
        'https://www.scrapethissite.com/',
        'https://toscrape.com/',
    ]

    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result, url in results:
        print(
            f"URL: {url}\nContent: {result[:200]}...\n")  # print the first 100 characters of the fetched content for each URL.


if __name__ == "__main__":
    asyncio.run(main())

"""
def profiling():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        fetch_url()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    # stats.dump_stats(filename='needs_profiling.prof')

if __name__ == '__main__':
    profiling()
"""