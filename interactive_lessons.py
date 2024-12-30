# File: interactive_lessons.py

import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Sample lessons data structure
lessons_data = {
    "A1": [
        {
            "title": "Greetings and Introductions",
            "content": """
            In German, greetings are important as they reflect the culture. 
            Common greetings:
            - Hallo! (Hello!)
            - Guten Morgen! (Good morning!)
            - Guten Tag! (Good day!)
            - Guten Abend! (Good evening!)
            - Wie geht's? (How are you?)
            - Mir geht's gut, danke! (I’m fine, thank you!)
            - Tschüss! (Bye!)
            
            Cultural Tip:
            - It’s common in Germany to shake hands when greeting someone for the first time. 
            When meeting friends, a hug or a kiss on both cheeks is typical.
            """,
        },
        {
            "title": "Numbers and Dates",
            "content": """
            Numbers from 1 to 10 in German:
            - 1 – eins
            - 2 – zwei
            - 3 – drei
            - 4 – vier
            - 5 – fünf
            - 6 – sechs
            - 7 – sieben
            - 8 – acht
            - 9 – neun
            - 10 – zehn

            Dates:
            - Heute ist der 1. Januar. (Today is January 1st.)
            - Am 15. März. (On March 15th.)
            """
        },
        {
            "title": "Family and Friends",
            "content": """
            Vocabulary for family members in German:
            - die Mutter (mother)
            - der Vater (father)
            - die Schwester (sister)
            - der Bruder (brother)
            - die Großmutter (grandmother)
            - der Großvater (grandfather)
            - die Tante (aunt)
            - der Onkel (uncle)

            Talking about friends:
            - mein Freund (my friend - male)
            - meine Freundin (my friend - female)
            """
        },
        {
            "title": "Daily Activities",
            "content": """
            Common verbs for daily routines:
            - essen (to eat)
            - trinken (to drink)
            - schlafen (to sleep)
            - arbeiten (to work)
            - lernen (to learn)
            - gehen (to go)

            Example sentences:
            - Ich esse Frühstück um 8 Uhr. (I have breakfast at 8 AM.)
            - Er arbeitet im Büro. (He works in the office.)
            """
        },
        {
            "title": "Shopping and Food",
            "content": """
            Common food-related words in German:
            - das Brot (bread)
            - die Butter (butter)
            - die Wurst (sausage)
            - der Käse (cheese)
            - die Kartoffeln (potatoes)
            - die Tomaten (tomatoes)

            Phrases for shopping:
            - Wie viel kostet das? (How much does it cost?)
            - Ich möchte das kaufen. (I would like to buy this.)
            - Haben Sie…? (Do you have…?)
            """
        }
    ],
    "A2": [
        {
            "title": "Talking about the Weather",
            "content": """
            Common weather vocabulary:
            - das Wetter (the weather)
            - der Regen (the rain)
            - der Schnee (the snow)
            - die Sonne (the sun)
            - der Wind (the wind)
            - es ist warm (it's warm)
            - es ist kalt (it's cold)
            - es regnet (it's raining)

            Example sentences:
            - Wie ist das Wetter heute? (How's the weather today?)
            - Es regnet heute. (It's raining today.)
            """
        },
        {
            "title": "Making Plans",
            "content": """
            Common phrases for making plans:
            - Hast du Zeit? (Do you have time?)
            - Möchtest du ins Kino gehen? (Do you want to go to the cinema?)
            - Ich habe keine Zeit. (I don't have time.)
            - Wann können wir uns treffen? (When can we meet?)

            Example sentences:
            - Wir können uns morgen um 3 Uhr treffen. (We can meet tomorrow at 3 PM.)
            """
        },
        {
            "title": "Travel and Directions",
            "content": """
            Vocabulary for traveling:
            - der Bahnhof (the train station)
            - die Bushaltestelle (the bus stop)
            - der Flughafen (the airport)
            - der Weg (the way/path)
            - rechts (right)
            - links (left)

            Example sentences:
            - Wie komme ich zum Bahnhof? (How do I get to the train station?)
            - Gehen Sie geradeaus und dann nach rechts. (Go straight ahead and then turn right.)
            """
        },
        {
            "title": "Food and Drink",
            "content": """
            Vocabulary for food and drink:
            - das Wasser (water)
            - der Kaffee (coffee)
            - der Apfel (apple)
            - das Gemüse (vegetables)
            - das Fleisch (meat)
            - der Salat (salad)

            Example sentences:
            - Ich hätte gerne einen Kaffee. (I would like a coffee.)
            - Möchtest du Wasser oder Saft? (Do you want water or juice?)
            """
        },
        {
            "title": "Shopping for Clothes",
            "content": """
            Vocabulary for shopping:
            - die Hose (pants)
            - das Hemd (shirt)
            - der Mantel (coat)
            - die Schuhe (shoes)
            - der Hut (hat)
            - die Jacke (jacket)

            Example sentences:
            - Wie viel kostet dieses Hemd? (How much does this shirt cost?)
            - Ich möchte diese Jacke kaufen. (I would like to buy this jacket.)
            """
        }
    ],
    "B1": [
        {
            "title": "Expressing Opinions",
            "content": """
            Common phrases for expressing opinions:
            - Ich denke, dass... (I think that...)
            - Meiner Meinung nach... (In my opinion...)
            - Ich bin der Meinung, dass... (I am of the opinion that...)
            - Es scheint mir, dass... (It seems to me that...)

            Example sentences:
            - Ich denke, dass wir morgen schönes Wetter haben werden. (I think we will have nice weather tomorrow.)
            - Meiner Meinung nach ist dieses Buch sehr interessant. (In my opinion, this book is very interesting.)
            """
        },
        {
            "title": "Describing People and Appearances",
            "content": """
            Vocabulary for describing people:
            - groß (tall)
            - klein (short)
            - schlank (slim)
            - dick (fat)
            - braune Augen (brown eyes)
            - blonde Haare (blonde hair)

            Example sentences:
            - Er ist groß und hat braune Augen. (He is tall and has brown eyes.)
            - Sie trägt ein rotes Kleid. (She is wearing a red dress.)
            """
        },
        {
            "title": "Health and Fitness",
            "content": """
            Vocabulary for health:
            - die Krankheit (illness)
            - der Arzt (doctor)
            - das Medikament (medicine)
            - fit (fit)
            - die Übung (exercise)

            Example sentences:
            - Ich muss mehr Sport machen, um fit zu bleiben. (I need to exercise more to stay fit.)
            - Hast du schon einen Arzttermin gemacht? (Have you already made a doctor’s appointment?)
            """
        },
        {
            "title": "At the Doctor's Office",
            "content": """
            Common phrases at the doctor's office:
            - Ich habe Bauchschmerzen. (I have a stomach ache.)
            - Ich fühle mich krank. (I feel sick.)
            - Wo tut es weh? (Where does it hurt?)
            - Ich brauche ein Rezept. (I need a prescription.)

            Example sentences:
            - Der Arzt sagt, dass ich mich ausruhen soll. (The doctor says I should rest.)
            """
        },
        {
            "title": "Talking About Hobbies",
            "content": """
            Vocabulary for hobbies:
            - das Hobby (hobby)
            - die Musik (music)
            - das Buch (book)
            - der Sport (sports)
            - das Tanzen (dancing)

            Example sentences:
            - Mein Hobby ist Musik hören. (My hobby is listening to music.)
            - Ich liebe es, im Park spazieren zu gehen. (I love walking in the park.)
            """
        }
    ],
    "B2": [
        {
            "title": "Discussing Future Plans",
            "content": """
            Vocabulary for future plans:
            - der Plan (plan)
            - die Zukunft (future)
            - der Traum (dream)
            - die Reise (trip)

            Example sentences:
            - Ich habe vor, im Sommer nach Italien zu reisen. (I plan to travel to Italy in the summer.)
            - Mein Traum ist es, ein eigenes Geschäft zu haben. (My dream is to have my own business.)
            """
        },
        {
            "title": "Talking about Experiences",
            "content": """
            Phrases for discussing experiences:
            - Ich habe schon einmal... (I have already...)
            - Es war eine tolle Erfahrung. (It was a great experience.)
            - Ich erinnere mich an... (I remember...)
            
            Example sentences:
            - Ich habe schon einmal in Frankreich Urlaub gemacht. (I have been on vacation in France before.)
            - Es war eine interessante Erfahrung, in einem internationalen             Unternehmen zu arbeiten. (It was an interesting experience working in an international company.)
            """
        },
        {
            "title": "Debating and Arguing",
            "content": """
            Common phrases for debating and arguing:
            - Ich stimme dir zu. (I agree with you.)
            - Ich denke, du hast Unrecht. (I think you're wrong.)
            - Es gibt verschiedene Ansichten zu diesem Thema. (There are different views on this topic.)
            - Meiner Meinung nach... (In my opinion...)

            Example sentences:
            - Ich stimme dir zu, aber ich sehe auch deinen Punkt. (I agree with you, but I also see your point.)
            - Es ist ein komplexes Thema, aber meiner Meinung nach sollte man es anders angehen. (It's a complex topic, but in my opinion, it should be approached differently.)
            """
        },
        {
            "title": "Discussing Social Issues",
            "content": """
            Vocabulary for discussing social issues:
            - die Gesellschaft (society)
            - die Umwelt (environment)
            - die Armut (poverty)
            - die Gerechtigkeit (justice)
            - die Freiheit (freedom)

            Example sentences:
            - Wir müssen mehr für die Umwelt tun. (We need to do more for the environment.)
            - Die soziale Gerechtigkeit ist ein wichtiges Thema. (Social justice is an important issue.)
            """
        },
        {
            "title": "Job Interviews and Career",
            "content": """
            Vocabulary for job interviews:
            - der Lebenslauf (resume)
            - das Vorstellungsgespräch (job interview)
            - die Fähigkeiten (skills)
            - die Erfahrung (experience)

            Example sentences:
            - Können Sie mir mehr über Ihre Erfahrung erzählen? (Can you tell me more about your experience?)
            - Warum sollten wir Sie für diese Position einstellen? (Why should we hire you for this position?)
            """
        },
        {
            "title": "Giving and Receiving Feedback",
            "content": """
            Common phrases for giving and receiving feedback:
            - Du hast gute Arbeit geleistet. (You did a great job.)
            - Ich denke, es gibt Raum für Verbesserung. (I think there's room for improvement.)
            - Wie können wir das verbessern? (How can we improve this?)
            - Ich schätze dein Feedback. (I appreciate your feedback.)

            Example sentences:
            - Du hast die Aufgabe gut erledigt, aber ich denke, wir könnten es beim nächsten Mal noch besser machen. (You did the task well, but I think we could do it even better next time.)
            """
        }
    ]
}

# Initialize main window
root = tk.Tk()
root.title("Interactive Language Lessons")
root.geometry("800x600")

# Create frames for different sections (main menu and lessons)
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill=tk.BOTH, expand=True)

lesson_frame = tk.Frame(root)

# Function to show lesson selection after a level is chosen
def show_lessons(level):
    # Clear the main menu frame
    for widget in main_menu_frame.winfo_children():
        widget.destroy()

    # Show the lesson frame
    lesson_frame.pack(fill=tk.BOTH, expand=True)

    # Populate the listbox with lesson titles for the selected level
    lesson_listbox.delete(0, tk.END)  # Clear existing items
    for lesson in lessons_data[level]:
        lesson_listbox.insert(tk.END, lesson["title"])

    # Add a label and a listbox for lesson selection
    lesson_label = tk.Label(lesson_frame, text=f"Select a Lesson for {level}", font=("Arial", 18))
    lesson_label.pack(pady=20)

    lesson_listbox.pack(pady=10)
    lesson_content_text.pack(pady=10)

# Function to return to the main menu
def back_to_main_menu():
    lesson_frame.pack_forget()
    main_menu_frame.pack(fill=tk.BOTH, expand=True)

# Create the main menu
level_label = tk.Label(main_menu_frame, text="Select Your Level", font=("Arial", 18))
level_label.pack(pady=20)

level_buttons = []

for level in lessons_data.keys():
    button = tk.Button(main_menu_frame, text=level, font=("Arial", 14), width=20, command=lambda level=level: show_lessons(level))
    button.pack(pady=5)
    level_buttons.append(button)

# Textbox to show lesson content
lesson_content_text = tk.Text(lesson_frame, height=15, width=60, font=("Arial", 12), wrap=tk.WORD)

# Listbox to display lesson titles for selection
lesson_listbox = tk.Listbox(lesson_frame, height=10, width=40, font=("Arial", 12))

# Function to display selected lesson content
def display_lesson_content(event):
    selected_title = lesson_listbox.get(lesson_listbox.curselection())
    lesson_content_text.delete(1.0, tk.END)
    
    # Find the content of the selected lesson title
    for level, lessons in lessons_data.items():
        for lesson in lessons:
            if lesson["title"] == selected_title:
                lesson_content_text.insert(tk.END, f"Title: {lesson['title']}\n")
                lesson_content_text.insert(tk.END, f"Content: {lesson['content']}\n\n")
                return

# Bind event to listbox
lesson_listbox.bind('<<ListboxSelect>>', display_lesson_content)

# Back button to go back to main menu
back_button = tk.Button(lesson_frame, text="Back to Main Menu", font=("Arial", 14), command=back_to_main_menu)
back_button.pack(pady=20)

# Function to start speech recognition
def start_speech_recognition():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        messagebox.showinfo("Speech Recognition", "Please speak now...")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language="de-DE")
            messagebox.showinfo("Speech Recognition Result", f"You said: {text}")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Sorry, there was a problem with the speech service.")

# Button to start speech recognition
speech_button = tk.Button(lesson_frame, text="Start Speech Recognition", font=("Arial", 14), command=start_speech_recognition)
speech_button.pack(pady=20)

# Run the main loop
root.mainloop()