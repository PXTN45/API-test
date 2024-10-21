import requests

url = "http://localhost:3000/user/login"  # URL ของ API login
login_data = {
    "email": "sofekung@gmail.com",  # ใส่อีเมลของคุณ
    "password": "Sofe_SE007", # ใส่รหัสผ่านของคุณ
    "role": "business" 
}

# ส่ง POST request ไปที่ API login
response = requests.post(url, json=login_data)

# ตรวจสอบว่าการ login สำเร็จหรือไม่
if response.status_code == 200:
    data = response.json()  # แปลง response เป็น JSON
    print("Login successful!")
    print("Response data:", data)  # แสดงข้อมูลที่ตอบกลับ เช่น token
else:
    print(f"Login failed with status code: {response.status_code}")
    print("Response:", response.text)
