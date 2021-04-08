from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/api/<int:id>', methods=['GET'])
def get_skill(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)