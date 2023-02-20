# can be used to sort other csv datasets
import os
import shutil
import random

seed = 1

random.seed(seed)
directory = "D:\\ISIC_2019_Training_Input"
targetMel = "D:\\NewData\\melanoma"
targetNV = "D:\\NewData\\NV"
targetBCC = "D:\\NewData\\BCC"
targetAK = "D:\\NewData\\AK"
targetBKL = "D:\\NewData\\BKL"
targetDF = "D:\\NewData\\DF"
targetVASC = "D:\\NewData\\VASC"
targetSCC = "D:\\NewData\\SCC"


train_samples = 0

for line in open("D:\\ISIC_2019_Training_GroundTruth.csv").readlines()[1:]:
    split_line = line.split(",")
    img_file = split_line[0]
    melanoma = split_line[1]
    NV = split_line[2]
    BCC = split_line[3]
    AK = split_line[4]
    BKL = split_line[5]
    DF = split_line[6]
    VASC = split_line[7]
    SCC = split_line[8]

    if int(float(melanoma)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetMel + "\\" + img_file + ".jpg"
        )
    elif int(float(NV)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetNV + "\\" + img_file + ".jpg"
        )
    elif int(float(BCC)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetBCC + "\\" + img_file + ".jpg"
        )
    elif int(float(AK)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetAK + "\\" + img_file + ".jpg"
        )
    elif int(float(BKL)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetBKL + "\\" + img_file + ".jpg"
        )
    elif int(float(DF)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetDF + "\\" + img_file + ".jpg"
        )
    elif int(float(VASC)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetVASC + "\\" + img_file + ".jpg"
        )
    elif int(float(SCC)) == 1:
        shutil.move(
            directory + "\\" + img_file + ".jpg", targetSCC + "\\" + img_file + ".jpg"
        )

print("Completed")

# end of file
