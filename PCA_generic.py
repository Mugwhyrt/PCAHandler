#
# PCA Methods
# genericised methods for handling CSV data files
# @ZacharyRohman, Summer 2019, University of Southern Maine Chemistry Dept.
"""
TO DO
"""
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.markers as mrk

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Import CSV
# Import CSV file and return the data and labels
# PARAMS
# csv, string: name and location of CSV to be loaded
# label, string: desired label, must match label in CSV
# numPoints, int: number of data points. Determines where data ends
#   and labels start
# RETURNS
# (df, features, targets), tuple: tuple containing
#   df, pandas dataframe of data and labels
#   features, array of feature points
#   targets, array of unique labels
def ImportCSV(csv, label, numPoints):
    # import CSV as numpy array, to preserve labels, 
    mat = np.genfromtxt(csv, dtype=str, delimiter=",")
    # the column index for the desired label set
    labelCol = np.where(mat[0]==label)[0]
    if labelCol.shape[0] == 0:
        print("Caution! labelCol is {}\n".format(labelCol) +
              "Make sure that label target is properly specified")
    # separate data and desired label into new arrays
    cols = np.append(mat[0, 0:numPoints], "target")
    data = np.array(mat[1:, 0:numPoints])
    labels = mat[1:, labelCol]
    # re-append specified labels to data
    data = np.append(data, labels, axis = 1)
    # create DataFrame from data/label matrix
    df = pd.DataFrame(data, columns = cols)
    return (df, mat[0, 0:numPoints], np.unique(labels))

# Principle Component Analysis
# PARAMS
# df, DataFrame: pandas dataframe of data to be analyzed
# features, array: array of the feature types
# n_comp, int: number of components to fit to, 2 by default
# showPCs, bool: show PC weights, False by default
# RETURNS
# finalDf, DataFrame: pandas dataframe of PC analyzed data

def PCAnalysis(df, features, n_comp = 2, showPCs = False):
    # separate features
    x = df.loc[:, features].values
    # separate the target
    y = df.loc[:, ['target']].values
    # standaradize features
    x = StandardScaler().fit_transform(x)
    pca = PCA(n_components = n_comp)
    # find first two principal components
    principalComponents = pca.fit_transform(x)
    # sort principal components into a data frame
    principalDf = pd.DataFrame(data = principalComponents,
                               columns = ['principal component 1',
                                          'principal component 2'])
    # sort principal component values alongside the target labels
    finalDf = pd.concat([principalDf, df[['target']]], axis = 1)
    if showPCs:
        for f, pc1, pc2 in zip(features, pca.components_[0], pca.components_[1]):
            print("{}\t{}\t{}\n".format(f, pc1, pc2))
    return finalDf

# Visualise PCA 2D
# visualises 2 dimensional PCA results with pyplot
#
# PARAMS
# finalDf, DataFrame: pandas dataframe of PC analyzed data
# targets, array: array of the targets by which datapoints were labeled
# chartTitle, str: title of output chart
def VisualisePCA_2D(finalDf, targets, chartTitle):
    # initialize plot with labels
    fig = plt.figure(figsize = (8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title(chartTitle, fontsize = 20)

    # initialize marker colors and type
    colors = ['r', 'g', 'b', 'k']
    mark_chars = ['.', 'v', 's', '*', 'H']
    markers = []
    # create marker objects based on characters in mark_chars
    for c in mark_chars:
        markers.append(mrk.MarkerStyle(marker=c)) 
    # counter for target
    count = 0
    # for each target, plot on grid
    for target in targets:
        indicesToKeep = finalDf['target'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c = colors[count%len(colors)], marker = markers[count%len(markers)], s = 100)
        count += 1
    ax.legend(targets)
    ax.grid()
    fig.show()

if __name__ == "__main__":
    # Name of the file to be imported, must be a csv
    file_name = "GCMS_combinedData.csv"
    # the target to label by
    label_target = "Date"
    # the number of features being examined by
    feature_count = 5
    
    chart_title = "Analysis by {}".format(label_target)
    df, features, targets = ImportCSV(file_name,
                                      label_target, feature_count)
    finalDf = PCAnalysis(df, features)
    VisualisePCA_2D(finalDf, targets, chart_title)
    input("press any key to continue . . .")
            
