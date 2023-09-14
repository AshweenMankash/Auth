from flask import Flask, request

app = Flask()

@app.route('/login', method=["POST"])
def login():
    payload = request.get_json()
    
    return {
        "message": "Wrong Password"
    }

if __name__ == "__main__":
    app.run(debug=True)
