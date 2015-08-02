from .core import Task, token_names, status_names

for symbol, name in token_names.iteritems():
    globals()[name] = symbol
for symbol, name in status_names.iteritems():
    globals()[name] = symbol
