import os
import json
from textblob import TextBlob

# Define the folder for memory data
memory_folder = ".MEM"
os.makedirs(memory_folder, exist_ok=True)

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

# Function to save memory data as a JSON file
def save_memory_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Function to load memory data from a JSON file
def load_memory_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    else:
        return None

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
        print("1. Analyze Text Sentiment")
        print("2. Respond to Question")
        print("3. Save Memory")
        print("4. Load Memory")
        print("5. Exit AI")
        ai_choice = input("Enter your AI choice (1/2/3/4/5): ")

        if ai_choice == '1':
            text_to_analyze = input("Enter the text you want to analyze: ")
            sentiment_result = analyze_sentiment(text_to_analyze)
            print("Sentiment Summary:", sentiment_result["sentiment_summary"])
            print("Keywords:", sentiment_result["keywords"])
            print("Overall Positive Score:", sentiment_result["overall_positive_score"])

            memory_data["sentences"].append({
                "text": text_to_analyze,
                "sentiment_summary": sentiment_result["sentiment_summary"],
                "keywords": sentiment_result["keywords"],
                "overall_positive_score": sentiment_result["overall_positive_score"]
            })
        elif ai_choice == '2':
            question = input("Ask a question: ")
            response = "AI responds to questions with a placeholder answer."
            print(response)
        elif ai_choice == '3':
            save_memory_data(memory_data, memory_filename)
            print("Memory saved successfully.")
        elif ai_choice == '4':
            memory_data = load_memory_data(memory_filename)
            if memory_data:
                print("Memory loaded successfully.")
            else:
                print("Memory file does not exist or is empty.")
        elif ai_choice == '5':
            print("Exiting AI. Goodbye!")
            break
        else:
            print("Invalid AI choice. Please select a valid option.")

if __name__ == "__main__":
    start_ai()
