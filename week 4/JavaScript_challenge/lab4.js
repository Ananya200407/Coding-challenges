// Lab 4: Payment Mode Charges

let totalWithTax = Number(prompt("Enter Total Amount"));
let paymentMode = prompt("Enter Payment Mode (Card/UPI/Cash)");

let charges = 0;

if (paymentMode === "Card" && totalWithTax < 1000) {
    charges = totalWithTax * 0.025;
} else {
    charges = totalWithTax * 0.01;
}

let finalAmount = totalWithTax + charges;

console.log("Charges:", charges);
console.log("Final Amount:", finalAmount);
