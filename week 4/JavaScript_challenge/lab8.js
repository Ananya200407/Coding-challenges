// Lab 8: Email Validation

function validateEmail(email) {
    const regex = /^[a-z0-9._%+-]+@gmail\.com$/;
    return regex.test(email);
}

let email;
do {
    email = prompt("Enter gmail.com email").trim().toLowerCase();
    if (!validateEmail(email)) {
        alert("Invalid email");
    }
} while (!validateEmail(email));

console.log("Valid Email:", email);
