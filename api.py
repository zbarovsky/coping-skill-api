from flask import Flask, render_template, url_for, request, redirect, jsonify
from skills import coping_skills

app = Flask(__name__)

# landing page for API
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# show all coping skills
@app.route('/api/get_all', methods=['GET'])
def get_all():
    return jsonify(coping_skills)

# get coping skill by id passed from frontend
@app.route('/api/<int:id>', methods=['GET'])
def get_skill(id):
    return jsonify(coping_skills[id])

if __name__ == '__main__':
    app.run(debug=True)