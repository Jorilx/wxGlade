"""
Utilities, e.g. for debugging

@copyright: 2018-2020 Dietmar Schwertberger
@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""


from __future__ import print_function

import wx


def hx(obj):
    return hex(id(obj)).upper()


class StructurePrinter:
    # print the structure and sizes of a wx window with all it's children
    # this is not the wxGlade data structure
    def __init__(self, window):
        self.window(window, 0)

    def _sizer_item(self, si, indent):
        expand = (si.GetFlag() & wx.EXPAND) and "EXPAND" or ""
        print( "  "*indent, " SI:", si.GetMinSize(), " ", si.GetSize(), " ", si.GetProportion(), expand )

    def sizer(self, sizer, si, indent=0):
        cname = sizer.GetClassName() # u'wxPanel'
        print( "  "*indent, "%s"%cname, sizer.GetSize(), sizer )

        if si: self._sizer_item(si, indent)
        print()

        # list all by sizer
        for si in sizer.GetChildren():
            if si is None:
                print("Child is None")
                continue
            child = si.GetWindow()
            if child is not None:
                self.window(child, si, indent+1)
                continue
            child = si.GetSizer()
            if child is not None:
                self.sizer(child, si, indent+1)
                continue
            child = si.GetSpacer()
            if child is not None:
                self.spacer(child, si, indent+1)
                continue
            raise ValueError("XXX")

    def window(self, widget, si, indent=0):
        cname = widget.GetClassName() # u'wxPanel'
        name  = widget.GetName() # u'panel'
        HEX = hx(widget)
        try:
            best_size = widget.GetBestSize()
        except AttributeError:
            best_size ="???"
        print( "  "*indent, "%s: %s %s"%(cname, name, HEX), widget.GetSize(), best_size, widget.GetEffectiveMinSize() )

        if si: self._sizer_item(si, indent)

        sizer = widget.GetSizer()

        if sizer:
            # list all by sizer
            self.sizer(sizer, None, indent+1)
        else:
            # list all children
            for child in widget.GetChildren():
                self.window(child, None, indent+1)
        print()

    def spacer(self, spacer, si, indent=0):
        # a spacer
        print( "  "*indent, "Spacer", spacer.Get() )
        self._sizer_item(si, indent)
        print()


class TreePrinter:
    # print the structure of the TreeCtrl
    def __init__(self, root):
        print("=============================================================================")
        self.prn(root, 0)
        print("=============================================================================")

    def prn(self, editor, indent=0):
        all_children = editor.get_all_children()
        if not all_children: return
        for child in all_children:
            klass = "class" in child.PROPERTIES and child.klass or None
            print( "  "*indent, child.WX_CLASS, klass, getattr(child, "custom_class", "---"), child.IS_TOPLEVEL, child.CAN_BE_CLASS)
            self.prn(child, indent+1)

        print()
