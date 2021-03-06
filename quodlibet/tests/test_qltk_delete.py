# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

from gi.repository import Gtk

from tests import TestCase

from quodlibet import config
from quodlibet.formats import AudioFile
from quodlibet.util.path import fsnative
from quodlibet.qltk.delete import DeleteDialog, TrashDialog, TrashMenuItem

SONG = AudioFile({"~filename": fsnative(u"/dev/null")})
SONG.sanitize()


class TDeleteDialog(TestCase):

    def setUp(self):
        config.init()

    def tearDown(self):
        config.quit()

    def test_delete_songs(self):
        dialog = DeleteDialog.for_songs(None, [])
        dialog.destroy()

    def test_delete_files(self):
        dialog = DeleteDialog.for_files(None, [])
        dialog.destroy()

    def test_trash_songs(self):
        dialog = TrashDialog.for_songs(None, [])
        dialog.destroy()

    def test_trash_files(self):
        dialog = TrashDialog.for_files(None, [])
        dialog.destroy()

    def test_delete_songs_full(self):
        w = Gtk.Window()
        dialog = DeleteDialog.for_songs(w, [SONG])
        dialog.destroy()

    def test_delete_files_full(self):
        w = Gtk.Window()
        dialog = DeleteDialog.for_files(w, [SONG("~filename")])
        dialog.destroy()

    def test_trash_songs_full(self):
        w = Gtk.Window()
        dialog = TrashDialog.for_songs(w, [SONG])
        dialog.destroy()

    def test_trash_files_full(self):
        w = Gtk.Window()
        dialog = TrashDialog.for_files(w, [SONG("~filename")])
        dialog.destroy()

    def test_menu_item(self):
        TrashMenuItem().destroy()
