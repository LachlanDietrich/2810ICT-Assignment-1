import wx
import pandas as pd
import matplotlib.pyplot as plt  # Add this import statement
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from pandas.plotting import register_matplotlib_converters

# Register matplotlib converters to avoid a warning
register_matplotlib_converters()


class CalcFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, title="CSV Data Analyzer | Graph")

        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Open CSV File")
        self.button.Bind(wx.EVT_BUTTON, self.open_csv_file)

        self.csv_data = None

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.panel.SetSizerAndFit(self.sizer)

    def open_csv_file(self, event):
        wildcard = "CSV Files (*.csv)|*.csv"
        dialog = wx.FileDialog(None, "Open CSV File", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            dialog.Destroy()

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

            # Create a wxPython frame to display the chart
            graph_frame = wx.Frame(None, title="CSV Data Analyzer | Graph")
            canvas = FigureCanvasWxAgg(graph_frame, -1, fig)  # Use FigureCanvasWxAgg
            graph_frame.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
