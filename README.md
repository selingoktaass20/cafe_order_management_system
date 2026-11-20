# Cafe Order Management System

An object-oriented Python console application designed to manage cafe operations, including product inventory, shopping cart validation, order processing, and daily revenue tracking.

## Features
- **Cafe Information:** Displays store name, city, and operating hours.
- **Inventory & Menu Display:** Lists available items with current prices and real-time stock counts.
- **Smart Cart Management:** Validates product availability, prevents negative quantities, and ensures combined cart quantities do not exceed available stock.
- **Order Processing:** Automatically deducts purchased quantities from stock, records unique sold items, calculates total revenue, and clears the cart.
- **Sales Reporting:** Tracks unique products sold during the day and displays total daily earnings.

## Concepts & Data Structures Used
- **Object-Oriented Programming (OOP):** Encapsulated state and behavior within the `Kafe` class.
- **Dictionaries:** Used for structured product inventory (`price`, `stock`) and cart items.
- **Lists:** Manages active shopping cart entries.
- **Sets:** Tracks unique sold products without duplicates.
- **Tuples:** Stores immutable cafe metadata (name, city, working hours).

## Sample Menu
```text
==========================
PYTHON KAFE
==========================
1- Kafe bilgilerini göster
2- Ürünleri göster
3- Sepete ürün ekle
4- Sepeti göster
5- Siparişi tamamla
6- Satılan ürünleri göster
7- Günlük kazancı göster
0- Programdan çık
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/selingoktaass20/cafe_order_management_system.git
   ```
2. Navigate to the project directory and run the script:
   ```bash
   cd cafe_order_management_system
   python cafe_management.py
   ```
