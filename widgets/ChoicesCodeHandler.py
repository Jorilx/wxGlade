"""\
Handler for the 'choices' property of various elements

@copyright: 2002-2007 Alberto Griggio
@copyright: 2016 Carsten Grohmann
@copyright: 2017 Dietmar Schwertberger
@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""


def xrc_write_choices_property(xrc_obj, outfile, tabs):
    "function used to write the XRC code for a ``choices'' property"
    from xml.sax.saxutils import escape
    choices = xrc_obj.properties['choices']
    write = outfile.write
    write('    '*tabs + '<content>\n')
    tab_s = '    ' * (tabs+1)
    for choice in choices:
        if isinstance(choice, tuple):
            write( tab_s + '<item checked="%d">%s</item>\n' % (choice[1], escape(choice[0])) )
        else:
            write( tab_s + '<item>%s</item>\n' % escape(choice) )
    write( '    '*tabs + '</content>\n' )

