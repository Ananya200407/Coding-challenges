// Lab 3: GST & Platform Fee

let discountedTotal = Number(prompt("Enter Discounted Total"));

const gstRate = 0.18;
const platformFeeRate = 0.002;

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;

let totalWithTax = discountedTotal + gstAmount + platformFee;

console.log("GST:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Total with Tax:", totalWithTax);
