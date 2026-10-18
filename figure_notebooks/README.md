# Figure generation

These notebooks regenerate single-cell figures from saved analytical objects and tables. They reuse plotting cells from the analytical notebooks at the release root and do not retrain scVI or rerun inferCNV, matched-null scoring or ALRA.

| Notebook | Required analytical stage | Exports |
|---|---|---|
| [003a_Epithelial_Landscape_Figures.ipynb](003a_Epithelial_Landscape_Figures.ipynb) | 003a | Epithelial landscape, specimen origin and CNV context |
| [003b_Meta_Programme_Figures.ipynb](003b_Meta_Programme_Figures.ipynb) | 003b | Programme assignments, donor composition and transcriptional profiles |
| [003c_Antigen_Codetection_Figures.ipynb](003c_Antigen_Codetection_Figures.ipynb) | 003c | Antigen expression, raw-count diagnostics and donor co-detection |

Set `CAP_PROJECT`, select the `cap` kernel and execute the relevant figure notebook. Inputs are read from `Adata_Saves/` and `Dataframe_Saves/`; exports are written to `Publication_Figures/` at the outer project root.

Protein-association figures are exported by `Three_Proteome.ipynb` to `$CAP_PROTEOME/output/`. HPA figures are exported by 003d to `Figures/`, unless its output environment variables are set.

For selected plots inside an analytical notebook, see [plotting from saved results](../REPlot_SAVED_RESULTS.md). Plotting-only objects contain a reduced expression-gene set and must not be used to overwrite analytical H5AD files.

Final manuscript panel order is assigned during figure assembly; an analytical export's filename is not a substitute for the final figure legend.
