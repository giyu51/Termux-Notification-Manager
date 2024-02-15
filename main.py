import subprocess
import json
import argparse
import wave
import datetime
import time


def get_wav_duration(sound_file_path: str) -> int:
    """Get the duration of a WAV sound file in seconds."""
    with wave.open(sound_file_path, "rb") as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration_seconds = frames / float(rate)
        print("Sound duration:", duration_seconds, "seconds")
        return int(duration_seconds)


def notify(sound_file: str) -> None:
    """Send a notification and play a sound."""
    print(
        f"Notification №{notification_count}: ",
        datetime.datetime.now().strftime("%m.%D - %H:%M:%S"),
    )
    subprocess.run(["termux-volume", "music", "15"])
    subprocess.run(["termux-media-player", "play", sound_file])
    time.sleep(get_wav_duration(sound_file))
    subprocess.run(["termux-volume", "music", "0"])

    notification_count += 1


def check_message(
    data_obj: dict, package_name: str, match_key: str, match_value: str
) -> None:
    """Check if there are any new notifications that match the specified criteria."""
    for obj in data_obj:
        if obj.get("packageName") == package_name:
            sender = obj.get(match_key)
            print(sender)
            if sender == match_value:
                notify()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notifier for Termux")
    parser.add_argument("search_value", help="Value to search for/ Contact Name")
    parser.add_argument("sound_file", help="Path to sound file")
    parser.add_argument(
        "--package_name",
        default="com.whatsapp",
        help="Name of the package. Default is `com.whatsapp`",
    )
    parser.add_argument(
        "--search_key", default="title", help="Search key. Default is `title`"
    )
    parser.add_argument(
        "--check_interval",
        type=int,
        default=5,
        help="Amount of time in seconds. Default is 5 seconds",
    )
    args = parser.parse_args()

    cmd = "termux-notification-list"
    package_name = args.package_name
    match_value = args.search_value
    match_key = args.search_key
    check_interval = args.check_interval
    sound_file = args.sound_file
    notification_count = 1

    print(
        "\nNotification Check started at ",
        datetime.datetime.now().strftime("%m.%D - %H:%M:%S"),
        "-" * 16,
        "\n",
    )

    while True:
        raw_output = subprocess.getoutput(cmd)
        json_output = json.loads(raw_output)
        check_message(json_output, package_name, match_key, match_value)
        time.sleep(check_interval)
