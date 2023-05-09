from news import NewsAPI
from sentiment import OpenAIPrompt

def main():
    api = NewsAPI()
    query = input("Enter a query: ")

    params = {'language': 'en'}
    api.get_articles(query, params)

    openai_prompt = OpenAIPrompt(api_key="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")
    prompt = openai_prompt.process_prompt_file()
    completion = openai_prompt.generate_completion(prompt)

    print("Generated completion:", completion)
    

if __name__ == "__main__":
    main()