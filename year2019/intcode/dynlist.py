# Written by Paul Seeb
# Jun 29, 2012
# See https://stackoverflow.com/a/11265571


class DynList(list):
    def __getitem__(self, index):
        if isinstance(index, int):
            self._expand(index)
            return super(DynList, self).__getitem__(index)

        elif isinstance(index, slice):
            print(index.stop)
            if index.stop < index.start:
                return super(DynList, self).__getitem__(index)
            else:
                self._expand(
                    index.stop
                    if abs(index.stop) > abs(index.start)
                    else index.start
                )
            return super(DynList, self).__getitem__(index)

        else:
            raise TypeError(
                f"list indices must be integers or slices, not {type(index)}"
            )

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self._expand(index)
            return super(DynList, self).__setitem__(index, value)

        elif isinstance(index, slice):
            if index.stop < index.start:
                return super(DynList, self).__setitem__(index, value)
            else:
                self._expand(
                    index.stop
                    if abs(index.stop) > abs(index.start)
                    else index.start
                )
            return super(DynList, self).__setitem__(index, value)

        else:
            raise TypeError(
                f"list indices must be integers or slices, not {type(index)}"
            )

    def _expand(self, index):
        rng = []
        if abs(index) > len(self) - 1:
            if index < 0:
                rng = range(abs(index) - len(self))
            else:
                rng = range(abs(index) - len(self) + 1)
        for i in rng:
            self.append(0)
