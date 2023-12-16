import csv
from googlesearch import search
import asyncio
from bs4 import BeautifulSoup
import httpx
import pandas as pd


async def fetch_url_data(search_result, keyword):
    try:
        url = search_result.url

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        body_text = soup.body.text.lower()
        keyword_occurrences = body_text.count(keyword.lower())
        website_title = search_result.title.strip() if search_result.title else ''

        return {'URL': url, 'Keyword Occurrences': keyword_occurrences, 'Website Title': website_title}
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None


async def search_and_parse(keyword, num_results=10):
    search_results = list(search(keyword, num_results=num_results, advanced=True))

    tasks = []
    for search_result in search_results:
        tasks.append(fetch_url_data(search_result, keyword))

    # Gather all the results
    results = await asyncio.gather(*tasks)

    # Convert results to a pandas DataFrame
    df = pd.DataFrame(filter(None, results))

    # Write the DataFrame to a CSV file
    df.to_csv('output.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    keyword_to_search = 'HSN Code 71179090'  # Replace with the actual keyword you want to search for
    asyncio.run(search_and_parse(keyword_to_search, num_results=10))


# HSN 71179090
