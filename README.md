# Overview
Matplotlib style sheet based on ggplot

# Installation
Just copy the style file, i.e. ggplot_bw.mplstyle or ggplot_classic.mplstyle, where your Python source codes are.

# Usage
```python
import matplotlib.pyplot as plt
plt.style.use('ggplot_bw.mplstyle') # or ggplot_classic.mplstyle
```

# Example
```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ggplot_palette = sns.palettes.hls_palette(n_colors=1, l=0.65, s=1.0)
sns.set_palette(palette=ggplot_palette)


def plot1(title, filename):
    data = pd.DataFrame({
        'x': np.random.randn(50),
        'y': np.random.randn(50),
        'z': np.random.choice(['pooh', 'rabbit', 'piglet', 'Christopher'], 50),
    })

    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=data, x='x', y='y', hue='z')
    ax.set(xlabel='Label X (0123456789 test)',
           ylabel='Label Y (9876543210)', title=title)
    lgnd = ax.legend(title='Title of legend', loc='center',
                     bbox_to_anchor=(1.15, 0.5))
    lgnd._legend_box.align = "left"
    fig.savefig(filename + '.jpg', bbox_inches='tight', dpi=100)


with plt.style.context('ggplot_bw.mplstyle'):
    plot1('ggplot_bw style', 'example-ggplot_bw')

with plt.style.context('ggplot_classic.mplstyle'):
    plot1('ggplot_classic style', 'example-ggplot_classic')
```
![example-ggplot_bw.jpg](example-ggplot_bw.jpg)
![example-ggplot_classic.jpg](example-ggplot_classic.jpg)
