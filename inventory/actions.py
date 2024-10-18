from db.database import create_connection

def add_product(product):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product.name, product.quantity))
    conn.commit()
    conn.close()

def view_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def update_product(product_id, new_quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
