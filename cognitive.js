
const videoData = [
    {
        video: "C:/Users/Samanth Abbur/digital rehab/rehave2/vedios/videoplayback.mp4",
        transcript: "Barbie biryani is looking good, right?, Pink colored masala, pink colored rice. And this is Oppenheimer biryani. Black colored masala, black colored rice. And no, it's not burnt. Barbie biryani is raita, so it should be barbie, right? Oppenheimer raita for Oppenheimer biryani. Want to taste? No, taste! Taste!",
        questions: ["What is the main topic discussed?", "What was mentioned at the end?"]
    },

    {
        video: "C:/Users/Samanth Abbur/digital rehab/rehave2/vedios/Why springs are NOT made from Ｉ-beams.mp4",
        transcript: "Springs are made out of round metal and square metal or even some kind of profile because when you compress a spring you are not bending the metal lengthwise you are twisting it and because circles are the most efficient shape for torque loads",
        questions: ["Who is the speaker?", "What are the key points highlighted?"]
    }
];

let currentVideoIndex = 0;

const videoPlayer = document.getElementById('video-player');
const videoSource = document.getElementById('video-source');
const questionsContainer = document.getElementById('questions-container');
const nextVideoButton = document.getElementById('next-video');

function loadVideo(index) {
    const video = videoData[index];
    videoSource.src = video.video;
    videoPlayer.load();

    questionsContainer.innerHTML = "<h2>Questions</h2>";
    video.questions.forEach((question, i) => {
        const questionElement = document.createElement('p');
        questionElement.textContent = `${i + 1}. ${question}`;
        questionsContainer.appendChild(questionElement);
    });
}

nextVideoButton.addEventListener('click', () => {
    currentVideoIndex = (currentVideoIndex + 1) % videoData.length;
    loadVideo(currentVideoIndex);
});

// Load the first video on page load
loadVideo(currentVideoIndex);
