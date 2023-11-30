const $input = document.querySelector('input');
const $button = document.querySelector('.search_btn1');
// const $answer = document.querySelector('.answer');

const data = [{
    "role": "system",
    "content": "assistant는 채팅 봇이다."
}];

const url = `http://127.0.0.1:8000/Conversation/chatbot/`;

const answerElement = document.querySelector('.search_answer');
const answerContent = document.getElementById('search_answerContent');

$button.addEventListener('click', (e) => {
    e.preventDefault();

    // const productType = document.getElementById('productType').value;
    const question = document.querySelector('input').value;

    data.push({
        "role": "user",
        "content": question,
    })

    $input.value = ''

    chatGPTAPI()
})

function chatGPTAPI() {

    const loadingMessage = document.getElementById('loading_msg');
    loadingMessage.style.display = 'block';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
        redirect: 'follow',
        max_tokens: 150, // 응답으로 받을 최대 토큰 수 지정
        temperature: 0.7, // 다양한 응답을 얻기 위한 온도 설정 (조절 가능)
    })
    .then(res => res.json())
    .then(res => {
        loadingMessage.style.display = 'none';
        answerElement.style.display = 'flex';
        answerContent.innerHTML = `<p>${res.choices[0].message.content.replace(/\n/g, '<br>')}</p>`
    })
}