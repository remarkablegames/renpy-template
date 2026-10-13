init python:
    BLEEP_CHANNEL = "bleep"
    renpy.music.register_channel(BLEEP_CHANNEL, mixer="voice", loop=True)


    def make_voice(filename):
        def callback(event, **kwargs):
            if event == "show_done":
                renpy.music.play(f"voice/{filename}.ogg", channel=BLEEP_CHANNEL, relative_volume=2)

            elif event in ("slow_done", "end"):
                renpy.music.stop(channel=BLEEP_CHANNEL, fadeout=.2)

        return callback


    def dismiss_callback() -> bool:
        renpy.sound.play("ui/click.ogg")
        return True


    config.say_allow_dismiss = dismiss_callback


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen", image="eileen", callback=make_voice("bleep024"))
define narrator = Character(None, callback=make_voice("bleep030"))
