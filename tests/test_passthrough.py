from . import *


class TestPassthrough(TestCase):

    def test_basic_tasks(self):
        for raw in '''
            - Do a thing +project ^today =10min
            - [ ] @home Do a thing at home.
        '''.splitlines():
            raw = raw.strip()
            if not raw:
                continue
            task = tada.Task(raw)
            self.assertEqual(str(task), raw)
