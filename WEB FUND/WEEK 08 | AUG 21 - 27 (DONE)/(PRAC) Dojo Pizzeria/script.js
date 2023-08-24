// PIZZA

function pizzaOven(crust, sauce, cheese, toppings) {
    let pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;
}

let pizza01 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni","sausage"])
console.log(pizza01);
let pizza02 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"])
console.log(pizza02);
let pizza03 = pizzaOven("thin crust", "bbq", "provolone", ["chicken","onion"])
console.log(pizza03);
let pizza04 = pizzaOven("flat bread", "pesto", "ricotta", ["basil","tomatoes"])
console.log(pizza04);

