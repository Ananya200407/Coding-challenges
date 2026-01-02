// Lab 1: Add Items to Cart

let cart = [];
let grandTotal = 0;
let addMore = "yes";

while (addMore.toLowerCase() === "yes") {
    let itemCode = prompt("Enter Item Code");
    let description = prompt("Enter Item Description");
    let quantity = Number(prompt("Enter Quantity"));
    let pricePerUnit = Number(prompt("Enter Price per Unit"));

    let totalPrice = quantity * pricePerUnit;

    cart.push({
        itemCode,
        description,
        quantity,
        pricePerUnit,
        totalPrice
    });

    grandTotal += totalPrice;

    addMore = prompt("Add another item? (yes/no)");
}

console.table(cart);
console.log("Grand Total:", grandTotal);
