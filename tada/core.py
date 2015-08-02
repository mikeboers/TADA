# encoding: utf8

import collections
import re


token_names = {
    '!': 'PRIORITY',
    '@': 'CONTEXT',
    '#': 'TAG',
    '_': 'GOAL',
    '+': 'GROUP',
    '-': 'PROJECT',
    '.': 'PARENT',
    '/': 'CATEGORY',
    '=': 'DURATION',
    '^': 'DUE',
    '%': 'REPEAT',
}

token_re = re.compile(r'''
    (?:^|(?<=\s)) # start, or after a space
    ([%s]) # (1) the token symbol
    (      # (2)
        (?: # space content
            (["']) # (3)
            .+?
            \3
        )|
        \S+ # non-space content
    )
''' % re.escape(''.join(token_names)), re.VERBOSE)


status_names = {
    '-': 'INCOMPLETE',
    '√': 'COMPLETE',
    'x': 'CANCELLED',
    '~': 'DEFERRED',
}

status_re = re.compile('[%s]' % re.escape(''.join(status_names)))


class Token(collections.namedtuple('Token', ('symbol', 'content'))):
    
    def __str__(self):
        if re.search(r'\s', self.content):
            quote = "'" if '"' in self.content else '"'
            return '%s%s%s%s' % (self.symbol, quote, self.content, quote)
        else:
            return '%s%s' % (self.symbol, self.content)


class Headline(list):

    def __init__(self, input_):
        if not isinstance(input_, basestring):
            raise TypeError('Headline requires str; got %s' % input_.__class__.__name__)
        input_ = token_re.split(input_)
        start = input_.pop(0)
        if start:
            self.append(start)
        while input_:
            symbol, content, _, text = input_[:4]
            input_[:4] = ()
            self.append(Token(symbol, content))
            if text:
                self.append(text)

    def __str__(self):
        return ''.join(str(x) for x in self)

    def get_tokens(self, symbol):
        return [t for t in self if isinstance(t, Token) and t.symbol == symbol]


class Task(object):

    def __init__(self, input_, allow_implicit_start=True):

        if not isinstance(input_, basestring):
            raise TypeError("Task requires str; got %s" % input_.__class__.__name__)

        self.prefix, self.status, self.is_implicit, headline = self._parse_status(input_)
        if self.is_implicit and not allow_implicit_start:
            raise ValueError('implicit start when not allowed')

        self.headline = Headline(headline)

    @classmethod
    def _parse_status(cls, input_):

        m = re.match(r'''
            (\s*) # leading space
            (?:
                (%s) # implicit start
                | - [ ] \[([ ]|%s)\] # explicit start
            )
        ''' % (status_re.pattern, status_re.pattern), input_, re.VERBOSE)

        if not m:
            raise ValueError('not a task')

        space, implicit, explicit = m.groups()
        headline = input_[m.end():]
        return space, implicit or explicit, bool(implicit), headline

    def __str__(self):

        parts = [
            self.prefix,
        ]
        if self.is_implicit:
            parts.append(self.status)
        else:
            parts.append('- [%s]' % (self.status))

        parts.append(self.headline)

        return ''.join(str(x) for x in parts)

