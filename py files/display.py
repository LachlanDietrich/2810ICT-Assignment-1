# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#   import wx.xrc
import wx.dataview


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(640, 480), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.navbar = wx.MenuBar(0)
        self.nav_options = wx.Menu()
        self.options_graph = wx.Menu()
        self.nav_options.AppendSubMenu(self.options_graph, u"Graph")

        self.navbar.Append(self.nav_options, u"Options")

        self.SetMenuBar(self.navbar)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.searchbar = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.searchbar.ShowSearchButton(True)
        self.searchbar.ShowCancelButton(False)
        bSizer11.Add(self.searchbar, 1, wx.ALL | wx.EXPAND, 5)

        self.period_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.period_box, 0, wx.ALL, 5)

        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)

        self.data_box = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.data_box.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer10.Add(self.data_box, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    mainFrame = MyFrame1(None)
    mainFrame.Show()
    app.MainLoop()
