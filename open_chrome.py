"""
Open Chrome/Chromium with a specific profile without using Selenium.
"""

import os
import sys
import shutil
import subprocess
import argparse

CANDIDATES = [
    "google-chrome-stable",
    "google-chrome",
    "chromium-browser",
    "chromium",
]

def find_chrome():
    for name in CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    return None

def main():
    parser = argparse.ArgumentParser(
        description="Open Chrome with a specific profile (no Selenium)."
    )
    parser.add_argument(
        "--user-data-dir",
        default=os.path.expanduser("~/.config/google-chrome"),
        help="Path to the user data directory (for Chromium usually ~/.config/chromium)."
    )
    parser.add_argument(
        "--profile",
        default="Default",
        help="Profile folder name: 'Default', 'Profile 1', etc."
    )
    parser.add_argument(
        "--url",
        default=None,
        help="Optional: URL to open in the new window."
    )
    args = parser.parse_args()

    chrome = find_chrome()
    if not chrome:
        print(
            "❌ Chrome/Chromium not found. Install one of these or add to PATH: "
            "google-chrome-stable, google-chrome, chromium-browser, chromium",
            file=sys.stderr
        )
        sys.exit(1)

    cmd = [
        chrome,
        f"--user-data-dir={args.user_data_dir}",
        f"--profile-directory={args.profile}",
        "--new-window",
    ]
    if args.url:
        cmd.append(args.url)

    try:
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ {os.path.basename(chrome)} launched with profile '{args.profile}'.")
    except Exception as e:
        print(f"❌ Failed to launch Chrome: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
