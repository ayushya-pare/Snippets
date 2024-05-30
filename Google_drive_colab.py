from google.colab import drive
drive.mount('/content/drive')

# Change directory to the dataset folder
import os
os.chdir('/content/drive/My Drive/[The Dataset to be downloaded]')

# Verify the contents
!ls
