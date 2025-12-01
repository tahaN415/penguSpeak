
PenguSpeak 🐧🔊💡

PenguSpeak is a voice-command tool that uses OpenAI Whisper for speech recognition and executes system commands like volume and brightness adjustments. It notifies the user with system notifications and logs every action.
📦 Installation
1️⃣ Clone the Repository

git clone github.com/robogamer9849/penguSpeak.git
cd penguspeak

2️⃣ Install Required Python Packages

`pip install openai-whisper sounddevice wavio notify-py spacy` <break/>

Or:

3️⃣ Install Required System Packages (apt)

`sudo apt install ffmpeg brightnessctl pamixer fastfetch`

⚙️ Configuration

Edit the config.py file to:

    Set the Whisper and spacy models used for transcription and NLP.

    Specify your system OS.

    Define the commands for brightness and volume control, system info, and more (if needed).

    add the apps you want as shown in the example

    configure screenshot and web search commands as needed

🚀 Usage

1️⃣ Run the Script
A run.sh file is already provided to start the program.

2️⃣ Set a Keyboard Shortcut
Set up a custom keyboard shortcut in your system pointing to the run.sh file. For example:

    Command: /path/to/penguspeak/run.sh

    Shortcut: (e.g., Ctrl+Alt+S)

This allows you to activate PenguSpeak by pressing a key combination.

3️⃣ Speak!
Press the shortcut and speak commands like:

    "Set volume to 30"

    "Increase brightness by 10"

    "Mute sound"

    "Set brightness to maximum"

    "open terminal"

    "search for one UI 7 release date"

🔥 Features

    Voice recognition using OpenAI Whisper

    Volume control: set, increase, decrease, mute, unmute

    Brightness control: set, increase, decrease

    opening apps: as you defined in the config

    searching with your default browser (firefox-based browsers only)

    Notifications and system info display

    Logging to pengu_speak.log

📝 Dependencies

    Python packages: whisper, sounddevice, wavio, notifypy

    System packages: ffmpeg, brightnessctl, pamixer, neofetch, 

🐧 License

MIT License – use, modify, share!
