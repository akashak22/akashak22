from flask import Flask, request

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming_message():
    user_msg = request.form.get('Body')   
    sender = request.form.get('From')     
    print(f"From: {sender} | Message: {user_msg}")
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)