from flask import Flask, render_template, url_for, request, redirect, jsonify
from skills import coping_skills

app = Flask(__name__)

# landing page for API
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# show all coping skills
@app.route('/api/copingskill/get_all', methods=['GET'])
def get_all():
    return jsonify(coping_skills)

# get coping skill by id passed from frontend
@app.route('/api/copingskill/', methods=['GET'])
def get_skill():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided."

    if id not in range(len(coping_skills)):
        return "Error, invalid id"
    else: 
        return jsonify(coping_skills[id])

if __name__ == '__main__':
    app.run(debug=True)