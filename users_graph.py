import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots()
plt.xlim([-1, 3])
plt.ylim([0, 300])

g = np.fromfile("new_users", sep=" ", dtype=int)
# plt.scatter(range(num),[250,270,222], c="#45e688")
# plt.plot([0,1,2],[250,270,222], c="#45e688")
plt.bar(["11-16", "16-22"], height=g, color =["#45e688","#e65545"],
        width = 0.4)
ax.set_xlabel('Временной промежуток')
ax.set_ylabel('Кол-во новых юзеров')
ax.set_title("Прирост юзеров с подпиской за сегодня")
# plt.savefig('new_users.png')
plt.show()