## @file
## @brief meta: система складского учёта для мастерской

from metaL import *

p = Project(
    title='''система складского учёта для мастерской''',
    about='''''') \
    | Python() \
    | Django()

p.sync()
