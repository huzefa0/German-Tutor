#File: cultural_insights.py
import tkinter as tk
from tkinter import messagebox

# Extended cultural insights data
cultural_insights_data = {
    "Idioms": [
        {"idiom": "Den Nagel auf den Kopf treffen", "meaning": "To hit the nail on the head", "example": "Mit dieser Antwort hast du den Nagel auf den Kopf getroffen."},
        {"idiom": "Die Kirche im Dorf lassen", "meaning": "To not get carried away", "example": "Lass die Kirche im Dorf, so schlimm ist es auch wieder nicht."},
        {"idiom": "Eine Extrawurst verlangen", "meaning": "To ask for special treatment", "example": "Er verlangt immer eine Extrawurst."},
        {"idiom": "Jemanden auf die Palme bringen", "meaning": "To drive someone up the wall", "example": "Sein Verhalten bringt mich auf die Palme."},
        {"idiom": "Klar wie Kloßbrühe", "meaning": "Crystal clear", "example": "Das ist doch klar wie Kloßbrühe!"},
        # Add more idioms to reach 50...
    ],
    "Dialects": [
        {"dialect": "Bavarian", "info": "Spoken in Bavaria and parts of Austria. Known for its unique vocabulary and pronunciation."},
        {"dialect": "Swabian", "info": "Spoken in southwestern Germany. It has a distinctive melody and soft pronunciation."},
        {"dialect": "Saxon", "info": "Spoken in eastern Germany. Often considered soft and lilting."},
        {"dialect": "Berlinisch", "info": "Berlin's local dialect with unique expressions and humor."},
        {"dialect": "Franconian", "info": "A group of dialects spoken in Franconia, northern Bavaria."},
        # Add more dialects to reach 50...
    ],
    "Cultural Notes": [
        {"note": "Germans value punctuality and direct communication."},
        {"note": "Bread (Brot) is a staple in German cuisine, and there are over 300 varieties."},
        {"note": "Christmas markets (Weihnachtsmärkte) are a cherished tradition."},
        {"note": "The Autobahn is famous for stretches without speed limits."},
        {"note": "Germany is known for its engineering and manufacturing excellence."},
        # Add more cultural notes to reach 50...
    ],
}

def show_cultural_insights():
    insights_window = tk.Toplevel()
    insights_window.title("Cultural Insights")
    
    idioms_label = tk.Label(insights_window, text="Idioms", font=("Arial", 14, "bold"))
    idioms_label.pack(pady=5)
    for idiom in cultural_insights_data["Idioms"]:
        idiom_text = f"{idiom['idiom']}\nMeaning: {idiom['meaning']}\nExample: {idiom['example']}"
        idiom_label = tk.Label(insights_window, text=idiom_text, wraplength=400, justify="left")
        idiom_label.pack(pady=5)
    
    dialects_label = tk.Label(insights_window, text="Dialects", font=("Arial", 14, "bold"))
    dialects_label.pack(pady=5)
    for dialect in cultural_insights_data["Dialects"]:
        dialect_text = f"{dialect['dialect']}\n{dialect['info']}"
        dialect_label = tk.Label(insights_window, text=dialect_text, wraplength=400, justify="left")
        dialect_label.pack(pady=5)

    cultural_notes_label = tk.Label(insights_window, text="Cultural Notes", font=("Arial", 14, "bold"))
    cultural_notes_label.pack(pady=5)
    for note in cultural_insights_data["Cultural Notes"]:
        note_label = tk.Label(insights_window, text=note["note"], wraplength=400, justify="left")
        note_label.pack(pady=5)

    close_button = tk.Button(insights_window, text="Close", command=insights_window.destroy)
    close_button.pack(pady=10)
