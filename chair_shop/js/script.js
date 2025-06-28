const cartIcon = document.querySelector(".cart-icon");
const body = document.querySelector("body");
const closeCart = document.querySelector(".close-cart");
const cart = document.querySelector("section.cart");

let Data = [];
// Function to toggle the cart visibility
const toggleCart = () => {
  body.classList.toggle("cart-active");
  addEventListener("click", (e) => {
    if (
      !cart.contains(e.target) &&
      !cartIcon.contains(e.target) &&
      body.classList.contains("cart-active")
    ) {
      body.classList.toggle("cart-active");
    }
  });
};

cartIcon.addEventListener("click", (e) => toggleCart());
closeCart.addEventListener("click", (e) => toggleCart());

const getData = async () => {
  let url = "../products.json";
  try {
    let response = await fetch("../products.json");
    if (!response.ok) {
      throw new Error("Error IN data Fetch 30");
    }
    const json = await response.json();
    json = Data;
    console.log(Data);
  } catch {
    console.log("a7a");
  }
};

getData();
console.log(Data);
