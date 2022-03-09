#import os library
import os

# function to rename files
def main():
    i = 0
    #path of the folder that contains the files
    path = "Directory Path.../"

    #loop through the folder an rename each file
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest

        #call to the rename method
        os.rename(my_source, my_dest)
        i += 1

#call to function when app is ran
if __name__ == '__main__':
    main()

