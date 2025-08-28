# Open Chrome with Specific Profile

![License](https://img.shields.io/badge/License-AGPL--3.0-blue.svg) ![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)

## Overview 🌐

This Python script allows you to easily launch **Google Chrome** or **Chromium** with a specific user profile. Whether you want to separate your work and personal browsing or use multiple profiles at once, this tool streamlines the process without relying on **Selenium**.

You can also pass an optional URL to open directly in a new window with your selected profile. It automatically detects and uses the correct Chrome/Chromium binary from your system's PATH.

## Features 🚀

- Open **Google Chrome** or **Chromium** with a specified user profile.
- Launch a new Chrome window with a specific profile folder (e.g., 'Default', 'Profile 1', etc.).
- Optionally open a specified URL in a new Chrome window.
- Cross-platform support: Works on any system with Chrome or Chromium installed.

## Requirements 📋

- Python 3.6+  
- **Google Chrome** or **Chromium** installed on your machine.
- The Chrome/Chromium binary must be in your system's **PATH**.

## Installation 🔧

1. **Clone the repository** or download the script:

```bash
   git clone https://github.com/Behdad-kanaani/Open-Chrome-with-Specific-Profile.git
   cd Open-Chrome-with-Specific-Profile
````

2. **Install dependencies** (if any):
   There are no external dependencies, but make sure you have Python 3.x installed.

3. **Ensure Chrome or Chromium is installed** and accessible via your system's PATH.

## Usage ⚙️

To use this script, simply run the Python file with the following options:

```bash
python open_chrome.py --user-data-dir <path_to_user_data_dir> --profile <profile_name> --url <optional_url>
```

### Arguments:

* `--user-data-dir`
  **Default:** `~/.config/google-chrome`
  Specifies the path to the Chrome/Chromium user data directory. For Chromium, it's typically `~/.config/chromium`.

* `--profile`
  **Default:** `Default`
  Specifies the profile folder name. For example: 'Default', 'Profile 1', 'Profile 2', etc.

* `--url`
  **Optional**
  The URL to open in the new Chrome window. If not specified, Chrome will just open a blank window with the selected profile.

### Example:

```bash
python open_chrome.py --user-data-dir ~/.config/chromium --profile "Profile 1" --url https://github.com
```

This command opens **Chromium** with the profile "Profile 1" and navigates to `https://github.com`.

### Example without URL:

```bash
python open_chrome.py --profile "Profile 2"
```

This will open **Google Chrome** with the profile "Profile 2" in a new window without opening a specific URL.

## Error Handling ⚠️

* If Chrome or Chromium is not found in your PATH, the script will notify you and exit gracefully.
* In case of any issues launching Chrome, error details will be displayed.

## Why Use This Script? 🤔

* **Organize your browsing:** Use different profiles for work, personal browsing, testing, or development without mixing data.
* **Easy access to your profiles:** Launch Chrome with any profile and URL in just one command.
* **No Selenium required:** This is a lightweight solution compared to using Selenium, ideal for simpler tasks like opening specific profiles.

## License 📜

This project is licensed under the **AGPL-3.0 License**. See the [LICENSE](LICENSE) file for more details.

## Contributing 💡

Feel free to fork this project, submit issues, and open pull requests for improvements. Contributions are welcome!

## Contact 📬

If you have any questions, suggestions, or feedback, feel free to open an issue or reach out.

---

Thanks for using **Behdad-kanaani/Open-Chrome-with-Specific-Profile**! 🚀
