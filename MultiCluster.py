#!C:\Program Files (x86)\Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

if __name__ == '__main__':
    # establishing some base level args
    XL_Name = r"C:\Users\rolep\Documents\Naithani Lab\SDRLF_Expression_Data\tiss_table_baseline_SDRLK.csv"
    sys.argv = ['MultiCluster.py']
    Basep1Flag = True
    Log2p1Flag = True
    Log2p2Flag = True
    Corrp1Flag = False
    Corrp2Flag = False
    metrix = 'correlation'

    XL_Handle = open(XL_Name, "r")

    XL_BaseTable = pd.read_csv(filepath_or_buffer=XL_Handle, index_col=0)
    XL_BaseTable.replace(to_replace=0, value=0.1, inplace=True)
    XL_Log2Table = np.log2(XL_BaseTable)

    XL_BaseTable.replace(to_replace=0.1, value=0, inplace=True)
    XL_BaseTableNANless = XL_BaseTable.fillna(value=0)

    XL_Log2TableNANless = XL_Log2Table.fillna(value=-3)

    # grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
    # f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)

    if Basep1Flag is True:
        BaseX = sns.clustermap(XL_BaseTableNANless.transpose(),
                               metric=metrix,
                               cmap="viridis",
                               figsize=[18, 8],
                               row_cluster=False,
                               # ax=ax,
                               # cbar_ax=cbar_ax,
                               xticklabels=True,
                               cbar_kws={'label': 'TPM Values',
                                         # 'fraction': 0.05,
                                         # 'shrink': 1.0,
                                         # 'anchor': (0.5, 0.75),
                                         # 'aspect': 10,
                                         # 'panchor': (0.5, 0.75),
                                         }
                               )
        # BaseX.cax.set_visible(False)
        BaseDendroBox = BaseX.ax_row_dendrogram.get_position()
        BaseDendroBox.x0 = (BaseDendroBox.x0 + 9 * BaseDendroBox.x1) / 10
        BaseX.cax.set_position(BaseDendroBox)
        BaseX.cax.yaxis.set_ticks_position("left")
        BaseX.cax.yaxis.set_label_position("left")
        # BaseX.cax.set_aspect(10, anchor="W", adjustable="box")
        BaseX.ax_row_dendrogram.set_visible(False)
        # BaseX.ax_heatmap.set_title("SDRLK Baseline Gene Expression", fontsize=25, verticalalignment='top', pad=80)
        # BaseX.ax_heatmap.set_ylabel("Tissue Type (abbreviated)", fontsize=20)
        # BaseX.ax_heatmap.set_xlabel("UniProt ID", fontsize=20)
        BaseX.ax_heatmap.tick_params(axis='x', labelsize=8)
        '''# split axes of heatmap to put colorbar
        ax_divider = make_axes_locatable(BaseX.ax_heatmap)
        # define size and padding of axes for colorbar
        cax = ax_divider.append_axes('top', size='5%', pad='2%')
        # make colorbar for heatmap.
        # Heatmap returns an axes obj but you need to get a mappable obj (get_children)
        colorbar(BaseX.ax_heatmap.get_children()[0], cax=cax, orientation='horizontal', ticks=[0, 30, 60, 90, 120, 150])
        # locate colorbar ticks
        cax.xaxis.set_ticks_position('top')
        cax.set_label("TPM Values")'''
        plt.savefig(f"BaseX_SDRLK_111_Express_{metrix}.png",
                    bbox_inches='tight'
                    )

    if Log2p1Flag is True:
        Log2X = sns.clustermap(XL_Log2TableNANless.transpose(),
                               metric=metrix,
                               cmap="viridis",
                               figsize=[18, 8],
                               row_cluster=False,
                               xticklabels=True,
                               cbar_kws={"label": "Log2 Transformed TPM Values",
                                         }
                               )
        Log2X.ax_row_dendrogram.set_visible(False)
        Log2DendroBox = Log2X.ax_row_dendrogram.get_position()
        Log2DendroBox.x0 = (Log2DendroBox.x0 + 9 * Log2DendroBox.x1) / 10
        # Log2DendroBox.x1 -= 0.03
        print(Log2DendroBox)
        Log2X.cax.set_position(Log2DendroBox)
        Log2X.cax.yaxis.set_ticks_position("left")
        Log2X.cax.yaxis.set_label_position("left")
        Log2X.cax.set_position(Log2DendroBox)
        # Log2X.ax_heatmap.set_title("SDRLK Baseline Gene Expression", fontsize=25, pad=60)
        # Log2X.ax_heatmap.set_ylabel("Tissue Type (abbreviated)", fontsize=20)
        # Log2X.ax_heatmap.set_xlabel("UniProt ID", fontsize=20)
        Log2X.ax_heatmap.set_xlabel("")
        Log2X.ax_heatmap.tick_params(axis="x", labelsize=8)
        plt.savefig(f"Log2X_SDRLK_111_Express_{metrix}.png",
                    bbox_inches='tight'
                    )
    if Log2p2Flag is True:
        Log2X = sns.clustermap(XL_Log2TableNANless.transpose(),
                               metric=metrix,
                               cmap="viridis",
                               figsize=[18, 8],
                               xticklabels=True,
                               cbar_kws={"label": "Log2 Transformed TPM Values"}
                               )
        # Log2X.ax_row_dendrogram.set_visible(False)
        Log2DendroBox = Log2X.ax_row_dendrogram.get_position()
        Log2DendroBox.x0 = (Log2DendroBox.x0 + 9 * Log2DendroBox.x1) / 10
        # Log2DendroBox.x1 -= 0.03
        Log2DendroWid = Log2DendroBox.x1 - Log2DendroBox.x0
        Log2DendroBox.x1 = Log2X.ax_row_dendrogram.get_position().x0
        Log2DendroBox.x0 = Log2DendroBox.x1 - Log2DendroWid
        print(Log2DendroBox)
        Log2X.cax.set_position(Log2DendroBox)
        Log2X.cax.yaxis.set_ticks_position("left")
        Log2X.cax.yaxis.set_label_position("left")
        Log2X.cax.set_position(Log2DendroBox)
        # Log2X.ax_heatmap.set_title("SDRLK Baseline Gene Expression", fontsize=25, pad=60)
        # Log2X.ax_heatmap.set_ylabel("Tissue Type (abbreviated)", fontsize=20)
        # Log2X.ax_heatmap.set_xlabel("UniProt ID", fontsize=20)
        Log2X.ax_heatmap.set_xlabel("")
        Log2X.ax_heatmap.tick_params(axis="x", labelsize=8)
        plt.savefig(f"Log2X_SDRLK_111_ClusTiss_{metrix}.png",
                    bbox_inches='tight'
                    )

    if Corrp1Flag is True:
        df = XL_Log2TableNANless.corr()
        df.to_csv(path_or_buf="CorrX_SDRLK_111_Tiss_Network.csv", mode="w")
        CorrX = sns.heatmap(XL_Log2TableNANless.corr(),
                            vmin=-1,
                            cmap='coolwarm',
                            # annot=True,
                            )
        plt.savefig("CorrX_SDRLK_111_Tiss.png",
                    bbox_inches='tight'
                    )
    if Corrp2Flag is True:
        CorrXTable = XL_Log2TableNANless.transpose()
        plt.show()
        CorrX = sns.heatmap(CorrXTable.corr(),
                            vmin=-1,
                            cmap='coolwarm',
                            # annot=True,
                            )
        plt.savefig("CorrX_SDRLK_111_Express.png",
                    bbox_inches='tight'
                    )

