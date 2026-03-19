# Shopping Cart 🛒

A terminal-based Shopping Cart simulator built with Python that 
allows users to add items, view their cart and calculate total bill!

## Features
- Browse a shop menu with 5 items
- Add items to cart with quantity
- View all added items in cart
- Calculates total bill automatically
- Checks for empty cart at checkout
- Validates invalid quantities
- Option to quit anytime

## Shop Menu
| Item   | Price    |
|--------|----------|
| Apple  | Rs. 10   |
| Banana | Rs. 5    |
| Milk   | Rs. 50   |
| Bread  | Rs. 30   |
| Cheese | Rs. 100  |

## How to Run
1. Make sure Python is installed on your computer
2. Run the script:
   python shopping_cart.py
3. Choose an item from the menu (1-5)
4. Enter quantity
5. Keep adding items
6. Enter 6 to checkout
7. Enter 7 to quit

## Technologies Used
- Python 3
- No external libraries needed

## Example Output
-----Welcome to the shop-----
1. Apple  = Rs. 10
2. Banana = Rs. 5
3. Milk   = Rs. 50
4. Bread  = Rs. 30
5. Cheese = Rs. 100
6. Checkout
7. Quit
Enter your choice (1/2/3/4/5/6/7): 1
How many apples? 3
3 apples are added to the cart
Enter your choice (1/2/3/4/5/6/7): 3
How many Milks? 2
2 Milks are added to the cart
Enter your choice (1/2/3/4/5/6/7): 6
-----Your Cart-----
Apples x3 = Rs.30
Milk x2 = Rs.100
Your Total: 130
-----Thank you for shopping! Visit Again-----
