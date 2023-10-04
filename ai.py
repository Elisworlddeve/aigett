from textblob import TextBlob

# Function to analyze sentiment of text
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0:
        return "It sounds positive!"
    elif sentiment_score < 0:
        return "It seems negative."
    else:
        return "I don't sense a strong sentiment."

# Function to start AI
def start_ai():
    while True:
        print("AI Menu:")
        print("1. Analyze Text Sentiment")
        print("2. Respond to Question")
        print("3. Exit AI")
        ai_choice = input("Enter your AI choice (1/2/3): ")

        if ai_choice == '1':
            text_to_analyze = input("Enter the text you want to analyze: ")
            sentiment_result = analyze_sentiment(text_to_analyze)
            print(sentiment_result)
        elif ai_choice == '2':
            question = input("Ask a question: ")
            # Implement AI response to questions (not provided in this code)
        elif ai_choice == '3':
            print("Exiting AI. Goodbye!")
            break
        else:
            print("Invalid AI choice. Please select a valid option.")

if __name__ == "__main__":
    start_ai()
