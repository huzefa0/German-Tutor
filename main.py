import tkinter as tk
from tkinter import messagebox
from interactive_lessons import lessons_data, display_lesson
from speech_recognition import analyze_speech
from cultural_insights import show_cultural_insights

def open_speech_recognition():
    speech_window = tk.Toplevel()
    speech_window.title("Speech Recognition")

    level_label = tk.Label(speech_window, text="Select your language level:")
    level_label.pack(pady=10)

    level_var = tk.StringVar(value="A1")
    levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    for level in levels:
        level_button = tk.Radiobutton(speech_window, text=level, variable=level_var, value=level)
        level_button.pack(anchor="w", padx=20)

    def start_analysis():
        user_level = level_var.get()
        analyze_speech(user_level)

    start_button = tk.Button(speech_window, text="Start Speech Analysis", command=start_analysis)
    start_button.pack(pady=20)

    close_button = tk.Button(speech_window, text="Close", command=speech_window.destroy)
    close_button.pack(pady=10)

def open_interactive_lessons():
    lessons_window = tk.Toplevel()
    lessons_window.title("Interactive Lessons")

    level_label = tk.Label(lessons_window, text="Select your language level:")
    level_label.pack(pady=10)

    level_var = tk.StringVar(value="A1")
    levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    for level in levels:
        level_button = tk.Radiobutton(lessons_window, text=level, variable=level_var, value=level)
        level_button.pack(anchor="w", padx=20)

    def show_lessons():
        user_level = level_var.get()
        lessons = lessons_data.get(user_level, [])

        if lessons:
            lessons_list_window = tk.Toplevel()
            lessons_list_window.title(f"{user_level} Lessons")

            lessons_list_label = tk.Label(lessons_list_window, text=f"Lessons for {user_level}", font=("Arial", 14, "bold"))
            lessons_list_label.pack(pady=10)

            for lesson in lessons:
                lesson_button = tk.Button(lessons_list_window, text=lesson["title"], command=lambda l=lesson: display_lesson(user_level, l))
                lesson_button.pack(pady=5, fill="x")

            close_button = tk.Button(lessons_list_window, text="Close", command=lessons_list_window.destroy)
            close_button.pack(pady=10)
        else:
            tk.messagebox.showinfo("No Lessons", "No lessons available for this level.")

    show_button = tk.Button(lessons_window, text="Show Lessons", command=show_lessons)
    show_button.pack(pady=20)

    close_button = tk.Button(lessons_window, text="Close", command=lessons_window.destroy)
    close_button.pack(pady=10)

def open_cultural_insights():
    show_cultural_insights()

def main():
    root = tk.Tk()
    root.title("German Tutor")

    title_label = tk.Label(root, text="Welcome to the German Tutor App", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    speech_button = tk.Button(root, text="Speech Recognition", command=open_speech_recognition)
    speech_button.pack(pady=10, fill="x", padx=50)

    lessons_button = tk.Button(root, text="Interactive Lessons", command=open_interactive_lessons)
    lessons_button.pack(pady=10, fill="x", padx=50)

    cultural_button = tk.Button(root, text="Cultural Insights", command=open_cultural_insights)
    cultural_button.pack(pady=10, fill="x", padx=50)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
