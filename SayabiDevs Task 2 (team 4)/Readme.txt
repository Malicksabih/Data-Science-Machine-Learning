Download dataset from here:

https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip

After downloading, move the "Cat" and "Dog" folders out of the "PetImages" to a new folder "cats_vs_dogs", to get a simpler file path:
e.g. D:\cats_vs_dogs"

Make sure to update the dataset's path in your code according to your dataset's loaction.

###########################################################################################################################################

##For Google Colab

!wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
!unzip kagglecatsanddogs_5340.zip

##use this code to remove improper and noisy images from the data (if using colab)

