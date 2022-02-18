import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots()
plt.xlim([-1, 3])
plt.ylim([0, 1000])

g = np.fromfile("group_number", sep=" ", dtype=int)
ng = []
for i in range(1,g.size):
    ng.append(g[i]-g[i-1])
# plt.scatter(range(num),[250,270,222], c="#45e688")
# plt.plot([0,1,2],[250,270,222], c="#45e688")
# "{:d}".format(x) for x in range(len(ng))]
plt.bar(["11-16", "16-22"], height=ng, color =["#45e688","#e65545"],
        width = 0.4)
ax.set_xlabel('Временной промежуток')
ax.set_ylabel('Прирост групп')
ax.set_title("Прирост групп за сегодня")
# plt.savefig('new_groups.png')
plt.show()