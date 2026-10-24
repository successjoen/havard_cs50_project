// Show welcome alert when the page loads
window.onload = function () {
    alert("Welcome to my homepage! 🎉");
    updateClock(); // Start the clock immediately
    setInterval(updateClock, 1000); // Update clock every second
};

// Function to change background color randomly
function changeBackground() {
    const colors = ["#f8b400", "#6a2c70", "#b83b5e", "#00bdaa", "#1a1a2e"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
}

// Function to update live clock
function updateClock() {
    const clock = document.getElementById("clock");
    const now = new Date();
    clock.textContent = now.toLocaleTimeString();
}

// Handle form submission without reloading
function handleForm(event) {
    event.preventDefault();
    const nameInput = document.getElementById("name").value;
    const message = document.getElementById("message");
    message.textContent = `Thanks for visiting, ${nameInput}! 🚀`;
}
