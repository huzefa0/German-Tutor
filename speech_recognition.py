import speech_recognition as sr
from gtts import gTTS
import os

# Data for dialect detection and pronunciation hints
base_pronunciation_data = {
    "A1": {
        "words": {
            "Hallo": "HAH-loh",
            "Tschüss": "Chews",
            "Danke": "DAHN-kuh",
            "Bitte": "BIH-tuh",
            "Ja": "Yah",
            "Nein": "Nine",
            "Entschuldigung": "En-shool-dee-goong",
            "Guten Tag": "GOO-ten Tahg",
        },
        "dialects": ["Standard German"]
    },
    "A2": {
        "words": {
            "Guten Morgen": "GOO-ten MOR-gen",
            "Auf Wiedersehen": "OwF VEE-der-zay-en",
            "Ich verstehe nicht": "Eekh fer-SHTAY-uh nikht",
            "Wie viel kostet das?": "Vee feel KOS-tet dahs?",
            "Sprechen Sie Englisch?": "SHPREH-khen zee ENG-lish?",
            "Wo ist die Toilette?": "Vo ist dee Toy-LET-te?",
        },
        "dialects": ["Standard German", "Bavarian"]
    },
    "B1": {
        "words": {
            "Könnten Sie mir helfen?": "KERN-ten zee meer HEL-fen?",
            "Ich brauche Hilfe": "Eekh BROW-khuh HIL-feh",
            "Können Sie das wiederholen?": "KERN-nen zee dahs VEE-der-HO-len?",
            "Das Wetter ist schön": "Dahs VET-ter ist SHURN",
            "Wo kann ich das finden?": "Vo kann eekh dahs FIN-den?",
            "Was empfehlen Sie?": "Vahs em-FAY-len zee?",
        },
        "dialects": ["Standard German", "Saxon"]
    },
    "B2": {
        "words": {
            "Können wir uns duzen?": "KERN-nen veer oons DOOT-sen?",
            "Könnten Sie das erklären?": "KERN-ten zee dahs er-KLAY-ren?",
            "Ich interessiere mich für": "Eekh in-ter-es-SEE-reh mikh fuer",
            "Das macht Sinn": "Dahs mahkht Zinn",
            "Vielen Dank für Ihre Hilfe": "FEE-len dahnk fuer EE-reh HIL-feh",
            "Ich stimme Ihnen zu": "Eekh STIM-meh EE-nen tsu",
        },
        "dialects": ["Standard German", "Berlinisch"]
    },
    "C1": {
        "words": {
            "Das ist eine gute Frage": "Dahs ist EYE-neh GOO-teh FRAH-geh",
            "Wie beurteilen Sie das?": "Vee beh-UR-tay-len zee dahs?",
            "Das kann ich nachvollziehen": "Dahs kann eekh NAHCH-fol-tsee-en",
            "Ich bin derselben Meinung": "Eekh bin DARE-sel-ben MINE-oong",
            "Die Diskussion ist spannend": "Dee DIS-koo-see-OHN ist SHPAN-nend",
            "Das ist eine Herausforderung": "Dahs ist EYE-neh Her-OWS-for-de-roong",
        },
        "dialects": ["Standard German", "Franconian"]
    },
    "C2": {
        "words": {
            "Es war mir eine Ehre": "Es vahr meer EYE-neh EH-reh",
            "Könnten wir detaillierter darauf eingehen?": "KERN-ten veer DAY-tie-ree-ter dah-ROWF IN-geh-en?",
            "Ich würde es bevorzugen": "Eekh VOOR-deh es beh-FOR-tsu-gen",
            "Das ist eine umstrittene Ansicht": "Dahs ist EYE-neh oom-STRIT-teh-neh AHN-zikht",
            "Ich schätze Ihre Perspektive": "Eekh SHET-zeh EE-reh Per-spek-TEE-veh",
            "Lassen Sie uns das näher beleuchten": "LAH-sen zee oons dahs NAY-er beh-LOYKH-ten",
        },
        "dialects": ["Standard German", "Austrian"]
    },
}
def build_pronunciation_data(base_data):
    cumulative_data = {}
    for level in ["A1", "A2", "B1", "B2", "C1", "C2"]:
        cumulative_words = {}
        cumulative_dialects = set()

        for prior_level in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            if prior_level == level:
                break
            cumulative_words.update(base_data[prior_level]["words"])
            cumulative_dialects.update(base_data[prior_level]["dialects"])

        cumulative_words.update(base_data[level]["words"])
        cumulative_dialects.update(base_data[level]["dialects"])

        cumulative_data[level] = {
            "words": cumulative_words,
            "dialects": list(cumulative_dialects),
        }

    return cumulative_data

pronunciation_data = build_pronunciation_data(base_pronunciation_data)

def analyze_speech(user_level):
    try:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        print("Please speak a word or phrase...")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        spoken_text = recognizer.recognize_google(audio, language="de-DE")
        print(f"You said: {spoken_text}")

        # Check for dialect and pronunciation suggestions
        level_data = pronunciation_data.get(user_level, {})
        pronunciation_hint = level_data.get("words", {}).get(spoken_text, None)

        if pronunciation_hint:
            print(f"Correct pronunciation: {pronunciation_hint}")

            # Use gTTS to provide the correct pronunciation
            tts = gTTS(text=f"Correct pronunciation is {pronunciation_hint}", lang="de")
            tts.save("pronunciation.mp3")
            os.system("start pronunciation.mp3")
        else:
            print("No specific pronunciation hint available for this word.")

        dialects = level_data.get("dialects", [])
        if dialects:
            print(f"Detected dialects for this level: {', '.join(dialects)}")

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except AttributeError as attr_err:
        print("An unexpected error occurred. Please ensure that the speech_recognition module is installed correctly.")
        print(attr_err)

# Example usage
if __name__ == "__main__":
    user_level = "A1"  # Replace with dynamic user level
    analyze_speech(user_level)
