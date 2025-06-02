# whatsappmessagebot

A Python automation bot that sends WhatsApp messages using Selenium WebDriver. This tool automates the process of logging into WhatsApp Web, searching for a contact, and sending messages, making it useful for bulk messaging, reminders, or personal automation.

## Features
- Automates WhatsApp Web login (requires QR code scan)
- Searches for contacts by name
- Sends messages loaded from `message.txt`
- Can be extended to send messages to multiple contacts
- Uses Selenium with Firefox (GeckoDriver)

## Requirements
- Python 3.7+
- Firefox browser
- GeckoDriver (must be in the project directory or in your PATH)
- Selenium (`pip install selenium`)

## Setup
1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd whatsappmessagebot
   ```
2. **Install dependencies**
   ```sh
   pip install selenium
   ```
3. **Download GeckoDriver**
   - Download from: https://github.com/mozilla/geckodriver/releases
   - Place the `geckodriver` binary in the project directory or add it to your PATH.

## Usage
1. **Prepare your contacts**
   - Edit the script to set the contact name(s) you want to send messages to.
   - Optionally, use a file like `numbers.txt` to store contact names or numbers.
2. **Write your message**
   - Place the message you want to send in the `message.txt` file. The bot will read the message from this file and send it to the selected contact(s).
3. **Run the bot**
   ```sh
   python main.py
   ```
4. **Scan the QR code**
   - When prompted, scan the QR code with your WhatsApp mobile app to log in.
5. **Automation in action**
   - The bot will search for the specified contact and send the message from `message.txt`.

## Customization
- Edit `main.py` to:
  - Change the contact name(s) to search for
  - Change how contacts are loaded (e.g., from `numbers.txt`)
  - Adjust message sending logic as needed

## Troubleshooting
- **Only first letter typed in search bar:**
  - The script has been updated to send characters one by one with a delay. If you still have issues, increase the delay or check for WhatsApp Web UI changes.
- **Element not found errors:**
  - WhatsApp Web updates may change element XPaths. Update the XPaths in `main.py` as needed.
- **GeckoDriver not found:**
  - Ensure `geckodriver` is in your project directory or PATH, and is executable.

## Disclaimer
This project is for educational and personal automation purposes only. Use responsibly and respect WhatsApp's terms of service.
