import requests

apiKey = '8ff7f0c89349c144290d5903f7aae3a1'
formID = '241575657782066'

def get_words_from_jotform(api_key, form_id):
    url = f"https://eu-api.jotform.com/form/{form_id}/submissions?apiKey={api_key}"

    try:
        # Make the API request
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Parse the response JSON
        data = response.json()

        # Print the raw JSON response for debugging
        print("Raw JSON response:")
        print(data)

        # Safely get the content list, default to empty list if not found
        submissions = data.get('content', [])
        
        if not submissions:
            print("No submissions found.")
            return []

        new_words = []
        for submission in submissions:
            answers = submission.get('answers', {})
            # Access the answer for ID '9'
            hangman_answer = answers.get('9', {}).get('answer', 'No answer provided')
            if hangman_answer != 'No answer provided':
                new_words.append(hangman_answer)
        
        return new_words
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []
