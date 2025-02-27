from yapper import Yapper, PiperSpeaker, PiperVoiceUK, PiperVoiceUS, PiperQuality

lessac = PiperSpeaker(
    voice=PiperVoiceUK.CORI, quality=PiperQuality.HIGH)
lessac.say('''
My hope Will never Die!!
''')