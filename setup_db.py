import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'database.sqlite')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create menu_items table
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category TEXT,
    imageUrl TEXT
)
''')

# Re-create orders table with customer details
cursor.execute('DROP TABLE IF EXISTS orders')
cursor.execute('''
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    item_id INTEGER,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    payment_method TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(item_id) REFERENCES menu_items(id)
)
''')

# Seed initial data
cursor.execute('SELECT COUNT(*) FROM menu_items')
count = cursor.fetchone()[0]

if count == 0:
    print("Seeding initial data...")
    items = [
        ("Classic Margherita", "Wood-fired perfection with fresh basil", 18.00, "Italian", "https://lh3.googleusercontent.com/aida-public/AB6AXuCfsk2mnpBiA3C8HASnvyrolGU7C-X5WIYWF5nlZMUaes3eEsSaTSiKsTXi6BPgU-CbLokdvwA-pAjjEN9UJ9wSMEYmTHAMEH2KSJEZSo1aKhHpz9EvLQRcPQbj1xKCBBzlLsvCaoqeNs7SEdrksrukMB03wf1fNUyqoWBkRBVsefDTG7-p6x1wbtjFmc5ftnI8S3GbScIKp6vOqrMlhapqZT5yLOJnR0zsWs8XP4qAhZSJgXhldxem"),
        ("Penne Arrabbiata", "Spicy tomato sauce, grated parmesan cheese, fresh parsley", 16.00, "Italian", "https://lh3.googleusercontent.com/aida-public/AB6AXuCwqcNvlkVUXy1vuZPp_5eppy0hODSDg_bxKKG0NluoC29I8OYYHci881JzwctdActRu0NmMhA_R4XL2ZxkCWZe7qAJyjeR9pg3Gs1Bv4ZtJMirbDD2LeSEZ48tt_0YBZ8_CN5jYNHzS7MTj3exl0MS9iEUx6bV0RgboE6HJB9hJc5BwcGnLTS1s0G1YgSDXeQQ4_FrmeiGoO_MYwf7gD6CzaHEASXWPHCLXPd-FT8QdI_lmQeFBLao"),
        ("Butter Chicken", "Creamy, vibrant orange-red curry garnished with fresh cream", 20.00, "Indian", "https://lh3.googleusercontent.com/aida-public/AB6AXuDoz3-vArxTlbptsJQJdgQ5aQLHXSNIwoq0NbSYgcLM9zUO2NYQClT3jxK4v9psjVT_QzJANbeVmKaZOWaeUVEXJCxFYlIfila2mVM2qN_V9Sq_dlT3nY31DYTRXslPIQKDWOkhF-MQreo_gPZ8uDr3cyj3RhA3hS1INrgWADLtPHliLmHIOQRbBzjWawmcevGx7Erku-IF-1c_Y2qNiAqXbhO8lAXUERbuGloaeEptvgVzuSzJFgK_"),
        ("Mixed Grill Platter", "Assortment of classic tandoori specials", 32.00, "Tandoori", "https://lh3.googleusercontent.com/aida-public/AB6AXuCpd_7jQdEh68-v4d0XIAccNzEfEVX0jZmm_KFXpi-ExunlVRDVPRcVofivGmzx4pp2vocO7aa42Alnu1XubsneICoA0uQ9Kx50Pm6kHL1tht1biK7q-bm8l-sQ18Mx0ryBj-nbo-Szut1eS9h2pixPFz4KUhgWV30SaQZGzZ14U0NPHj4Ma_7J1Ak5Wng0PQHz4VkwEYuD8wZ6_l4Z5NUYruIJe2y-hsbqTN7pKFElq_U-t-4Oowuw")
    ]
    cursor.executemany('INSERT INTO menu_items (name, description, price, category, imageUrl) VALUES (?, ?, ?, ?, ?)', items)
    conn.commit()
    print("Seeding complete.")
else:
    print("Database already seeded.")

conn.close()
print("Database setup successfully!")
