// Typing effect
const text1 = "Makr2 test product quiz app";

let i = 0;
const speed = 100; // Typing speed in milliseconds

function typeWriter1() {
    if (i < text1.length) {
        document.getElementById("title1").innerHTML += text1.charAt(i);
        i++;
        setTimeout(typeWriter1, speed);
    }
}

document.body.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        document.querySelector('.btn-success').click(); // Programmatically click the button
    }
});

typeWriter1();




