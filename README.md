# Taltulator - The Prank Calculator

A fun calculator that gives intentionally wrong answers, perfect for pranking your friends!

## Features
- Basic arithmetic operations (+, -, *, /)
- Power (^) and Square Root (√) functions
- Wrong answers with a funny message
- Web version available
- Desktop GUI version included

## Desktop Version
Run the desktop version using:
```bash
python calculator.py
```

## Web Version
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the web server:
```bash
python app.py
```

3. Open `http://localhost:5000` in your browser

## Share with Friends
Use ngrok to share your local server:
```bash
python start_tunnel.py
```

## How the Prank Works
The calculator:
1. Calculates the correct answer
2. Adds a random number to make it wrong
3. Displays a funny message

## Requirements
- Python 3.6+
- Flask (for web version)
- tkinter (usually comes with Python)

## Note
This is a prank application. Use it responsibly and for entertainment purposes only!
