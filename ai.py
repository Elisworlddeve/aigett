import os
import json
import wikipediaapi
from textblob import TextBlob
import nltk
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
import datetime  # Added to handle date and time

# Define the folder for AI configuration
ai_config_folder = "Aiconfig"
os.makedirs(ai_config_folder, exist_ok=True)

# Define the folder for personalities
personalities_folder = os.path.join(ai_config_folder, "Personalities")
os.makedirs(personalities_folder, exist_ok=True)

# Define the folder for memory data
memory_folder = os.path.join(ai_config_folder, "Memory")
os.makedirs(memory_folder, exist_ok=True)

# Define the path for certification file
certification_file = os.path.join(ai_config_folder, "Certification.txt")

# Initialize NLTK resources
nltk.download('brown')
nltk.download('punkt')

# Function to analyze sentiment of text
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    subjectivity_score = analysis.sentiment.subjectivity

    sentiment_summary = "neutral"
    if sentiment_score > 0:
        sentiment_summary = "positive"
    elif sentiment_score < 0:
        sentiment_summary = "negative"

    keywords = analysis.noun_phrases
    overall_positive_score = (sentiment_score + 1) / 2  # Normalize to [0, 1]

    result = {
        "sentiment_summary": sentiment_summary,
        "keywords": keywords,
        "overall_positive_score": overall_positive_score
    }

    return result

# Function to start AI
def start_ai():
    memory_filename = os.path.join(memory_folder, "memory.json")
    memory_data = load_memory_data(memory_filename)

    if memory_data is None:
        memory_data = {
            "sentences": []
        }

    while True:
        print("AI Menu:")
        print("1. Respond to Question")
        print("2. Save Memory")
        print("3. Load Memory")
        print("4. Check for Updates from GitHub")
        print("5. Load Other Personality Files")
        print("6. Exit AI")
        ai_choice = input("Enter your AI choice (1/2/3/4/5/6): ")

        if ai_choice == '1':
            question = input("Ask a question: ")
            response = get_ai_response(question, memory_data)
            print(response)
        elif ai_choice == '2':
            save_memory_data(memory_data, memory_filename)
            print("Memory saved successfully.")
        elif ai_choice == '3':
            memory_data = load_memory_data(memory_filename)
            if memory_data:
                print("Memory loaded successfully.")
            else:
                print("Memory file does not exist or is empty.")
        elif ai_choice == '4':
            check_for_updates()
        elif ai_choice == '5':
            load_personality_files()
        elif ai_choice == '6':
            print("Exiting AI. Goodbye!")
            break
        else:
            print("Invalid AI choice. Please select a valid option.")

# Function to save memory data as a JSON file
def save_memory_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # Update certification file with the date and time of save
    update_certification_file()

# Function to load memory data from a JSON file
def load_memory_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    else:
        return None

# Function to check for updates from GitHub
def check_for_updates():
    # Implement code to check for updates here
    print("Checking for updates from GitHub...")
    # Provide information about commits, dates, and size of the update, if available

# Function to load other personality files
def load_personality_files():
    # Implement code to load other personality files here
    print("Loading other personality files...")
    # Allow the user to select a personality file to load

# Function to get AI response based on the question and memory data
def get_ai_response(question, memory_data):
    found_data = search_information(question, memory_data)

    if found_data:
        response = "I found information related to your question:\n"
        response += f"Keywords: {', '.join(found_data['keywords'])}\n"
        response += f"Overall Sentiment: {found_data['sentiment_summary']}\n"
        response += "Here's a brief summary of the information:\n"
        response += found_data["summary"]
    else:
        response = "I couldn't find information related to your question."

    return response

# Function to search for information in memory data
def search_information(question, memory_data):
    # Implement search logic based on keywords and question
    # Return relevant information if found, or None if not found

# Function to update the certification file with the current date and time
def update_certification_file():
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S CST")
    with open(certification_file, 'w') as cert_file:
        cert_file.write(current_datetime)

if __name__ == "__main__":
    start_ai()
