# 🌡️ ESP32 DHT11 Temperature & Humidity Monitor

This project is an IoT-based **temperature and humidity monitoring system** using an **ESP32** and **DHT11 sensor**. The data is read in real-time using **MicroPython (Thonny IDE)** and can be used for basic environmental monitoring or extended for cloud/IoT dashboards.

---

## 📌 Features
- Reads real-time temperature and humidity
- Uses DHT11 sensor with ESP32
- Built using MicroPython (Thonny IDE)
- Simple and beginner-friendly IoT project
- Can be extended to web dashboard or cloud storage

---

## 🧰 Hardware Required
- ESP32 Development Board
- DHT11 Temperature & Humidity Sensor
- Breadboard
- Jumper wires
- USB cable for ESP32

---

## 🔌 Circuit Connection (DHT11 → ESP32)

| DHT11 Pin | ESP32 Pin |
|-----------|----------|
| VCC       | 3.3V     |
| GND       | GND      |
| DATA      | GPIO (e.g., 4) |

> You can change GPIO pin in code if required.

---

## 💻 Software Used
- Thonny IDE
- MicroPython firmware for ESP32

---

## 🚀 How It Works
1. ESP32 connects to DHT11 sensor via GPIO pin  
2. Sensor collects temperature and humidity data  
3. MicroPython code reads sensor values  
4. Data is printed in Thonny console in real-time  

---

## 📟 Example Output
