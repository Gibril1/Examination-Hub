const question = document.getElementById('question');
const answer = document.getElementById('answers');
const post = document.getElementById('post');

post.addEventListener('click', (e) => {
    e.preventDefault();
    question.value = '';
    answer.value = '';
})