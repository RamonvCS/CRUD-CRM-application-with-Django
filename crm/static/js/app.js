// crm/static/js/app.js
console.log('app.js is loaded');

// Function to hide the message after 2 seconds
setTimeout(function() {
    var message = document.getElementById("message");
    if (message) {
        message.style.display = "none";
    }
}, 2000); // 2000 milliseconds = 2 seconds
