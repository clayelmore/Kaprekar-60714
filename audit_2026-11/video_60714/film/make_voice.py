"""Generate the narration takes in NARRATION.md with the cloned ElevenLabs voice.
Usage: /usr/bin/python3 make_voice.py [take numbers, e.g. 02 05]   (no arguments = all seven)
The voice id and the location of the API key file are read from voice.local.json, which is not in the repository."""
import json, os, re, subprocess, sys, urllib.request
LOCAL = json.load(open("voice.local.json"))        # not in the repository: {"voice": "<voice id>", "key_file": "<path to the key file>"}
KEY_FILE = os.path.expanduser(LOCAL["key_file"])
VOICE, MODEL = LOCAL["voice"], "eleven_multilingual_v2"
SETTINGS = {"stability": 0.6, "similarity_boost": 0.8, "style": 0.1, "use_speaker_boost": True, "speed": 1.0}
key = subprocess.run(["textutil", "-convert", "txt", "-stdout", KEY_FILE], capture_output=True, text=True).stdout.strip()
takes = re.findall(r"`(\d\d[a-z]?_\w+)\.wav`\n\s+(.+)", open("NARRATION.md").read())
want = set(sys.argv[1:])
for i, (name, text) in enumerate(takes):
    if want and name.split("_")[0] not in want: continue
    body = {"text": text, "model_id": MODEL, "voice_settings": SETTINGS}
    if i > 0: body["previous_text"] = takes[i-1][1]
    if i + 1 < len(takes): body["next_text"] = takes[i+1][1]
    req = urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_128" % VOICE,
                                 data=json.dumps(body).encode(), headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        audio = urllib.request.urlopen(req, timeout=120).read()
    except urllib.error.HTTPError as e:
        print(name, "FAILED", e.code, e.read()[:300].decode(errors="replace")); sys.exit(1)
    open("assets/vo/%s.mp3" % name, "wb").write(audio)
    if os.path.exists("assets/vo/%s.wav" % name): os.remove("assets/vo/%s.wav" % name)
    d = subprocess.run(["afinfo", "assets/vo/%s.mp3" % name], capture_output=True, text=True).stdout
    print(name, len(text), "chars", re.search(r"estimated duration: ([\d.]+)", d).group(1), "s")
