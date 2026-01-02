// Lab 7: LocalStorage

let cart = [{ item: "Book", price: 200 }];

localStorage.setItem("cartItems", JSON.stringify(cart));

let savedCart = JSON.parse(localStorage.getItem("cartItems"));
console.log("Retrieved Cart:", savedCart);
