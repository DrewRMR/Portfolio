import requests

# Replace with your actual Jotform API key and form ID
apiKey = '8ff7f0c89349c144290d5903f7aae3a1'
formID = '241575657782066'

url = f"https://eu-api.jotform.com/form/{formID}/submissions?apiKey={apiKey}"

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
    
    for submission in submissions:
        answers = submission.get('answers', {})
        # Replace '3' with the actual field ID you want to extract
        name_answer = answers.get('3', {}).get('answer', 'No name provided')
        print(name_answer)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
