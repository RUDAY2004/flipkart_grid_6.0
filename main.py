import os  # Make sure to import the os module
from voice_recognition import listen_to_audio
from text_to_speech import speak_text
from chatgpt_integration import get_response  # Now using GroqCloud for responses
import flipkart_scraper  # Your scraper module for product info

# Set the Groq API key
os.environ['GROQ_API_KEY'] = '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'

def main():
    while True:
        # Listen to the customer's query via voice input
        query = listen_to_audio()
        print(f"Query: {query}")
        
        if 'exit' in query.lower():
            speak_text("Exiting the program.")
            break
        
        # Get the response from GroqCloud via the get_response function
        gpt_response = get_response(query)
        
        # Retrieve product information based on the query
        product_info = flipkart_scraper.get_product_info(query)
        
        # Combine both the AI response and the product information
        response = f"{gpt_response}\n{product_info}"
        
        # Output the combined response
        print(f"Response: {response}")
        speak_text(response)

if __name__ == "__main__":
    main()
