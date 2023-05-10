import gradio
import openai
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("API_KEY")
openai.api_key = api_key


messages = [{"role": "system", "content": "You know everything"}]


def chatbot(user_input, model="gpt-3.5-turbo"):
    try:
        messages.append({"role": "user", "content": str(user_input)})  # Add the question to the message history

        # Generate a response from OpenAI API
        response = openai.Completion.create(
                engine=model,
                prompt=' '.join([message['content'] for message in messages]),
                max_tokens=50,
                temperature=0.7
            )


        messages.append(response.choices[0].text.strip())  # Add the generated response to the message history
        return response.choices[0].text.strip()  # Return the response

    except Exception as e:
        # Handle any exceptions, including OpenAI API errors
        error_message = f"An error occurred: {str(e)}"
        return error_message

# Define the interface
demo = gradio.Interface(fn=chatbot,
                        inputs=gradio.inputs.Textbox(lines=2, label="How can I assist you today?"),
                        outputs=gradio.outputs.Textbox(),
                        title="Chat Bot"
                        )

# Launch the interface
demo.launch(share=True)
