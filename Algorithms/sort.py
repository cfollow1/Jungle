from os.path import join, dirname, abspath
import timeit
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


reps = 100
N = [10,100,1000,10000]
results = defaultdict(list)


dir = dirname(abspath(__file__))
fpath = join(dir,'plots','SortPlot.png')
print(fpath)


for n in N:
    print(n)
    results['Tuple'].append(timeit.timeit('"-".join(str(n) for n in range(%d))'%n, number=reps))
    results['List'].append(timeit.timeit('"-".join([str(n) for n in range(%d)])'%n, number=reps))
    results['Map'].append(timeit.timeit('"-".join(map(str, range(%d)))'%n, number=reps))

plt.figure()
for result in results:
    plt.loglog(N, results[result],label=result)
plt.title('Timing')
plt.xlabel('N')
plt.ylabel('Log Time')
plt.legend()
plt.savefig(fpath)




