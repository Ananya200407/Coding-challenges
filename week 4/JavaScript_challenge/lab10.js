// Lab 10: Closures for Membership Discount (User Input)

function getDiscountFunction(membershipType) {
    let rate = 0;

    if (membershipType === "Silver") {
        rate = 0.05;
    } else if (membershipType === "Gold") {
        rate = 0.10;
    } else if (membershipType === "Platinum") {
        rate = 0.15;
    }

   
    return function (amount) {
        return amount * rate;
    };
}


let amount = Number(prompt("Enter purchase amount"));
let membershipType = prompt("Enter membership type (Silver/Gold/Platinum)");

membershipType = membershipType.trim();
 
let discountCalculator = getDiscountFunction(membershipType);

let discount = discountCalculator(amount);

console.log("Purchase Amount:", amount);
console.log("Membership Type:", membershipType);
console.log("Discount Applied:", discount);
console.log("Final Amount:", amount - discount);
