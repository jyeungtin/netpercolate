import matplotlib.pyplot as plt
import seaborn as sns

### Plot seaborn heatmap for dissimilarity matrices 

def plot_matrix(matrix, suptitle, title, ticks_labels, reverse = False, ax = None, vmin = 0, vmax = 1):
    '''
    Plot seaborn heatmap for dissimilarity matrices 

    ## Parameters
    matrix: numpy matrix
    suptitle: super title
    title: subtitle
    ticks_labels: a list of tick lables. 
    reverse: Whether to reverse the colour gradient `RdBu`. Default at False.
    ax: axis 
    vmin: minimum value for the color mapping. Default at 0.
    vmax: maxmimum value for the color mapping. Default at 1. 
    '''
    with plt.style.context('default'):
        if reverse is False:
            cmap = 'RdBu'
        else:
            cmap = 'RdBu_r'

        plt.figure(figsize=(12,12))
        ax = sns.heatmap(matrix, cmap = cmap, annot=True, vmin=vmin, vmax=vmax, annot_kws={"fontsize":25}, ax = ax)
        ax.set_xticklabels(ticks_labels, fontsize = 20)
        ax.set_yticklabels(ticks_labels, fontsize = 20)
        # ax.set_title(f'{title}', fontsize = 20)
        plt.xticks(rotation=90)
        plt.yticks(rotation=0)
        plt.suptitle(f'{suptitle}\n{title}', fontsize = 35)
        plt.tight_layout()

        plt.show()