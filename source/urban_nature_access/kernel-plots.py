import os

import matplotlib.pyplot as plt
import numpy

CWD = os.path.dirname(__file__)
MAXDIST = 50
TICKS = numpy.arange(0.0, MAXDIST+10, 0.25)


def plot_decay_function(
        data_array_or_dict, title, filename,
        ylabel='Weight',
        xlabel='Distance (in pixels) from greenspace'):
    fig, ax = plt.subplots()

    if isinstance(data_array_or_dict, numpy.ndarray):
        # plot each segment to ensure we plot the discontinuity correctly.
        data_array = data_array_or_dict
        ax.plot(TICKS, numpy.where(TICKS <= MAXDIST, data_array, numpy.nan),
                color='blue', linewidth=3)
        ax.plot(TICKS, numpy.where(TICKS > MAXDIST, data_array, numpy.nan),
                color='blue', linewidth=3)
    else:  # it's a dict mapping params to data.
        for clr, (label, data_array) in zip(
                'bgrk', data_array_or_dict.items()):
            ax.plot(TICKS,
                    numpy.where(TICKS <= MAXDIST, data_array, numpy.nan),
                    color=clr, linewidth=3, label=label)

        # produce a legend with the unique colors from the scatter
        plt.legend(loc='upper right')

    # TODO: plot circles for the discontinuity.

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.set_yticks(numpy.arange(0, 1.1, 0.1))
    ax.set_xticks([MAXDIST])
    ax.set_xticklabels(["$d_0$"])  # no latex needed for this!
    fig.savefig(filename)


ARRAY_DICHOTOMY = numpy.where(TICKS <= MAXDIST, 1, 0)
ARRAY_EXP = numpy.where(TICKS <= MAXDIST, numpy.e**(-TICKS/MAXDIST), 0)
ARRAY_GAUSSIAN = numpy.where(
    TICKS <= MAXDIST, ((
        numpy.e**(-(1/2)*(TICKS/MAXDIST)**2)-numpy.e**(-1/2)) /
        (1-numpy.e**(-1/2))),
    0)
ARRAY_DENSITY = numpy.where(
    TICKS <= MAXDIST, (3/4)*(1-(TICKS/MAXDIST)**2), 0)

POWER_BETA_ARRAYS = {}
for beta in (-0.1, -0.25, -0.5, -0.75):
    array = numpy.where(
        (TICKS <= MAXDIST) & (TICKS > 1),
        TICKS ** (beta),
        0)
    array[TICKS <= 1] = 1
    POWER_BETA_ARRAYS[f'$\\beta={beta}$'] = array


for name, array in [
        ('Dichotomy', ARRAY_DICHOTOMY),
        ('Exponential', ARRAY_EXP),
        ('Gaussian', ARRAY_GAUSSIAN),
        ('Density', ARRAY_DENSITY),
        ('Power', POWER_BETA_ARRAYS),
        ]:
    plot_decay_function(
        array, f'{name} Kernel',
        os.path.join(CWD, f'kernel-{name.lower()}.png'))
