Polski | [English](README.md)

# ROS2 Jetson – Czujnik odległości UART i wyświetlacz LCD (I2C)

Projekt przedstawia prosty system pomiarowy oparty o ROS2, działający na platformie NVIDIA Jetson Orin Nano.

System odczytuje dane z czujnika odległości przez UART, publikuje je w ROS2 oraz wyświetla wynik na wyświetlaczu LCD 16x2 poprzez I2C.

## Zastosowanie

Projekt symuluje podstawowy moduł czujnikowy systemu pokładowego BSP (drona).

## Funkcjonalności

- ROS2 Humble (węzły w Pythonie)
- Komunikacja UART z czujnikiem
- Parsowanie ramek 4-bajtowych: FF DH DL CS
- Weryfikacja sumy kontrolnej
- Komunikacja przez topic /lcd/text
- Wyświetlanie danych na LCD (I2C)
- Tryb heartbeat przy braku danych

## Sprzęt

- NVIDIA Jetson Orin Nano
- Czujnik odległości UART
- Konwerter USB–UART (np. TTL-232R)
- LCD 16x2 z interfejsem I2C
- Ubuntu 22.04
- ROS2 Humble

## Architektura systemu

```[Czujnik UART] -> [lcd_publisher] -> /lcd/text -> [lcd_subscriber] -> [LCD I2C]```

## Węzły ROS2

### lcd_publisher

Odczytuje dane z UART, parsuje ramki i publikuje odległość.

Format ramki:
```FF DH DL CS```

Obliczanie odległości:
```distance_mm = DH * 256 + DL```

Sprawdzenie sumy kontrolnej:
```CS == (FF + DH + DL) & 0xFF```

Przykład:
Distance:
122 mm

### lcd_subscriber

Subskrybuje topic /lcd/text i wyświetla dane na LCD 16x2 przez I2C.

## Instalacja
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/YOUR_USERNAME/ros2-jetson-uart-lcd-distance.git
cd ~/ros2_ws

pip install -r src/ros2-jetson-uart-lcd-distance/requirements.txt

colcon build
source install/setup.bash
```
## Uruchomienie

```bash
ros2 run py_pubsub lcd_publisher
ros2 run py_pubsub lcd_subscriber
```
Z własnym portem UART:
```bash
ros2 run py_pubsub lcd_publisher --ros-args -p port:=/dev/ttyUSB0
```
Z własnym adresem I2C:
```bash
ros2 run py_pubsub lcd_subscriber --ros-args -p i2c_address:=39
```

## Struktura repozytorium
```
ros2-jetson-uart-lcd-distance/
├── README.md
├── README_PL.md
├── requirements.txt
├── docs/
│   └── Pkum.pdf
├── images/
│   ├── setup_connected.jpg
│   └── setup_disconnected.jpg
└── src/
    └── py_pubsub/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── resource/
        │   └── py_pubsub
        └── py_pubsub/
            ├── __init__.py
            ├── lcd_publisher.py
            └── lcd_subscriber.py
```
## Autor

Bohdan Susulovskyi  
Wojskowa Akademia Techniczna  
Awionika
