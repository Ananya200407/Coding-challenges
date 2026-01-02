// Lab 11: Async / Await

async function processPayment() {
    console.log("Processing Payment...");
    await new Promise(resolve => setTimeout(resolve, 2000));
    console.log("Payment Successful");
}

processPayment();
