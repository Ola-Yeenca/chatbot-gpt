import gradio
import openai
import os

openai.api_key = os.getenv("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")

message = []

def chatbot(user_input, model="gpt-3.5-turbo"):
    try:
        message.append({"role": "user", "content": user_input})  # Add the question to the message history

        # Generate a response from OpenAI API
        response = openai.Completion.create(
            engine=model,
            prompt=' '.join(message),
            max_tokens=50,
            temperature=0.7
        )

        message.append(response.choices[0].text.strip())  # Add the generated response to the message history
        return response.choices[0].text.strip()  # Return the response

    except openai.Error as e:
        # Handle OpenAI API-specific errors
        error_message = f"OpenAI API error: {str(e)}"
        return error_message

    except Exception as e:
        # Handle any other general exceptions
        error_message = f"An error occurred: {str(e)}"
        return error_message

# Define the interface
demo = gradio.Interface(fn=chatbot,
                        inputs=gradio.inputs.Textbox(lines=2, label="How can I assist you today?"),
                        outputs=gradio.outputs.Textbox(lines=2),
                        title="Chat Bot"
                        )

# Launch the interface
demo.launch(share=True)
