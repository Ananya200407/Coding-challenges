// Lab 5: Invoice Generation

let invoiceNumber = "INV-" + Math.floor(Math.random() * 100000);
let invoiceDate = new Date();

console.log("Invoice Number:", invoiceNumber);
console.log("Invoice Date:", invoiceDate.toLocaleString());
console.log("Invoice Generated Successfully");
