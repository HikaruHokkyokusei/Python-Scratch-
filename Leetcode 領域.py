# noinspection PyUnresolvedReferences
from collections import defaultdict, deque
from typing import Optional, List

FUNC_NAME, PARAMS = "func", []


# noinspection PyPep8Naming, PyMethodMayBeStatic
class Solution:
    def __init__(self, dummy: Optional[List] = None):
        self.dummy = dummy

    def func(self):
        pass


if __name__ == "__main__":
    print(getattr(Solution(), FUNC_NAME)(*PARAMS))
