import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            sentiment = "Positive"
        elif compound_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        messagebox.showinfo("Sentiment Analysis Result", f"Sentiment: {sentiment}\nCompound Score: {compound_score}")
    else:
        messagebox.showwarning("No Text", "Please enter some text.")

# Create the main window
window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("400x300")

# Create the label and text entry field
label = tk.Label(window, text="Enter text:")
label.pack()
text_entry = scrolledtext.ScrolledText(window, height=5)
text_entry.pack()

# Create the analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Start the main loop
window.mainloop()