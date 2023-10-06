import tkinter as tk
import pandas as pd
import plotly.express as px
from PIL import Image, ImageTk
import io  # Import io module

# Load your data
df = pd.read_csv("reviews_dec18.csv")

cleanliness_keywords = ["clean", "tidy", "sanitary", "hygienic", "spotless"]
df['comments'] = df['comments'].fillna('')

mentions_cleanliness = df['comments'].str.contains('|'.join(cleanliness_keywords), case=True)
total_cleanliness_comments = mentions_cleanliness.sum()

fig = px.pie(
    names=['Cleanliness Mentions', 'Other Mentions'],
    values=[total_cleanliness_comments, len(df) - total_cleanliness_comments],
    title='Percentage of Comments Mentioning Cleanliness'
)

# Convert Plotly figure to an image
fig_bytes = fig.to_image(format="png")
fig_image = Image.open(io.BytesIO(fig_bytes))

# Create a Tkinter window
root = tk.Tk()
root.title("Cleanliness")

# Convert the image to a Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(fig_image)

# Create a label to display the image
label = tk.Label(root, image=tk_image)
label.pack()

# Run the Tkinter main loop
root.mainloop()
