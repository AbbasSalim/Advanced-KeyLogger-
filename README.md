🛡️ Advanced Keylogging Awareness Lab
A Python Project Demonstrating How Attackers Capture Keystrokes, Screenshots & Webcam Images — Built for Ethical Cybersecurity Education Only
⚠️ Ethical Disclaimer

This project is created strictly for cybersecurity education and awareness.
It is designed to help students, analysts, and defenders understand:

How keylogging works

How attackers chain simple tools into powerful data-exfiltration pipelines

How to better detect, prevent, and respond to these behaviors

🔐 Do not deploy or run this on any device you do not own or have explicit written permission to test.
This repository exists to raise awareness, not enable misuse.

🚀 Project Overview

This Python lab simulates a realistic attack behavior by:

✔️ Logging keystrokes through keyboard hooks
✔️ Capturing screenshots of the victim machine
✔️ Taking webcam photos
✔️ Sending all captured data to a Discord webhook
✔️ Cleaning up artifacts after each cycle
✔️ Running in timed intervals for continuous exfiltration

The goal is to demonstrate the seriousness of keylogging-based attacks and help users visualize what can happen once a malicious script is executed on a system.

This is an awareness tool, not malware.

🎯 Why This Project Matters

Cyber attackers often rely on:

Keyloggers to steal passwords and messages

Screenshot capture tools to gather sensitive on-screen data

Webcam capture for privacy invasion & extortion

Webhook-based exfiltration to hide in normal HTTPS traffic

By recreating this attack chain in a controlled environment, we can study:

🔍 Indicators of compromise
🛡️ How to detect malicious behavior
🚨 How easily data can be captured once a system is compromised
🏴‍☠️ How attackers structure their exfiltration logic

This project turns a “scary attack” into a learning experience.

🧠 Skills Demonstrated

This project showcases proficiency in:

🐍 Python

Real-time event listening

File handling

Screenshot & webcam capture

Network requests

Loop scheduling & script automation

🔐 Offensive Security Concepts (Ethical Use)

Keystroke interception

Data collection & exfiltration

Understanding attacker TTPs (Tactics, Techniques, Procedures)

🛡️ Defensive Security Concepts

Recognizing malicious persistence

Monitoring suspicious outbound traffic

Understanding forensic artifacts

🗂️ Tooling & Libraries

pynput

pyautogui

opencv-python (cv2)

requests

os, shutil, time

🏗️ Project Structure
project/
│
├── main.py                # Core script (keylogging, screenshots, webcam, exfiltration)
├── lab_outputs/           # Temporary storage for captured data
└── README.md              # Project documentation

⚙️ Features Breakdown
1️⃣ Keystroke Logging

Captures all keyboard input using pynput and writes to a local log file before exfiltration.

2️⃣ Screenshot Capture

Takes a full-screen screenshot every cycle via pyautogui.

3️⃣ Webcam Image Capture

Snaps images from the default webcam using OpenCV (cv2).

4️⃣ Discord Webhook Exfiltration

Sends keystrokes and media files to a designated webhook.

5️⃣ Automatic Cleanup

Deletes local artifacts after successful transmission to avoid buildup.

6️⃣ Automated Looping

Runs continuously in timed intervals (default: every 30 seconds for demo purposes).

📦 Installation

⚠️ Run only in a controlled environment.

1. Clone the repository:
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

2. Install required Python packages:
pip install pynput pyautogui opencv-python requests

3. Replace the webhook URL in main.py:
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

4. Run the script:
python main.py

🎥 Demo Screenshot (Replace with your own)

You can insert an example image of the captured screenshot or terminal output here.

🔍 What You’ll Learn

How keyloggers operate behind the scenes

How webcam and screen capture tools work programmatically

How attackers exfiltrate data using legitimate services (Discord, Slack, Telegram, etc.)

How defenders can build signatures, detections, and behavioral rules to stop these attacks

🛡️ Future Improvements

Ideas for expanding the project:

Add encrypted payload delivery

Add timestamping & metadata

Build a keylogger detection tool as a complementary project

Add network traffic monitoring logs

Integrate with SIEM simulation

Add a “defender mode” to show detection strategies

🤝 Contributing

If you want to improve this educational project or collaborate on cybersecurity awareness tools, feel free to open an issue or submit a pull request.

⭐ Support the Project

If this helped you understand cybersecurity threats better:

👉 Star the repo
👉 Share it with students / interns learning cybersecurity
👉 Connect with me on LinkedIn

🏁 Final Note

This project exists to educate, inform, and empower users to protect themselves.

Understanding threats is the first step to defending against them.

Stay curious. Stay ethical. Stay secure. 🔐
