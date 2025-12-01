from notifypy import Notify
import subprocess
import logging
from pathlib import Path
import subprocess


def get_command(action, x):
    commands = {
        'brightness_set': f'brightnessctl set {x}%',
        'brightness_up': f'brightnessctl set +{x}%',
        'brightness_down': f'brightnessctl set {x}%-',
        'Display system information and hardware specifications': 'fastfetch',
        'Print detailed system and kernel information': 'uname -a',
        'volume_set': f'pamixer --set-volume {x} --allow-boost',
        'volume_up': f'pamixer -i {x} --allow-boost',
        'volume_down': f'pamixer -d {x} --allow-boost',
        'volume_mute': 'pamixer -m',
        'volume_unmute': 'pamixer -u --allow-boost',
        'run app': f'{x}'
    }

    cmd = commands[action]

    return(cmd)

def run_cmd(cmd):
    try:
        subprocess.Popen(cmd, shell = True)
        logging.info(f'Command executed: {cmd}')
    except Exception as e:
        logging.error(f'Command execution failed: {cmd}, Error: {str(e)}')
        pass

def send_notification(message):
    notification = Notify()
    notification.title = 'PenguSpeak'
    notification.message = message
    notification.icon = f'{Path(__file__).parent.resolve()}/../logo.png'
    notification.send()
    logging.info(f'Notification sent: {message}')

def extract_int(text):
    num = None
    for word in text.split():
            try:
                num = int(word)
                break
            except ValueError:
                continue
    return num