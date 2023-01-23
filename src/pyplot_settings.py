import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap

plt.style.use("seaborn-colorblind")
plt.rc("xtick", labelsize=11)
plt.rc("ytick", labelsize=11)
plt.rcParams.update({"font.size": 11})

top = cm.get_cmap("Blues_r", 128)
bottom = cm.get_cmap("Oranges", 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)), bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name="OrangeBlue")

color = {"Core proteome genes": newcmp(0.85), "Other proteins": newcmp(0.15)}
