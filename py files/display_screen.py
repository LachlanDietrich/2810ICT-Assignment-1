import wx
import wx.dataview
import wx.grid
import pandas as pd
import sqlite3


#################################
##   class MyFrame1
#################################
class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(640, 480), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.navbar = wx.MenuBar(0)
        self.nav_options = wx.Menu()

        self.options_rentals = wx.MenuItem(self.nav_options, wx.ID_ANY, u"Rentals Graph (Selectable file)", wx.EmptyString, wx.ITEM_NORMAL)
        self.nav_options.Append(self.options_rentals)

        self.options_clean = wx.MenuItem(self.nav_options, wx.ID_ANY, u"Cleanliness Graph", wx.EmptyString, wx.ITEM_NORMAL)
        self.nav_options.Append(self.options_clean)

        self.navbar.Append(self.nav_options, u"Options")

        self.SetMenuBar(self.navbar)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_PROCESS_ENTER)
        bSizer11.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.start_period_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.start_period_box, 0, wx.ALL, 5)

        self.end_period_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.end_period_box, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DisplaySize(), 0)

        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

        # Grid
        self.m_grid2.CreateGrid(0, 0)
        self.m_grid2.EnableEditing(False)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer10.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.RentalsScreen, self.options_rentals)
        self.Bind(wx.EVT_MENU, self.CleanScreen, self.options_clean)
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnSearch)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnSearch(self, event):
        event.Skip()

    def RentalsScreen(self, event):
        event.Skip()

    def CleanScreen(self, event):
        event.Skip()

