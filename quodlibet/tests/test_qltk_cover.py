from tests import TestCase, add

from formats._audio import AudioFile
from qltk.cover import CoverImage

class TCoverImage(TestCase):
    def setUp(self): self.c = CoverImage()
    def tearDown(self): self.c.destroy()

    def test_set_song(self):
        self.c.set_song(None, AudioFile({"~filename":"woo"}))
add(TCoverImage)
