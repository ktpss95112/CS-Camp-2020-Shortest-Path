import re
from data import graph, source, best_solution

class Handler:
    def __init__(self, task_id, team_id):
        self.task_id = str(task_id)
        self.team_id = str(team_id)
        self.paths = {}
        self.scores = { k: 100 for k in best_solution[self.task_id].keys() }

    def __str__(self):
        return f'team {self.team_id} , task {self.task_id} , score {self.scores}'

    def receive(self, path):
        if not re.match(r'^[A-T],([0-9A-T]{1,3},)+[A-T]$', path):
            raise ValueError('Invalid path: bad format')

        path_list = path.split(',')
        start, end = path_list[0], path_list[-1]

        if start != source[self.task_id]:
            raise ValueError('Invalid path: bad start point')

        if end not in best_solution[self.task_id]:
            raise ValueError('Invalid path: bad end point')

        _sum = 0
        for i in range(len(path_list) - 1):
            for a, b, l in graph:
                if a == path_list[i] and b == path_list[i+1]:
                    _sum += l
                    break
                elif a == path_list[i+1] and b == path_list[i]:
                    _sum += l
                    break

        if _sum == 0:
            raise ValueError('Invalid path: bad internal points')

        score = _sum - best_solution[self.task_id][end]
        if score < self.scores[end]:
            self.paths[end] = path_list
            self.scores[end] = score

        return score

    def get_total_score(self):
        return sum(self.scores.values())
