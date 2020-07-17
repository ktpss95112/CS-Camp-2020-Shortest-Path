from flask import Flask, request, url_for, render_template, send_file
app = Flask(__name__)

from task import Handler
from data import graph, token2team, en2name

from random import randint
from os import listdir

server_id = randint(1000000000, 10000000000-1)

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

    print(f'server_id: {server_id}')
    print(f'team: {team_id}')
    print(f'task: {task}')
    print(f'path: {path}')
    print(f'score: {score}')
    print()

    open(f'result/{server_id}-{task}-{team_id}.txt', 'a').write(path + '\n')

    ret_path = ' ⮕ '.join([ en2name[s] if s in en2name else s for s in path.split(',') ])
    return render_template('success.html', team_id=team_id, path=ret_path, score=score)


@app.route('/aaaaadmin')
def admin():
    global server_id
    print(f'server_id: {server_id} (admin)')
    print()

    for f_name in listdir('result'):
        server_id = f_name.split('-')[0]
        task = f_name.split('-')[1]
        team_id = int(f_name.split('-')[2].split('.')[0])

        for line in open(f'result/{f_name}').read().strip().split('\n'):
            handlers[task][team_id].receive(line)

    return render_template('admin.html', handlers=handlers)


if __name__ == "__main__":
    app.run('0.0.0.0')
