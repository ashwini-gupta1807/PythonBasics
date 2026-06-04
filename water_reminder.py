#!/usr/bin/env python3
import sys
import os
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

def escape_applescript_string(s):
    """Escapes backslashes and double quotes for AppleScript."""
    return s.replace('\\', '\\\\').replace('"', '\\"')

def send_notification(title, message, sound="Glass"):
    """
    Sends a desktop notification. Supports macOS natively via AppleScript,
    with basic fallbacks for Linux and Windows.
    """
    system = platform.system().lower()
    if system == "darwin":
        # macOS notification using AppleScript
        title_esc = escape_applescript_string(title)
        msg_esc = escape_applescript_string(message)
        sound_esc = escape_applescript_string(sound)
        
        script = f'display notification "{msg_esc}" with title "{title_esc}" sound name "{sound_esc}"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            return True
        except subprocess.SubprocessError as e:
            print(f"Error sending macOS notification: {e}", file=sys.stderr)
            return False
    elif system == "linux":
        # Linux notification using notify-send
        try:
            subprocess.run(["notify-send", title, message], check=True)
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            print("Linux notify-send not found or failed. Printing to console.", file=sys.stderr)
            print(f"[{title}] {message}")
            return False
    elif system == "windows":
        # Windows notification using win10toast if available, else print
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=10, threaded=True)
            return True
        except ImportError:
            print("win10toast not installed. Printing to console.", file=sys.stderr)
            print(f"[{title}] {message}")
            return False
    else:
        # Fallback console notification
        print(f"[{title}] {message}")
        return True

def format_time(seconds):
    """Formats seconds into mm:ss format."""
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

def main():
    parser = argparse.ArgumentParser(
        description="Drink Water Reminder - Sends periodic notifications to remind you to stay hydrated."
    )
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=60.0,
        help="Reminder interval in minutes (default: 60.0)"
    )
    parser.add_argument(
        "-t", "--test",
        action="store_true",
        help="Send a test notification immediately and exit"
    )
    
    args = parser.parse_args()
    
    title = "💧 Drink Water Reminder"
    
    if args.test:
        print("Sending test notification...")
        success = send_notification(
            title,
            "Staying hydrated keeps you energized and healthy! 🥤",
            sound="Glass"
        )
        if success:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification.")
        sys.exit(0)
        
    interval_minutes = args.interval
    interval_seconds = int(interval_minutes * 60)
    
    if interval_seconds <= 0:
        print("Error: Interval must be greater than 0.", file=sys.stderr)
        sys.exit(1)
        
    print("=" * 60)
    print("💧 DRINK WATER REMINDER STARTED 💧")
    print(f"Interval: {interval_minutes} minutes ({interval_seconds} seconds)")
    print("Press Ctrl+C to stop the reminder.")
    print("=" * 60)
    
    # Send an initial notification to confirm it is running
    send_notification(title, f"Reminder service started! Will remind you every {interval_minutes} minutes.", sound="Hero")
    
    try:
        while True:
            next_reminder = datetime.now() + timedelta(seconds=interval_seconds)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Next reminder at {next_reminder.strftime('%H:%M:%S')}")
            
            # Countdown loop
            remaining = interval_seconds
            while remaining > 0:
                # Print remaining time on the same line
                sys.stdout.write(f"\rTime remaining: {format_time(remaining)}   ")
                sys.stdout.flush()
                time.sleep(1)
                remaining -= 1
            
            # Clear countdown line
            sys.stdout.write("\r" + " " * 40 + "\r")
            sys.stdout.flush()
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Sending reminder!")
            send_notification(
                title,
                "Time to drink some water! Take a short break and hydrate. 💧",
                sound="Glass"
            )
            
    except KeyboardInterrupt:
        print("\n\nStopping Drink Water Reminder. Stay hydrated! Bye! 💧")
        sys.exit(0)

if __name__ == "__main__":
    main()
