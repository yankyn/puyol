__author__ = 'USER'


class PuyolQuery(object):
    def __init__(self, q, cls, *criteria, **kwargs):
        self._q = q
        self._cls = cls
        self._q = self._refine(*criteria, **kwargs)

    def _refine(self, *criteria, **kwargs):
        new_q = self._q.filter(*criteria)
        new_q = new_q.filter_by(**kwargs)
        return new_q

    def refine(self, *criteria, **kwargs):
        return PuyolQuery(self._q, self._cls, *criteria, **kwargs)

    def first(self):
        return self._q.first()

    def join(self, join_object):
        return PuyolQuery(self._q.join(join_object), self._cls)

    def __len__(self):
        return self._q.count()

    def __repr__(self):
        return '<%d %s objects>' % (len(self), self._cls.__name__)
