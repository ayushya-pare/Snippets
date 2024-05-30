from google.colab import drive
drive.mount('/content/drive')

# Change directory to the dataset folder
import os
os.chdir('/content/drive/My Drive/[The Dataset to be downloaded]')

# Verify the contents
!ls

OR

!unzip gdrive/My\ Drive/NN_Datasets/[the dataset to be downloaded in zip format].zip
