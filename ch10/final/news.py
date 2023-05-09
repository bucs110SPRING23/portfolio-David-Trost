import requests

class NewsAPI:
    BASE_URL = 'https://newsapi.org/v2/'
    API_KEY = '4bc51311e8a64a7fb3cf424d57427eb5' 

    def get_articles(self, query, params):
        endpoint = 'everything'
        params['q'] = query
        params['apiKey'] = self.API_KEY

        url = self.BASE_URL + endpoint

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            articles = data.get('articles', [])

            # Write titles to a .txt file
            with open('output.txt', 'w') as file:
                for article in articles:
                    title = article.get('title', '')
                    file.write(title + '\n')

            print("Titles written to output.txt successfully.")
        else:
            print(f"Error: {data.get('message')}")

