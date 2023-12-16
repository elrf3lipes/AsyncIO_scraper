import asyncio
import httpx
import cProfile
import pstats


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text, url


async def main():
    urls = [
        'https://finance.yahoo.com',
        'https://www.scrapethissite.com/',
        'https://toscrape.com/',
    ]

    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result, url in results:
        print(f"URL: {url}\nContent: {result[:200]}...\n")


def main2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    with cProfile.Profile() as pr:
        loop.run_until_complete(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='needs_profiling.prof')  # create proof file and open with


# run 'snakeviz ./needs_profiling.prof' from terminal to visualize

if __name__ == '__main__':
    main2()
