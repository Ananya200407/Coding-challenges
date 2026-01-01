/* =========================
   Lab 9: Custom Error Class
   ========================= */
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
}

/* =========================
   Utility Functions
   ========================= */
function generateInvoiceNumber() {
    return "INV-" + Math.floor(Math.random() * 1000000);
}

function validateEmail(email) {
    const regex = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;
    return regex.test(email);
}

/* =========================
   Lab 12: Inventory Lookup using Promises
   ========================= */
const inventory = {
    ITM101: 10,
    ITM102: 20,
    ITM103: 15
};

function checkInventory(itemCode, quantity) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (!inventory[itemCode]) {
                reject("Item not found in inventory");
            } else if (inventory[itemCode] < quantity) {
                reject("Insufficient stock for item " + itemCode);
            } else {
                resolve("Stock available");
            }
        }, 500);
    });
}

/* =========================
   Lab 10: Membership Discount using Closures
   ========================= */
function getDiscountFunction(type) {
    let rate = 0;
    if (type === "Silver") rate = 0.05;
    if (type === "Gold") rate = 0.10;
    if (type === "Platinum") rate = 0.15;

    return function (amount) {
        return amount * rate;
    };
}

/* =========================
   Lab 11: Async Payment Processing
   ========================= */
async function processPayment(paymentMode) {
    console.log("Processing payment...");
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Payment Successful via " + paymentMode);
        }, 2000);
    });
}

/* =========================
   Lab 1: Add Items to Cart
   ========================= */
let cart = [];
let grandTotal = 0;

try {
    // Lab 7: Load previous cart
    let savedCart = localStorage.getItem("cartItems");
    if (savedCart) {
        let resume = prompt("Previous cart found. Resume? (yes/no)");
        if (resume.toLowerCase() === "yes") {
            cart = JSON.parse(savedCart);
            cart.forEach(item => grandTotal += item.totalPrice);
        }
    }

    let addMore = "yes";

    while (addMore.toLowerCase() === "yes") {
        let itemCode = prompt("Enter Item Code (ITM101/ITM102/ITM103)");
        let description = prompt("Enter Item Description");
        let quantity = Number(prompt("Enter Quantity"));
        let pricePerUnit = Number(prompt("Enter Price per Unit"));

        if (quantity <= 0 || pricePerUnit <= 0) {
            throw new ValidationError("Quantity and Price must be greater than zero");
        }

        // Inventory check (Lab 12)
        await checkInventory(itemCode, quantity);

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

    if (cart.length === 0) {
        throw new ValidationError("Cart cannot be empty");
    }

} catch (err) {
    console.error(err.message);
    alert(err.message);
} finally {
    console.log("Cart processing completed");
}

/* =========================
   Lab 2: Apply Membership Discount
   ========================= */
let membershipType = "None";
let discountAmount = 0;
let discountedTotal = grandTotal;

let isMember = prompt("Are you a member? (yes/no)");
if (isMember.toLowerCase() === "yes") {
    membershipType = prompt("Enter Membership Type (Silver/Gold/Platinum)");
    let discountFn = getDiscountFunction(membershipType);
    discountAmount = discountFn(grandTotal);
    discountedTotal -= discountAmount;
}

/* =========================
   Lab 3: GST & Platform Fee
   ========================= */
const gstRate = 0.18;
const platformFeeRate = 0.002;

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;

let totalWithTax = discountedTotal + gstAmount + platformFee;

/* =========================
   Lab 4: Payment Mode Charges
   ========================= */
let paymentMode = prompt("Enter Payment Mode (Card/UPI/Cash)");
let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "Card" && totalWithTax < 1000) {
    surcharge = totalWithTax * 0.025;
} else {
    convenienceFee = totalWithTax * 0.01;
}

let finalTotalBeforeInvoice = totalWithTax + surcharge + convenienceFee;

/* =========================
   Lab 11: Async Payment Confirmation
   ========================= */
let paymentStatus = await processPayment(paymentMode);
console.log(paymentStatus);

/* =========================
   Lab 5: Generate Final Invoice
   ========================= */
let invoiceNumber = generateInvoiceNumber();
let invoiceDate = new Date();

let invoiceData = {
    invoiceNumber,
    invoiceDate,
    cart,
    grandTotal,
    discountAmount,
    gstAmount,
    platformFee,
    surcharge,
    convenienceFee,
    finalAmount: finalTotalBeforeInvoice
};

console.log("========== INVOICE ==========");
console.log("Invoice No:", invoiceNumber);
console.log("Date:", invoiceDate.toLocaleString());
console.table(cart);
console.log("Subtotal:", grandTotal);
console.log("Discount:", discountAmount);
console.log("GST:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Payment Charges:", surcharge + convenienceFee);
console.log("Final Payable:", finalTotalBeforeInvoice);
console.log("Payment Successful");
console.log("Invoice Generated");

/* =========================
   Lab 6 & Lab 8: Email Validation & Simulation
   ========================= */
let email;
do {
    email = prompt("Enter your email (@karunya.edu)");
    if (!validateEmail(email)) {
        alert("Invalid email format");
    }
} while (!validateEmail(email));

console.log("Invoice sent to", email);
console.log("Invoice JSON:", JSON.stringify(invoiceData, null, 2));

/* =========================
   Lab 7: Save Cart & Invoice to LocalStorage
   ========================= */
localStorage.setItem("cartItems", JSON.stringify(cart));
localStorage.setItem("invoiceData", JSON.stringify(invoiceData));
localStorage.setItem("email", email);
localStorage.setItem("timestamp", new Date().toISOString());

/* =========================
   Lab 13: Callback after Billing
   ========================= */
function completeBilling(callbackFn) {
    callbackFn(invoiceData);
}

completeBilling(function (data) {
    console.log("Thank you for shopping at Karazon.com!");
    console.log("Invoice Reference:", data.invoiceNumber);
});
