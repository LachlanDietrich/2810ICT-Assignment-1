import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.plotting import register_matplotlib_converters
import wx

# Register matplotlib converters to avoid a warning
register_matplotlib_converters()

# Create the main window

root = tk.Tk()
root.geometry("800x600")
root.title("CSV Data Analyzer")


# Function to open a CSV file and display a pie chart
def open_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)

        # Convert the 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Filter the DataFrame for the desired date range
        start_date = pd.to_datetime('2018-12-06')
        end_date = pd.to_datetime('2019-12-18')
        df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

        # Extract month from the 'date' column and count occurrences
        df['month'] = df['date'].dt.strftime('%B')
        month_counts = df['month'].value_counts()

        # Create a pie chart
        fig, ax = plt.subplots()
        month_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Percentage of Airbnb Rentals (Period December 2018 - December 2019)')

        # Remove the y-label (count label)
        ax.set_ylabel('')

        # Display the pie chart in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)


# Create an "Open CSV File" button
open_button = tk.Button(root, text="Open CSV File", command=open_csv_file)
open_button.pack(pady=10)

if __name__ == '__main__':
    root.mainloop()
