import cProfile
from test_sorting import test_quick_sort
import pstats
from pstats import SortKey

cProfile.run('test_quick_sort()')

# p = pstats.Stats('states')
# p.strip_dirs().sort_stats(-1).print_stats()