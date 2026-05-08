import network
import socket
from machine import Pin
import dht
import time

# ---------------- LED ----------------
led = Pin(2, Pin.OUT)

# ---------------- DHT SENSOR ----------------
sensor = dht.DHT11(Pin(4))   # change to DHT22 if needed

# ---------------- WIFI ----------------
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print("Connecting to WiFi...")
wifi.connect("WIFI_NAME", "wIFI_Pass")

while not wifi.isconnected():
    pass

ip = wifi.ifconfig()[0]

print("Connected!")
print("IP:", ip)

# ---------------- SERVER ----------------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(5)

print("Server running")
print("Open: http://{}".format(ip))

# ---------------- LOOP ----------------
while True:
    client, addr = server.accept()
    print("Client:", addr)

    request = client.recv(1024).decode()

    # LED control
    if "/on" in request:
        led.value(1)
        print("LED ON")

    if "/off" in request:
        led.value(0)
        print("LED OFF")

    # ---------------- READ TEMP ----------------
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temp:", temp, "Hum:", hum)
    except:
        temp = "Error"
        hum = "Error"
        print("Sensor read failed")

    # ---------------- HTML ----------------
    response = """HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

<!DOCTYPE html>
<html>
<head>
<title>ESP32 Temp Dashboard</title>

<style>
body{
    margin:0;
    background:#0f172a;
    font-family:Arial;
    color:white;
    text-align:center;
}

.card{
    width:320px;
    margin:80px auto;
    padding:25px;
    background:#111827;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.6);
}

h1{
    font-size:24px;
}

.data{
    font-size:22px;
    margin:15px 0;
}

button{
    width:200px;
    padding:12px;
    margin:10px;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.on{background:#22c55e;color:white;}
.off{background:#ef4444;color:white;}
</style>

</head>

<body>

<div class="card">
<h1>🌡 ESP32 Temperature Monitor</h1>

<div class="data">Temperature: """ + str(temp) + """ °C</div>
<div class="data">Humidity: """ + str(hum) + """ %</div>

<a href="/on"><button class="on">LED ON</button></a>
<br>
<a href="/off"><button class="off">LED OFF</button></a>

</div>

</body>
</html>
"""

    client.send(response.encode())
    client.close()

