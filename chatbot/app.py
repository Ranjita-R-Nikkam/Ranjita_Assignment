from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()  # convert to lowercase

    # Custom FAQ rules
    if 'hello' in user_message:
        reply = "Hi there! How can I help you?"
    elif 'your name' in user_message:
        reply = "I'm a Flask Chatbot!"
    elif 'program details' in user_message:
        reply = "Iron Lady offers leadership programs focused on confidence, career growth, and communication."
    elif 'duration' in user_message:
        reply = "The course duration is 3 months."
    elif 'mode' in user_message:
        reply = "The program is conducted onsite."
    elif 'certification' in user_message:
        reply = "Yes! You will receive a certificate upon completion of the course."
    elif 'mentors' in user_message:
        reply = "Our mentors are industry experts and experienced leaders."
    else:
        reply = "I didn't understand that. Please ask about program details, duration, mode, certification, or mentors."

    return jsonify({'reply': reply})

if __name__== '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
