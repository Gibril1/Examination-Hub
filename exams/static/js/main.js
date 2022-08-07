const question = document.getElementById('question');
const answer = document.getElementById('answers');
const clear = document.getElementById('clear');

clear.addEventListener('click', (e) => {
    e.preventDefault();
    question.value = '';
    answer.value = '';
})