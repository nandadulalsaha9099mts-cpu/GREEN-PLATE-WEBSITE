import http.server
import socketserver
import sqlite3
import json
import os
import urllib.parse

PORT = 8000
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/menu':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            conn = get_db_connection()
            items = conn.execute('SELECT * FROM menu_items').fetchall()
            conn.close()
            
            response = [dict(ix) for ix in items]
            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/api/orders':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            conn = get_db_connection()
            items = conn.execute('SELECT * FROM orders ORDER BY timestamp DESC').fetchall()
            conn.close()
            
            response = [dict(ix) for ix in items]
            self.wfile.write(json.dumps(response).encode())
        else:
            # Serve static files
            if self.path == '/':
                self.path = '/code.html'
            return super().do_GET()

    def do_POST(self):
        if self.path == '/api/menu':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO menu_items (name, description, price, category, imageUrl) VALUES (?, ?, ?, ?, ?)',
                         (data['name'], data.get('description', ''), float(data['price']), data.get('category', ''), data.get('imageUrl', '')))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"id": new_id, "status": "success"}).encode())
        elif self.path == '/api/orders':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO orders (customer_name, customer_email, customer_phone, item_id, item_name, quantity, total_price, payment_method) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                         (data.get('customer_name'), data.get('customer_email'), data.get('customer_phone'), data.get('item_id'), data['item_name'], int(data['quantity']), float(data['total_price']), data['payment_method']))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"id": new_id, "status": "success"}).encode())
        else:
            self.send_error(404, "Not Found")

    def do_DELETE(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path.startswith('/api/menu/'):
            item_id = parsed_path.path.split('/')[-1]
            
            conn = get_db_connection()
            conn.execute('DELETE FROM menu_items WHERE id = ?', (item_id,))
            conn.commit()
            conn.close()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "deleted"}).encode())
        else:
            self.send_error(404, "Not Found")

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
