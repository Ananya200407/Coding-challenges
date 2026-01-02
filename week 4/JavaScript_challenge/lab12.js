// Lab 12: Inventory Lookup using Promises (User Input)

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
            }
            else if (quantity <= 0) {
                reject("Quantity must be greater than zero");
            }
            else if (inventory[itemCode] < quantity) {
                reject("Insufficient stock. Available: " + inventory[itemCode]);
            }
            else {
                resolve("Stock available for " + itemCode);
            }

        }, 1000);
    });
}

let itemCode = prompt("Enter Item Code (ITM101 / ITM102 / ITM103)");
let quantity = Number(prompt("Enter Quantity"));

itemCode = itemCode.trim().toUpperCase();

checkInventory(itemCode, quantity)
    .then(message => {
        console.log(message);
        console.log("Proceed with purchase");
    })
    .catch(error => {
        console.error("Error:", error);
        alert(error);
    })
    .finally(() => {
        console.log("Inventory check completed");
    });
