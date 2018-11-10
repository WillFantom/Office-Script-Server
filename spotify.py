import dbus
import subprocess

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object(
        "org.mpris.MediaPlayer2.spotify",
        "/org/mpris/MediaPlayer2" )

def get_properties():
    try:
        spotify_props = dbus.Interface(
            spotify_bus, "org.freedesktop.DBus.Properties" )
        data = spotify_props.Get(
            "org.mpris.MediaPlayer2.Player", "Metadata" )
        return ( data['xesam:title'], data['xesam:artist'][0] )
    except BaseException:
        return ('null', 'null')

def run_spotify_command(command):
    command = "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player." + command
    subprocess.call(command.split())

def send_spotify_command(command):
    c_title, c_artist = get_properties()
    if not(c_artist == 'null' and c_title == 'null'):
        if command.lower() == "play":
            run_spotify_command("Play")
        elif command.lower() == "pause":
            run_spotify_command("Pause")
        elif command.startswith("OpenUri string:spotify:track:"):
            run_spotify_command(command)
        elif command.lower() == "current":
            return get_properties()
    else:
        return 'null'