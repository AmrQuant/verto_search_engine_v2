import requests
from bs4 import BeautifulSoup

def get_yahoo_results(keywords):
    try:
        url = f"https://search.yahoo.com/search?p={keywords}"
        headers = {'User-Agent': 'Mozilla/5.0'}  # Yahoo needs a user-agent header
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for result in soup.find_all('h3', {'class': 'title'}):
            link = result.find('a', href=True)
            if link:
                results.append({'title': result.get_text(), 'link': link['href'], 'source': 'Yahoo'})
                if len(results) == 10:  # Limit results to 10
                    break
        return results
    except requests.RequestException as e:
        print(f'Error with Yahoo Search: {e}')
        return []

# Existing Google and Bing functions ...

def aggregate_results(keywords):
    # Existing setup for Google and Bing API Keys...

    results = get_google_results(keywords, google_api_key, google_cse_id)
    results.extend(get_bing_results(keywords, bing_api_key))
    results.extend(get_yahoo_results(keywords))
    return results

# Main execution ...

