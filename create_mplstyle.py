# Author: Morteza Hosseini
# https://github.com/smortezah

"""Create matplotlib style sheets that mimic ggplot2 (R) styles."""

import sys

base_size = 11.
base_line_size = base_size / 22
base_rect_size = base_size / 22
half_line = base_size / 2
grey20 = '333333'
grey30 = '4d4d4d'
grey92 = 'ebebeb'

SUPPORTED_STYLES = ['bw', 'classic']


def gen_header(theme: str) -> str:
    """Generate header of the style sheet.

    Args:
        theme (str): theme name

    Returns:
        str: header information
    """
    return \
        f"## ggplot_{theme.lower()} matplotlib style sheet\n" \
        "## Author: Morteza Hosseini\n" \
        "## https://github.com/smortezah\n"


def backbone() -> dict:
    """Backbone of the style sheet.

    Returns:
        dict: initial settings
    """
    return {
        'font.family': 'sans-serif',
        'font.sans-serif': 'Arial',
        'font.weight': 'normal',  # 100, 200, 300, ..., 900 -> dflt: normal=400
        'font.size': base_size,
        #
        'figure.dpi': 100,
        'figure.titlesize': base_size * 1.2,
        'figure.titleweight': 'normal',
        'figure.frameon': 'False',
        'figure.facecolor': 'white',
        'figure.edgecolor': 'white',
        #
        'axes.titlesize': base_size * 1.2,
        'axes.titleweight': 'normal',
        'axes.titlelocation': 'left',
        'axes.titlepad': half_line * 2,
        'axes.labelsize': base_size,
        'axes.labelpad': half_line / 2,
        #
        'xtick.labelsize': base_size * 0.8,
        'ytick.labelsize': base_size * 0.8,
        'xtick.color': grey20,
        'ytick.color': grey20,
        'xtick.labelcolor': grey30,
        'ytick.labelcolor': grey30,
        'xtick.major.size': half_line / 2,
        'ytick.major.size': half_line / 2,
        'xtick.major.pad': half_line * 0.8 / 2,
        'ytick.major.pad': half_line * 0.8 / 2,
        #
        'legend.frameon': 'False',
        'legend.fontsize': base_size * 0.8,
        'legend.title_fontsize': base_size,
        # Dimensions as fraction of font size:
        'legend.borderpad': 0.5,
        'legend.labelspacing': 1.0,
        'legend.borderaxespad': 1.0,
        'legend.columnspacing': 2.0,
        'legend.handlelength': 1.2,
        'legend.handleheight':  1.0,
        # set('legend.handletextpad', 1.2)
    }


def bw() -> dict:
    """Settings specifically for ggplot_bw style.

    Returns:
        dict: ggplot_bw specific settings
    """
    return {
        'axes.edgecolor': grey20,
        'axes.linewidth': base_rect_size,
        'axes.grid': 'True',
        'axes.grid.axis': 'both',
        'axes.grid.which': 'both',
        'axes.axisbelow': 'True',
        #
        'grid.color': grey92,
        'grid.linewidth': base_line_size * 2,
        'grid.alpha': 1.0
    }


def classic() -> dict:
    """Settings specifically for ggplot_classic style.

    Returns:
        dict: ggplot_classic specific settings
    """
    return {
        'axes.edgecolor': 'black',
        'axes.linewidth': base_line_size * 1.5,  # ggplot2 dflt: base_line_size
        'axes.spines.top': 'False',
        'axes.spines.right': 'False',
        'axes.grid': 'False'
    }


def gen_save_mplstyle(style: str) -> None:
    """Generate and save the matplotlib style sheet.

    Args:
        style (str): style name
    """
    dict = {}
    dict.update(backbone())
    if style == 'bw':
        dict.update(bw())
    elif style == 'classic':
        dict.update(classic())

    result = gen_header(style)

    parts = ['font', 'figure', 'axes', 'tick', 'legend', 'grid']
    for part in parts:
        result += f'\n## {part.upper()}\n'
        for key in sorted(dict):
            if part in key.split('.')[0]:
                result += f'{key}: {str(dict[key])}\n'

    with open(f'ggplot_{style}.mplstyle', 'w') as output:
        output.write(result)


if __name__ == '__main__':
    style = sys.argv[1].lower()
    if style in SUPPORTED_STYLES:
        gen_save_mplstyle(style)
    else:
        raise ValueError(f"\"{sys.argv[1]}\" style not supported.")
