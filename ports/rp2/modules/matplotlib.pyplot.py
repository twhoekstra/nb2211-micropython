# Format for plot is {dictionary of settings}[[x axis], [y axis]]
           
# Format for attribute is ATTRIBUTE_PREFIXattribute(parameters)

__ATTRIBUTE_PREFIX = '%matplotlib --' # Prefix to recognize attribute

def show():
    raise NotImplementedError('matplotlib.pyplot.show is not implemented yet for ALPACA.')
    
def pause():
    raise NotImplementedError('matplotlib.pyplot.pause is not implemented yet for ALPACA.')

def figure(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.figure is not implemented yet for ALPACA.')

def close(fig=None):
    """
    Close a figure window.
    """
    raise NotImplementedError('matplotlib.pyplot.close is not implemented yet for ALPACA.')

def clf():
    """Clear the current figure."""
    raise NotImplementedError('matplotlib.pyplot.clf is not implemented yet for ALPACA.')

def draw():
    raise NotImplementedError('matplotlib.pyplot.draw is not implemented yet for ALPACA.')

def savefig(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.savefig is not implemented yet for ALPACA.')


def cla():
    """Clear the current axes."""
    raise NotImplementedError('matplotlib.pyplot.cla is not implemented yet for ALPACA.')


def subplot(*args, **kwargs):
    """Add an Axes to the current figure or retrieve an existing Axes."""
    raise NotImplementedError('matplotlib.pyplot.subplot is not implemented yet for ALPACA.')


def subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True,
             subplot_kw=None, gridspec_kw=None, **fig_kw):
    """
    Create a figure and a set of subplots.
    """
    raise NotImplementedError('matplotlib.pyplot.subplots is not implemented yet for ALPACA. Instead, please use matplotib.pyplot.plot')


def xlim(*args, **kwargs):
    """
    Get or set the x limits of the current axes.
    Call signatures::
        left, right = xlim()  # return the current xlim
        xlim((left, right))   # set the xlim to left, right
        xlim(left, right)     # set the xlim to left, right
    If you do not specify args, you can pass *left* or *right* as kwargs,
    i.e.::
        xlim(right=3)  # adjust the right leaving left unchanged
        xlim(left=1)  # adjust the left leaving right unchanged
    Setting limits turns autoscaling off for the x-axis.
    Returns
    -------
    left, right
        A tuple of the new x-axis limits.
    Notes
    -----
    Calling this function with no arguments (e.g. ``xlim()``) is the pyplot
    equivalent of calling `~.Axes.get_xlim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xlim` on the current axes. All arguments are passed though.
    """
    return __ATTRIBUTE_PREFIX + 'xlim'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'

def ylim(*args, **kwargs):
    """
    Get or set the y-limits of the current axes.
    Call signatures::
        bottom, top = ylim()  # return the current ylim
        ylim((bottom, top))   # set the ylim to bottom, top
        ylim(bottom, top)     # set the ylim to bottom, top
    If you do not specify args, you can alternatively pass *bottom* or
    *top* as kwargs, i.e.::
        ylim(top=3)  # adjust the top leaving bottom unchanged
        ylim(bottom=1)  # adjust the bottom leaving top unchanged
    Setting limits turns autoscaling off for the y-axis.
    Returns
    -------
    bottom, top
        A tuple of the new y-axis limits.
    Notes
    -----
    Calling this function with no arguments (e.g. ``ylim()``) is the pyplot
    equivalent of calling `~.Axes.get_ylim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_ylim` on the current axes. All arguments are passed though.
    """
    return __ATTRIBUTE_PREFIX + 'ylim'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'

def xticks(ticks=None, labels=None, **kwargs):
    """
    Get or set the current tick locations and labels of the x-axis.
    Pass no arguments to return the current values without modifying them.
    Parameters
    ----------
    ticks : array-like, optional
        The list of xtick locations.  Passing an empty list removes all xticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.
    Returns
    -------
    locs
        The list of xtick locations.
    labels
        The list of xlabel `.Text` objects.
    Notes
    -----
    Calling this function with no arguments (e.g. ``xticks()``) is the pyplot
    equivalent of calling `~.Axes.get_xticks` and `~.Axes.get_xticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xticks` and `~.Axes.set_xticklabels` on the current axes.
    """

    kwargs['ticks'] = ticks
    kwargs['labels'] = labels
    args = ()

    return __ATTRIBUTE_PREFIX + 'xticks'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'

def yticks(ticks=None, labels=None, **kwargs):
    """
    Get or set the current tick locations and labels of the y-axis.
    Pass no arguments to return the current values without modifying them.
    Parameters
    ----------
    ticks : array-like, optional
        The list of ytick locations.  Passing an empty list removes all yticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.
    Returns
    -------
    locs
        The list of ytick locations.
    labels
        The list of ylabel `.Text` objects.
    Notes
    -----
    Calling this function with no arguments (e.g. ``yticks()``) is the pyplot
    equivalent of calling `~.Axes.get_yticks` and `~.Axes.get_yticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_yticks` and `~.Axes.set_yticklabels` on the current axes.
    """
    kwargs['ticks'] = ticks
    kwargs['labels'] = labels
    args = ()

    return __ATTRIBUTE_PREFIX + 'yticks'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'


def polar(*args, **kwargs):
    """Make a polar plot."""
    raise NotImplementedError('matplotlib.pyplot.polar is not implemented yet for ALPACA.')

def errorbar(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.errorbar is not implemented yet for ALPACA.')

def hist(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.hist is not implemented yet for ALPACA.')

def hlines(y, xmin, xmax, colors=None, linestyles='solid', label='', data=None, **kwargs):

    kwargs['colors'] = colors
    kwargs['linestyles'] = linestyles
    kwargs['label'] = label
    kwargs['data'] = data

    args = (y, xmin, xmax)

    return __ATTRIBUTE_PREFIX + 'yticks'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'

def legend(*args, **kwargs):
    return __ATTRIBUTE_PREFIX + 'yticks'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'

def loglog(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.loglog is not implemented yet for ALPACA. Please use xscale and yscale.')

def pie(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.pie is not implemented yet for ALPACA.')

def plot(*args, scalex=True, scaley=True, data=None, **kwargs):
    # Format for string is {dictionary of settings}[[x axis], [y axis]]
    xx = args[0]
    yy = args[1]

    if len(args) > 2: # add fmt string to kwargs if present:
        kwargs['fmt'] = args[2]
    else:
        kwargs['fmt'] = ''

    kwargs['scalex'] = scalex
    kwargs['scaley'] = scaley
    kwargs['data'] = data

    print(str(kwargs) + str([xx, yy]))

def scatter(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.scatter is not implemented yet for ALPACA.')

def violinplot(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.violinplot is not implemented yet for ALPACA.')

def vlines(
        x, ymin, ymax, colors=None, linestyles='solid', label='', *, data=None, **kwargs):
    args = (x, ymin, ymax)

    kwargs['colors'] = colors
    kwargs['linestyles'] = linestyles
    kwargs['label'] = label
    kwargs['data'] = data

    return __ATTRIBUTE_PREFIX + 'vlines'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  

def title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs):
    args = (label)

    kwargs['fontdict'] = fontdict
    kwargs['loc'] = loc
    kwargs['pad'] = pad
    kwargs['y'] = y

    return __ATTRIBUTE_PREFIX + 'title'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  


def xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    args = (xlabel)

    kwargs['fontdict'] = fontdict
    kwargs['labelpad'] = labelpad
    kwargs['loc'] = loc

    return __ATTRIBUTE_PREFIX + 'xlabel'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  

def ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    args = (ylabel)

    kwargs['fontdict'] = fontdict
    kwargs['labelpad'] = labelpad
    kwargs['loc'] = loc

    return __ATTRIBUTE_PREFIX + 'ylabel'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  

def xscale(value, **kwargs):
    args = (value)

    return __ATTRIBUTE_PREFIX + 'xscale'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  

def yscale(value, **kwargs):
    args = (value)

    return __ATTRIBUTE_PREFIX + 'xscale'  + '(' + str(args).replace('(','').replace(')','') + ', '+ str(kwargs) +')'  