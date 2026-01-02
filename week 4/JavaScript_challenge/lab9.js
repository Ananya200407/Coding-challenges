// Lab 9: Custom Error

class ValidationError extends Error {}

try {
    let quantity = Number(prompt("Enter Quantity"));
    if (quantity <= 0) {
        throw new ValidationError("Quantity must be greater than zero");
    }
    console.log("Valid Quantity:", quantity);
} catch (err) {
    console.error(err.message);
} finally {
    console.log("Validation Completed");
}
