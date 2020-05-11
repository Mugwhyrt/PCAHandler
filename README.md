Overview
========
PCA_generic.py is a python script for generic handling of CSV (comma separated value) files for 
principal component analysis. Inputs are hardcoded at the end of the file
with the following parameters
	- file_name: The name of the CSV file to be imported, must be in quotes
	   with the .csv file tag.
		ex: file_name = "file-name.csv"
	- label_target: the label type by which to label the visualized data points
	  must match the column title in the csv file EXACTLY, and be in quotes
		ex: label_target = "label_name"
	- feature_count: the number of features (dimensions) of the dataset. 
		ex: feature_count = 5
PCA_generic can be edited through any IDE or if you don't have an IDE any basic
text editor (NOT a word processor), such as notepad, should be fine as long as 
PCA_generic retains the .py file tag.

PCA_generic assumes that data in the CSV is arranged as follows:
	top row: feature_name_1,  . . . , feature_name_n, label_name_1, . . ., label_name_n
     data_set_1: feature_1,  . . . feature_n, label_1, . . ., label_n
	. . .
     data_set_2: feature_1,  . . . feature_n, label_1, . . ., label_n
or in other words:
	the top row contains the names for each dimension followed by the label categories
	the remaining rows are associated with the data sets (row 1 contains data set 1,
	row 2 contains data set 2, etc)

PCA_generic can be run either from a command line or from python's IDLE environment.
Unfortunately, matplotlib (the library used to visualise the figures) is a little wonky
when it comes to displaying figures depending on the environment in which it's run.
If running from the command line, PCA_generic should work fine as-is. If running through
IDLE, you'll just have to enter some key press to get the window to appear. Note that PCA_generic 
will run faster through the command line or terminal, this is especially important when working 
with large data sets.
	
Set-Up
======
PCA_generic requires Python 3.x which can be downloaded at python.org
(python is usually pre-installed on Mac OSx)

PCA_generic is dependent on the following libraries:
	- pandas
	- numpy
	- matplotlib
	- sklearn

These can be installed from your OS's command line/terminal with:
	python -m pip install pandas
	python -m pip install numpy
	python -m pip install matplotlib
	python -m pip install sklearn

Tutorial
========
If you want to make sure you know what you're doing, you can practice with the
iris data set. The iris data set is a set of data sorted by iris species with
various flower measurements as their dimensions. There are four dimensions in total
and the final column ("variety") is the label column. There are three different 
species included the data set.

To start, make sure that iris.csv is located in the same folder as PCA_generic.py

Open up PCA_generic and input the full file name and the number of 
features/dimensions.

There is only one label name ("variety"), because it's in quotations in the csv
you'll have to escape the quotations with a backslash like so:
	label_target = "\"variety\""

The final parameters should be entered as follows:
	file_name = "iris.csv"
	label_target = "\"variety\""
	feature_count = 4

The output image should match the included Iris_example_output.png image.

Troubleshooting
===============
If PCA_generic crashes, double-check the following:
	- all parameters are spelled correctly and match exactly what appears
	on the file name or in the csv file
	- the file name includes the ".csv" tag
	- the number for feature count matches the number of dimensions for each
	data set; ie, the number of columns for dimensions in the CSV
	- Is the file to be analyzed in the same folder as PCA_generic.py? If not
	make sure the file path is also included the file_name variable
If the output plot won't appear:
	- If in IDLE, and the window appears but won't finish loading, make sure
	some key press was entered into the IDLE terminal window
	- If running from a command line and the window won't appear (or appears but dissapears
	immediately), try running from IDLE