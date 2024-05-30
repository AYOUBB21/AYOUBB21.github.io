import csv
import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact(name, phone, email):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    messagebox.showinfo("Contact added", f"Contact {name} added successfully.")
    clear_entries()

# Function to view all contacts
def view_contacts():
    contacts_list.delete(0, tk.END)
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts_list.insert(tk.END, row)

# Function to search for a contact
def search_contact():
    name = entry_search_name.get()
    contacts_list.delete(0, tk.END)
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                contacts_list.insert(tk.END, row)
                return
    messagebox.showinfo("Not found", "Contact not found.")

# Function to update a contact
def update_contact():
    name = entry_name.get()
    new_phone = entry_phone.get()
    new_email = entry_email.get()
    rows = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                rows.append([name, new_phone, new_email])
            else:
                rows.append(row)
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    messagebox.showinfo("Contact updated", f"Contact {name} updated successfully.")
    clear_entries()
    view_contacts()

# Function to delete a contact
def delete_contact():
    name = entry_search_name.get()
    rows = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                rows.append(row)
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    messagebox.showinfo("Contact deleted", f"Contact {name} deleted successfully.")
    view_contacts()

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Set up the main Tkinter window
root = tk.Tk()
root.title("Contact Management System")

# Create and place labels, entry fields, and buttons
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Button(root, text="Add Contact", command=lambda: add_contact(entry_name.get(), entry_phone.get(), entry_email.get())).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Search by Name:").grid(row=4, column=0)
entry_search_name = tk.Entry(root)
entry_search_name.grid(row=4, column=1)

tk.Button(root, text="Search", command=search_contact).grid(row=5, column=0)
tk.Button(root, text="Update", command=update_contact).grid(row=5, column=1)
tk.Button(root, text="Delete", command=delete_contact).grid(row=6, column=0, columnspan=2)

tk.Button(root, text="View All Contacts", command=view_contacts).grid(row=7, column=0, columnspan=2)

contacts_list = tk.Listbox(root, width=50)
contacts_list.grid(row=8, column=0, columnspan=2)

# Run the Tkinter main loop
root.mainloop()
