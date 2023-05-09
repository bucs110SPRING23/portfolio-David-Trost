import openai

class OpenAIPrompt:
    def __init__(self, api_key):
        openai.api_key = api_key

    def process_prompt_file(self):
        file_path = 'output.txt'  # Update the file path here
        with open(file_path, 'r') as file:
            prompt = file.read()
        return prompt

    def generate_completion(self, prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Classify the sentiment in the output.txt file",
            temperature=0.7,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=1,
            stop=None,
        )
        completion = response.choices[0].text
        return completion




