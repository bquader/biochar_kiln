from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key (replace with your actual key)
openai.api_key = "your-api-key"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the frontend
        user_message = request.json.get('message', '')

        if not user_message:
            return jsonify({"reply": "Please enter a message!"}), 400

        # Create a context to focus responses on fertilizers and biochar
        context = "You are an expert on fertilizers and biochar. Provide concise and helpful answers to related questions."

        # Send the message to OpenAI's ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_message}
            ]
        )

        # Extract and send back the reply
        bot_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": "An error occurred while processing your request.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)