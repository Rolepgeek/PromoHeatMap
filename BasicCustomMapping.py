#!C:\Program Files (x86)\Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

if __name__ == '__main__':
    # establishing some base level arguments; what the name is and what the filename we want is
    XL_Name = r"C:\Users\rolep\Documents\Naithani Lab\SDRLK_Expression_Data\Abiotic Data\submergence-02.xlsx"
    sys.argv = ['BasicCustomMapping.py']

    # This section is what we use to read in the data, depending on how it's oriented/located in the file we're reading
    # from
    # usecollist = range(21)
    df_Custom = pd.read_excel(XL_Name,
                              index_col=0,
                              na_values="",
                              # usecols=usecollist,
                              # skiprows=4,
                              # nrows=41,
                              )
    # For clustermaps, this is used to deal with the NA entries (where no data is available) in differential expression
    # by changing them to 0.
    df_Custom.fillna(value=0, inplace=True)
    # For heatmaps, we have to define the figure size before we make the figure.
    # f, ax = plt.subplots(figsize=(7, 10))
    # This is the actual part where we run the program.
    ax = sns.clustermap(data=df_Custom,
                        metric='correlation',  # the sort of distance measure we're using to cluster wth.
                        # vmin=-1,  #  sets the lowest value of the color mapping
                        center=0.0,  # Sets the center point of the color mapping to a specific value
                        # robust=True,
                        col_cluster=False,  # Code for do we want to cluster the columns or not
                        figsize=(7, 10),  # desired size for the figure to be for clustermaps only
                        cmap='RdBu_r',  # the color palette we're using for the colormap - RdBu_r means Red is high,
                        # blue is low
                        xticklabels=True,
                        annot=False,  # Whether or not we want the values for each box labeled.
                        cbar_kws={  # 'use_gridspec': False,
                                  # 'location': "top",
                                  'label': 'Fold Change',  # the label for the colormap
                                  'orientation': 'horizontal',  # the direction we want the colormap's gradient to be
                                  # aligned along
                        }
                        )
    # This section is what we used in clustermaps when we want to move the colorbar and only cluster along one axis.
    ax.ax_col_dendrogram.set_visible(False)
    BaseDendroBox = ax.ax_col_dendrogram.get_position()
    BaseDendroBox.y1 = (BaseDendroBox.y1 + 6 * BaseDendroBox.y0) / 7
    ax.cax.set_position(BaseDendroBox)
    # This section is setting the labels for the colorbar
    ax.cax.xaxis.set_ticks_position("top")
    ax.cax.xaxis.set_label_position("top")
    ax.cax.set_position(BaseDendroBox)
    # This is where we set the size of the labels on the graph and save it to a specified file.
    ax.ax_heatmap.tick_params(axis='x', labelsize=8)
    plt.savefig("BasicClusterMap_Submerge2-apr-17-2020.png",
                bbox_inches='tight'
                )
