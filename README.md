CUHK-03 Dataset Description
===========================
This dataset is collected from The Chinese University of Hong Kong (CUHK) campus
and please refer to the CUHK regulation for using it. It contains sensitive data
and the usage should respect CUHK student's privacy.

The data is stored in MATLAB MAT file "cuhk-03.mat". 1467 identities are
collected from 5 different pairs of camera views. The "cuhk-03.mat" contains
three cells.

-   "detected" means the bounding boxes are estimated by pedestrian detector
-   "labeled" means the bounding boxes are labeled by human
-   "testsets" contains the testing protocols

Details of each are listed below.

"detected" and "labeled"
------------------------
5 x 1 cells and each contains the data collected from a pair of camera views.
Each pair of camera views consists of M x 10 cells, where M is the number of
identities. For each identity, cell 1-5 are images from one camera and cell 6-10
are images from another camera. However, some identities may have less than 10
images.

"testsets"
----------
20 x 1 cells and each contains the identities used for testing. They are
represented as a 100 x 2 matrix A, where A(i, 1) is the index of camera pair and
A(i, 2) is the index of identity.
