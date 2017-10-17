import os

import sublime, sublime_plugin


class TADAEvents(sublime_plugin.EventListener):
    
    def on_load(self, view):

        name = view.file_name()
        if not name:
            return

        name = name.lower()
        if not name.endswith('.txt'):
            return

        parts = name.lower().split(os.path.sep)
        if 'todo' not in parts:
            return

        print('[TADA]: Setting syntax.')
        view.set_syntax_file('Packages/TADA/TADA.tmLanguage')


