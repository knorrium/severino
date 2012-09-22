import glob
import Image
import numpy
import os

class Compare(object):

    def are_equal(self, img_a, img_b):
        if os.path.isdir(img_a) and os.path.isdir(img_b):
            return True

        img_a = Image.open(img_a)
        img_b = Image.open(img_b)

        if img_a.size != img_b.size or img_a.getbands() != img_b.getbands():
            return False
    
        s = 0
        for band_index, band in enumerate(img_a.getbands()):
            m1 = numpy.array([p[band_index] for p in img_a.getdata()]).reshape(*img_a.size)
            m2 = numpy.array([p[band_index] for p in img_b.getdata()]).reshape(*img_b.size)
            s += numpy.sum(numpy.abs(m1-m2))
            
        return s == 0

    def directories(self, dir_a, dir_b):
        """
        compares two directories and returns a list of different files
        """
        files_a = glob.glob(dir_a)
        files_b = glob.glob(dir_b)

        # check file count/names
        different_files = list(set(files_a) - set(files_b))
        if different_files != []:
            different_files

        else: 
            wrongFiles = []
            #check each file
            for file_a, file_b in zip(files_a, files_b):
                eq = self.are_equal(file_a, file_b)
                if eq == False:
                    wrongFiles.append(file_a)

            return wrongFiles
        
