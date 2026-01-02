// Lab 2: Membership Discount

let grandTotal = Number(prompt("Enter Grand Total"));
let membershipType = prompt("Enter Membership (None/Silver/Gold/Platinum)");

let discountRate = 0;

if (membershipType === "Silver") discountRate = 0.05;
else if (membershipType === "Gold") discountRate = 0.10;
else if (membershipType === "Platinum") discountRate = 0.15;

let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

console.log("Discount Amount:", discountAmount);
console.log("Discounted Total:", discountedTotal);
