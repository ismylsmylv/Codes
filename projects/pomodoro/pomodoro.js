const bells = new Audio('./bell.mp3');
const startBtn = document.querySelector('.btn-start');
const session = document.querySelector('.minutes');
let myInterval;
let state = true;
let totalSeconds = 0;

const appTimer = () => {
    if (state) {
        state = false;
        const sessionAmount = Number.parseInt(session.textContent);
        totalSeconds = sessionAmount * 60;
        myInterval = setInterval(updateSeconds, 1000);
        // Play the audio after the user clicks the "start" button
        bells.play();
    } else {
        alert('Session already started');
    }
};

const updateSeconds = () => {
    const minuteDiv = document.querySelector('.minutes');
    const secondDiv = document.querySelector('.seconds');

    totalSeconds--;

    let minutesLeft = Math.floor(totalSeconds / 60);
    let secondsLeft = totalSeconds % 60;

    if (secondsLeft < 10) {
        secondDiv.textContent = '0' + secondsLeft;
    } else {
        secondDiv.textContent = secondsLeft;
    }
    minuteDiv.textContent = `${minutesLeft}`;

    if (minutesLeft === 0 && secondsLeft === 0) {
        clearInterval(myInterval);
    }
};

startBtn.addEventListener('click', appTimer);
