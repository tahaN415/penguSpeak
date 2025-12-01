# AI models used for different tasks
whisperModel = "small.en"  # Model for speech recognition
"""possible options:
model 	             Required VRAM 	Relative speed
tiny.en 	            ~1 GB 	        ~10x
base.en 	            ~1 GB 	        ~7x
small.en 	            ~2 GB 	        ~4x
medium.en               ~5 GB 	        ~2x
"""


spacyModel = "en_core_web_md" #Model for Natural Language Processing 
""" possible options: 
en_core_web_sm	~12MB	Small model (basic performance)
en_core_web_md	~50MB	Medium model (better performance)
en_core_web_lg	~800MB	Large model (good accuracy)
en_core_web_trf	~400MB	Transformer-based (best accuracy)
"""

# Your computer settings
systemOs = 'omarchy'  # Your operating system


# add the names of the apps that you need and the command that tuns it in the terminal here
# first type the app name then the command that runs it like this example:
#   'terminal' : 'gnome-terminal'
apps = {
    'terminal' : 'alacritty',
    'beeper' : '~/AppImages/beeper.appimage',
    'file' or 'files' or 'nautilus': 'nautilus',
    'phone' or 'screen' or 'mobile': 'scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --audio-codec=opus --keyboard=uhid --mouse=uhid --stay-awake --turn-screen-off --kill',
    'task' or 'tasks': 'flatpak run net.nokyan.Resources',
    'browser' or 'zen': 'flatpak run app.zen_browser.zen',
    'code' or 'vscode': 'code',
}

# the command that is used to take screenshots, its gnome-screenshot by default for gnome
screenshot_cmd = 'omarchy-cmd-screenshot'
# the command for opening the screenshots folder in the file explorer, this is the default for gnome : nautilus -w Pictures
screenshot_open_path = 'nautilus -w Pictures'

# search command for your browser, put {term} for the search term
def search_cmd(term):
    search = f'{apps["browser"]} --search "{term}"'
    return search