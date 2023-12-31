import wx
import wx.grid
import pandas as pd
from datetime import datetime

from display_screen import MyFrame1
import matplotlib.pyplot as plt  # Add this import statement
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from pandas.plotting import register_matplotlib_converters

import tkinter as tk
import plotly.express as px
from PIL import Image, ImageTk
import io  # Import io module

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

df = pd.read_csv(r"listings_dec18.csv",
                 low_memory=False)  # CHANGE THIS TO FILE LOCATION OF listings_dec18.csv


#################################
##   class DataTable
#################################
class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


#################################
##   class CalcFrame
#################################
class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = DataTable(df)

        self.m_grid2.SetTable(self.table, takeOwnership=True)
        self.m_grid2.AutoSize()

        self.Show()
        self.Layout()

    def RentalsScreen(self, event):

        with open("calendar_dec18_piechart.py", "r") as code_file:
            code = code_file.read()
            exec(code)

    def CleanScreen(self, event):

        with open("cleanliness.py", "r") as code_file:
            code = code_file.read()
            exec(code)

    def OnDisplayMButton(self, event):
        pass

    # search func
    def OnSearch(self, event):
        search_val = self.m_textCtrl2.GetValue()

        if not search_val:  # if search is blank, return all data
            self.table = DataTable(df)
            self.m_grid2.SetTable(self.table, takeOwnership=True)
            self.m_grid2.AutoSize()
            self.Show(True)
            self.Layout()
            return

        search_start_val = self.start_period_box.GetValue()
        search_end_val = self.end_period_box.GetValue()

        # check for start/end dates
        if not search_start_val:
            pass
        else:
            search_start = datetime.strptime(search_start_val, '%Y-%m-%d')

        if not search_end_val:
            pass
        else:
            search_end = datetime.strptime(search_end_val, '%Y-%m-%d')

        df_all = df[df.applymap(lambda cell: str(search_val) in str(cell))]
        df['host_since'] = pd.to_datetime(df['host_since'], format='%Y-%m-%d')

        # checks for start/end dates, searches accordingly
        if not (search_start_val or search_end_val):
            df_filtered = df[
                df_all.apply(lambda row: row.astype(str).str.contains(search_val, case=False).any(),
                             axis=1)]  # lamda checks if any rows (axis=1) fit the search_val
        else:
            df_filtered = df[
                (df_all.apply(lambda row: row.astype(str).str.contains(search_val).any(), axis=1)) & (
                        df['host_since'] >= search_start) & (
                        df[
                            'host_since'] <= search_end)]  # lamda checks if any rows (axis=1) fit the search_val; checks using dates as well

        tabel = DataTable(df_filtered)
        self.m_grid2.ClearGrid()
        self.m_grid2.SetTable(tabel, True)
        self.m_grid2.AutoSize()
        self.Layout()


#################################
##   opens window on startup
#################################
if __name__ == '__main__':
    app = wx.App()
    frame = CalcFrame(None)
    frame.Show()
    app.MainLoop()
