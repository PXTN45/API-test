import requests

def test_delete_booking():
    url = "http://localhost:3000/"  # URL ของ API ที่ต้องการทดสอบ

    # กรณีที่ 1: ทดสอบการลบ booking ที่มีอยู่
    booking_id = "66fce447492081d7e37cd312"  # ใส่ ID ของ booking ที่ต้องการลบ
    response = requests.delete(f"{url}/deleteBooking/{booking_id}")

    if response.status_code == 200:
        response_data = response.json()
        if response_data["message"] == "Booking deleted successfully!":
            print("Test 1 passed: Booking deleted successfully.")
            # ทำอย่างอื่นที่ต้องการเมื่อการลบสำเร็จ
        else:
            print(f"Unexpected message: {response_data['message']}")
    elif response.status_code == 404:
        print("Test 1 failed: Booking not found as expected.")
        # ทำอย่างอื่นที่ต้องการเมื่อไม่พบ booking
    else:
        print(f"Unexpected status code: {response.status_code}")

    # กรณีที่ 2: ทดสอบการลบ booking ที่ไม่มีอยู่ (ใช้ ID ไม่ถูกต้อง)
    invalid_booking_id = "invalid_booking_id"  # ใส่ ID ที่ไม่ถูกต้อง
    response = requests.delete(f"{url}/deleteBooking/{invalid_booking_id}")

    if response.status_code == 404:
        response_data = response.json()
        if response_data["message"] == "Booking Not Found":
            print("Test 2 passed: Booking not found as expected.")
            # ทำอย่างอื่นที่ต้องการเมื่อไม่พบ booking
        else:
            print(f"Unexpected message: {response_data['message']}")
    else:
        print(f"Test 2 failed: Expected status code 404, but got {response.status_code}")

if __name__ == "__main__":
    test_delete_booking()
