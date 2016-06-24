import unittest
class SimpleWidgetTsetCase(unittest.TestCase):
    def setUp(self):
        self.widget=widget('the widget')


class DefaultWidgetSizeTestCase(SimpleWidgetTsetCase):
    def runTest(self):
        self.assertEqual(self.widget.size(),(50,50),'incorrect default size')

class WidgetResizeTestCase(SimpleWidgetTsetCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(),(100,150),'wrong size after resize')
