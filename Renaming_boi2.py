#This code rename files with given extension in it's working directory.
#14.08.2018 JuleNissen
import os

os.chdir(os.path.dirname(__file__)) #Allows file to be moved to any folder it has to work in.

#This will check EVERYTHING in listed directory!
for i in os.listdir():
    Fname, Fext = os.path.splitext(i)
    
    if Fext == ".avi":  #This will make the code look for any files with given extension.
        spaces = Fname.count(" ") #count the number of spaces in name before splitting it
        
        if (spaces == 10):
            Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr, Fdash, FepName = Fname.split(" ") #Will split text for all dots it finds.
            Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
            FsNReNR = "S{}E{}".format(Fsnr, Fenr)
            FeName = "{}".format(FepName)
            new_name = "{}-{} {}{}".format(Ftitle, FsNReNR, FepName, Fext)#example: Dexter - S01E03.1080P.BluRay.x264.mp4
            os.rename(i, new_name)
            
        if (spaces == 11):
            Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr, Fdash, FepName, FepName1 = Fname.split(" ")
            Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
            FsNReNR = "S{}E{}".format(Fsnr, Fenr)
            FeName = "{} {}".format(FepName, FepName1)
            new_name = "{}-{} {}{}".format(Ftitle, FsNReNR, FeName, Fext)
            os.rename(i, new_name)
        
        if (spaces == 12):
            Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr, Fdash, FepName, FepName1, FepName2 = Fname.split(" ")
            Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
            FsNReNR = "S{}E{}".format(Fsnr, Fenr)
            FeName = "{} {} {}".format(FepName, FepName1, FepName2)
            new_name = "{}-{} {}{}".format(Ftitle, FsNReNR, FeName,Fext)
            os.rename(i, new_name)
        
        if (spaces == 13):
            Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr, Fdash, FepName, FepName1, FepName2, FepName3 = Fname.split(" ")
            Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
            FsNReNR = "S{}E{}".format(Fsnr, Fenr)
            FeName = "{} {} {} {}".format(FepName, FepName1, FepName2, FepName3)
            new_name = "{}-{} {}{}".format(Ftitle, FsNReNR, FeName, Fext)
            os.rename(i, new_name)
        
        if (spaces == 14):
            Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr, Fdash, FepName, FepName1, FepName2, FepName3, FepName4 = Fname.split(" ")
            Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
            FsNReNR = "S{}E{}".format(Fsnr, Fenr)
            FeName = "{} {} {} {} {}".format(FepName, FepName1, FepName2, FepName3, FepName4)
            new_name = "{}-{} {}{}".format(Ftitle, FsNReNR, FeName, Fext)
            os.rename(i, new_name)
        
        else:
            print(Fname + " Does not meet the correct requirements to be handled correcly!")
        
        print("Old name: "+i+"\nNew name: "+new_name) #Prints info for old name to new name.

    else:
        print("Failure!\n '"+i+"' does not have correct extension\n")
