#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if __name__ == "__main__":
    window = Gtk.Window(title="Hello World")
    window.show()
    window.connect("delete-event", Gtk.main_quit)
    Gtk.main()
