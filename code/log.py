import random
import time
from datetime import datetime

def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_datetime():
    timestamp = time.time() - random.randint(0, 2592000)  
    return datetime.fromtimestamp(timestamp).strftime('%d/%b/%Y:%H:%M:%S +0200')

def generate_request():
    methods = ["GET", "POST", "DELETE", "PUT", "HEAD", "OPTIONS"]
    resources = ["/index.html", "/about.html", "/contact.html", "/products.html", "/api/data", "/login", "/logout"]
    http_version = "HTTP/1.1"
    return f'"{random.choice(methods)} {random.choice(resources)} {http_version}"'

def generate_status():
    return random.choice([200, 404, 500, 301, 400, 302])

def generate_bytes():
    return random.randint(20, 5000)

def generate_referrer():
    referrers = ["-", "http://www.example.com", "http://www.anotherdomain.com", "https://www.somedomain.org"]
    return f'"{random.choice(referrers)}"'

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Yandex/23.2 (beta) Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
    ]
    return f'"{random.choice(user_agents)}"'

def generate_log_entry():
    return f'{generate_ip()} - - [{generate_datetime()}] {generate_request()} {generate_status()} {generate_bytes()} {generate_referrer()} {generate_user_agent()}'

number_of_logs = 5000

with open("apache_logs.txt", "w") as file:
    for _ in range(number_of_logs):
        file.write(generate_log_entry() + "\n")

print("Log dosyası başarıyla oluşturuldu.")
