import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management System")
        self.menu_items = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Pasta": 7.99,
            "Salad": 4.99,
            "Soda": 1.99, 
            "Coffee": 2.49, 
            "Cold Coffee": 2.49,
            "Tea": 1.99,
            "Ice Cream": 3.99,
            "Fries": 2.99
        }
        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Restaurant Order Management System", font = ("Aerial", 20, "bold")
        ).grid(row=0, columnspan=3, pady=10, padx=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font = ("Aerial", 12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2, columnspan=3, pady=10, padx=10)
    def place_order(self):
        total_cost = 0
        order_details = "Order Details:\n"
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_details += f"{item}: {quantity} x ${price} = ${cost:.2f}\n"
        if total_cost > 0:
            order_details += f"\nTotal Cost: ${total_cost:.2f}"
            messagebox.showinfo("Order Placed!", order_details)
        else:
            messagebox.showinfo("No Items Ordered", "Please enter quantities for at least one item.")
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()