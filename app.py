from flask import Flask, request, url_for, render_template, send_file
app = Flask(__name__)

from task import Handler
from data import graph, token2team, en2name


handlers = {
    '1': [ Handler(1, team_id) for team_id in range(11) ],
    '2': [ Handler(2, team_id) for team_id in range(11) ],
    '3': [ Handler(3, team_id) for team_id in range(11) ],
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/submit')
def submit():
    path = request.args.get('path')
    token = request.args.get('token')
    task = request.args.get('task')

    if token not in token2team:
        return '<p>Invalid token</p> <a href="/">Go back</a>'
    team_id = token2team[token]

    if task not in ('1', '2', '3'):
        return '<p>Invalid task id</p> <a href="/">Go back</a>'

    try:
        score = handlers[task][team_id].receive(path)
    except ValueError as e:
        return f'<p>{e}</p> <a href="/">Go back</a>'


    print(f'team: {token2team[token]}')
    print(f'task: {task}')
    print(f'path: {path}')
    print(f'score: {score}')
    print()

    ret_path = ' ⮕ '.join([ en2name[s] if s in en2name else s for s in path.split(',') ])
    return render_template('success.html', team_id=team_id, path=ret_path, score=score)


@app.route('/aaaaadmin')
def admin():
    return render_template('admin.html', handlers=handlers)


if __name__ == "__main__":
    app.run('0.0.0.0')
