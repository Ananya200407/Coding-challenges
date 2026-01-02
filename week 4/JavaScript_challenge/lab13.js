// Lab 13: Callback

function completeBilling(callback) {
    console.log("Billing Complete");
    callback();
}

completeBilling(() => {
    console.log("Thank you for shopping!");
});
