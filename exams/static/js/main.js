const question = document.getElementById('question');
const answer = document.getElementById('answers');
const clear = document.getElementById('clear');

// this piece of code is used to clear the fields for setting questions
clear.addEventListener('click', (e) => {
    e.preventDefault();
    question.value = '';
    answer.value = '';
})