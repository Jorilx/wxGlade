#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[], style=0)
        self.button_4 = wx.Button(self, wx.ID_ADD, "")
        self.button_5 = wx.Button(self, wx.ID_REMOVE, "")
        self.list_box_2 = wx.ListBox(self, wx.ID_ANY, choices=[], style=0)
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.button_2 = wx.Button(self, wx.ID_OK, "")
        self.button_1 = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(_("dialog_1"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        self.grid_sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)
        self.sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer_2 = wx.FlexGridSizer(1, 3, 0, 0)
        self.sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Assigned Permissions:")), wx.HORIZONTAL)
        self.sizer_4 = wx.FlexGridSizer(4, 1, 0, 0)
        self.sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Unassigned Permissions:")), wx.HORIZONTAL)
        self.sizer_2.Add(self.list_box_1, 1, wx.ALL | wx.EXPAND, 5)
        self.grid_sizer_2.Add(self.sizer_2, 1, wx.EXPAND, 0)
        self.sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        self.sizer_4.Add(self.button_4, 0, wx.ALL, 5)
        self.sizer_4.Add(self.button_5, 0, wx.ALL, 5)
        self.sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        self.sizer_4.AddGrowableRow(0)
        self.sizer_4.AddGrowableRow(3)
        self.grid_sizer_2.Add(self.sizer_4, 1, wx.EXPAND, 0)
        self.sizer_3.Add(self.list_box_2, 1, wx.ALL | wx.EXPAND, 5)
        self.grid_sizer_2.Add(self.sizer_3, 1, wx.EXPAND, 0)
        self.grid_sizer_2.AddGrowableRow(0)
        self.grid_sizer_2.AddGrowableCol(0)
        self.grid_sizer_2.AddGrowableCol(2)
        self.grid_sizer_1.Add(self.grid_sizer_2, 1, wx.EXPAND, 0)
        self.grid_sizer_1.Add(self.static_line_1, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer_1.Add(self.button_2, 0, wx.ALL, 5)
        self.sizer_1.Add(self.button_1, 0, wx.ALL, 5)
        self.grid_sizer_1.Add(self.sizer_1, 1, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        self.SetSizer(self.grid_sizer_1)
        self.grid_sizer_1.Fit(self)
        self.grid_sizer_1.AddGrowableRow(0)
        self.grid_sizer_1.AddGrowableCol(0)
        self.Layout()
        # end wxGlade

# end of class MyDialog

class MyApp(wx.App):
    def OnInit(self):
        self.dialog_1 = MyDialog(None, wx.ID_ANY, "")
        self.SetTopWindow(self.dialog_1)
        self.dialog_1.ShowModal()
        self.dialog_1.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()
