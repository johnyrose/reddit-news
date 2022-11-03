from enum import Enum


class SortingMethod(str, Enum):
    score = 'score'
    relative_upvotes = 'relative_upvotes'

