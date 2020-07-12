'use strict';

let problemId = 0;
let teamToken = 0;

let payload = [];
let pathlen = 0;

let en2name = {
    A : '皓神學長',
    B : '唐浩學長跳舞好帥',
    C : '奇哥',
    D : '謝老闆',
    E : '裴裴學長',
    F : '王娜麗莎',
    G : '陳宇浩克',
    H : '力娜',
    I : '苗栗人',
    J : '守德',
    K : '宜蘭巨砲',
    L : '卑鄙昊新',
    M : '正義雲',
    N : 'Bert',
    O : '叡叡',
    P : '學一',
    Q : '阿鶴',
    R : '酒鬼敬能',
    S : '傑神',
    T : 'Mandy姐',
}


let startPoints = { 1: 'M', 2: 'C', 3: 'H' }
let specialPoints = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'];


function getDistance(from, to) {
    let answer = -1;

    neighbor.forEach((value, index, array) => {
        if (from === value[0] && to === value[1]) {
            answer = value[2];
        }
        else if (from === value[1] && to === value[0]) {
            answer = value[2];
        }
    });

    console.assert(answer !== -1);
    return answer
}


function setProblem(pid) {
    problemId = pid;

    document.getElementById('title').innerHTML = 'Your team token:'
    document.getElementById('select').innerHTML = `<input type="text" name="teamToken" id="teamToken"> <button onclick="setToken()">submit</button>`;
}


function renderSelect(from) {
    let html = '';

    neighbor.forEach((value, index, array) => {
        if (from === value[0]) {
            let tmp = value[1];
            if (specialPoints.includes(tmp)) {
                tmp = en2name[tmp];
            }
            html += `<button onclick="setTravel('${value[1]}')">${tmp} (距離 ${value[2]})</button> <br>`;
        }
        else if (from === value[1]) {
            let tmp = value[0];
            if (specialPoints.includes(tmp)) {
                tmp = en2name[tmp];
            }
            html += `<button onclick="setTravel('${value[0]}')">${tmp} (距離 ${value[2]})</button> <br>`;
        }
    });

    let replacedPayload = [];
    payload.forEach((value, index, array) => {
        let tmp = specialPoints.includes(value) ? en2name[value] : value;
        replacedPayload.push(tmp);
    });

    document.getElementById('current').innerHTML = 'Current path: ' + replacedPayload.join(' -> ') + '<br> Current length: ' + pathlen.toString();
    document.getElementById('title').innerHTML = 'Go to:';
    document.getElementById('select').innerHTML = html;
    document.getElementById('sidebar').innerHTML = '<button onclick="undo()">undo</button> <br>';
    if (payload.length !== 1 && destinations[problemId].includes(payload[payload.length - 1])) {
        document.getElementById('sidebar').innerHTML += '<button onclick="submit()">submit</button>';
    }
}


function setToken() {
    teamToken = document.getElementById('teamToken').value;
    payload.push(startPoints[problemId]);

    renderSelect(startPoints[problemId]);
}


function setTravel(point) {
    if (payload.length !== 0) {
        pathlen += getDistance(payload[payload.length - 1], point)
    }
    payload.push(point);

    renderSelect(point);
}


function undo() {
    pathlen -= getDistance(payload[payload.length - 1], payload[payload.length - 2]);
    payload.pop();

    renderSelect(payload[payload.length - 1]);
}


function submit() {
    window.location.href = 'submit?task=' + problemId.toString() + '&token=' + teamToken.toString() + '&path=' + payload.join(',');
}
