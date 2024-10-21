import requests
import json

def test_get_homestay_by_id():
    url = "http://localhost:3000/"  # URL ของ API ที่ต้องการทดสอบ
    id = "6708a981456143bb11dee460"

    try:
        # ส่งคำขอ GET request ไปยัง API
        response = requests.get(f"{url}/homestay/{id}")

        # ตรวจสอบว่า status code เป็น 200 หรือไม่
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        data = response.json()  # แปลง response เป็น JSON

        # ตรวจสอบว่าค่า homestay_name อยู่ใน response หรือไม่
        homestay_name = data.get("name_homeStay")
        assert homestay_name is not None, "Expected 'name_homeStay' in response but not found"
        
        print(f"Test passed. Homestay name: {homestay_name}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
    except AssertionError as e:
        print(f"Assertion error: {str(e)}")

if __name__ == "__main__":
    test_get_homestay_by_id()
