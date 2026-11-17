import numpy
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

# Source - https://stackoverflow.com/a/33382750
# Posted by BlivetWidget, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-19, License - CC BY-SA 4.0

import matplotlib.pyplot as plt

# plt.hlines(y, xmin, xmax, colors, linestyles)
plt.hlines(y=0.45, xmin=0.0, xmax=0.6, color='r', linestyle='-')
plt.hlines(y=0.25, xmin=0.0, xmax=0.6, color='r', linestyle='-')

# Same logic applies for vlines if you want to shorten vertical lines:
# plt.vlines(x, ymin, ymax, colors, linestyles)
plt.vlines(x=0.2, ymin=0.0, ymax=0.6, color='r', linestyle='-')
plt.vlines(x=0.45, ymin=0.0, ymax=0.6, color='r', linestyle='-')

plt.xticks([])
plt.yticks([])




plt.show()