# Matplotlib style sheets based on ggplot2

The following styles are currently available:

- **ggplot_bw**: to mimic "theme_bw" (in R)
- **ggplot_classic**: to mimic "theme_classic" (in R)

## Requirements

- Matplotlib >= 3.4.0
  - To make older versions work, *xtick.labelcolor: 4d4d4d* and *ytick.labelcolor: 4d4d4d* should be removed from the style sheets.

## Installation

Copy the style file, i.e. *ggplot_bw.mplstyle* or *ggplot_classic.mplstyle*, where your Python source codes are.

## Usage

```python
import matplotlib.pyplot as plt
plt.style.use('ggplot_bw.mplstyle') # or ggplot_classic.mplstyle
```

or

```python
import matplotlib.pyplot as plt
with plt.style.context('ggplot_bw.mplstyle'):
    # PLOTTING FUNCTION
```

## Example

You can run `example.py`, that basically generates the following results.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ggplot_palette = sns.palettes.hls_palette(n_colors=1, l=0.65, s=1.0)
sns.set_palette(palette=ggplot_palette)

def plot(title, filename):
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
    fig.savefig(filename + '.jpg', bbox_inches='tight', dpi=150)

with plt.style.context('ggplot_bw.mplstyle'):
    plot('ggplot_bw style', 'example-ggplot_bw')

with plt.style.context('ggplot_classic.mplstyle'):
    plot('ggplot_classic style', 'example-ggplot_classic')
```

![example-ggplot_bw](https://user-images.githubusercontent.com/19313488/116784350-b774e700-aa8b-11eb-8eda-deba7e4e9b93.jpg)
![example-ggplot_classic](https://user-images.githubusercontent.com/19313488/116784351-b8a61400-aa8b-11eb-8352-b56b5b855735.jpg)

## Development

Run `python3 create_mplstyle.py bw` to create *ggplot_bw.mplstyle* and `python3 create_mplstyle.py classic` to create the *ggplot_classic.mplstyle* file.
