import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def plot_heatmap(hydrocron_df, column, fig, ax, cmap='viridis'):
    """
    Plot a heatmap of a specified column over time for different nodes.
    
    Parameters
    ----------
    hydrocron_df : pd.DataFrame
        DataFrame with columns ['node_id', 'time_str', column]
    column : str
        Column name to plot (e.g., 'wse', 'width')
    fig : matplotlib.figure.Figure
        Figure object to plot on
    ax : matplotlib.axes.Axes
        Axes object to plot on
    cmap : str, optional
        Colormap to use for the heatmap. Default is 'viridis'.
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object with the heatmap.
    """
    # Reformat the DataFrame for heatmap
    pivot = (
        hydrocron_df
        .reset_index()
        .pivot(index='time', columns='node_id', values=column)
        .resample('1D')
        .mean()
        .dropna(axis=0, how='all')
    )
    pivot[pivot < 0] = np.nan

    # Create heatmap
    plt.sca(ax)
    x = mdates.date2num(pivot.index.to_pydatetime())
    y = np.flip(np.arange(len(pivot.columns)))
    X, Y = np.meshgrid(x, y)
    pcm = ax.pcolormesh(X, Y, pivot.T.values, shading='auto', cmap=cmap)

    # Format x-axis as dates
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig.autofmt_xdate()

    # Optional colorbar
    fig.colorbar(pcm, ax=ax)
    return fig