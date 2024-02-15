# 📲 Termux Notification Manager

## 🚀 Introduction:

This project was inspired by the need to effectively manage and prioritize notifications on my Android device. With numerous notifications from various apps and contacts, muting the sound mode became a necessity to maintain focus. However, there were instances where immediate responses to important messages, such as those from managers, were essential. To address this challenge, I developed a notification manager tailored for Termux. This Python-based solution enables users to customize criteria for triggering alerts based on sender names or message content. By playing designated sound files, the script ensures prompt notification of critical messages while maintaining a muted sound mode for non-urgent notifications.

## 💡 Usage:

### Prerequisites:

- [Termux](https://termux.com/) installed on your Android device.
- Python installed within Termux (`pkg install python`).
- `mutagen` Python library (`pip install mutagen`)

### Installation:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your_username/termux-notification-manager.git
   ```
2. Move into the project directory:
   ```bash
   cd termux-notification-manager
   ```
3. Move your desired sound file (in MP3 format) into the project directory.

### Configuration:

1. Open the `main.py` file in a text editor.
2. Customize the command-line arguments in the `argparse.ArgumentParser` according to your preferences:
   - `-search_value`: Value to search for/ Contact Name (e.g., manager's name).
   - `-sound_file`: Name of the sound file you moved into the directory.
   - `--package_name`: Name of the package for the app you want to monitor (default: `com.whatsapp`).
   - `--search_key`: Search key for matching notifications (default: `title`).
   - `--check_interval`: Amount of time in seconds to check for notifications (default: `5` seconds).

### Running the Script:

1. Ensure your Android device is unlocked and Termux is open.
2. Navigate to the project directory within Termux:
   ```bash
   cd /path/to/termux-notification-manager
   ```
3. Run the `main.py` script with the desired command-line arguments:
   ```bash
   python main.py -search_value "Manager Name" -sound_file "soundfile.mp3"
   ```
   Replace `"Manager Name"` with the name of the contact whose messages you want to monitor, and `"soundfile.mp3"` with the name of your sound file.

---

### Running in the Background:

After configuring and running the script, you can leave it running in the background even when your phone is locked. Termux continues to execute scripts in the background, ensuring that you receive notifications and alerts as needed.

Additionally, you can hide the visibility of notification content on the lock screen, and the script will still work seamlessly.

---
