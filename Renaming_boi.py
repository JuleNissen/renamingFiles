#This code rename files with given extension in it's working directory.
#14.08.2018 JuleNissen
import os

os.chdir(os.path.dirname(__file__)) #Allows file to be moved to any folder it has to work in.

#This will check EVERYTHING in listed directory!
for i in os.listdir():
    Fname, Fext = os.path.splitext(i)
    
    if Fext == ".avi":  #This will make the code look for any files with given extension.
        Fhow, Fi, Fmet, Fyour, Fmother, Fseason, Fsnr, Fepisode, Fenr = Fname.split(" ") #Will split text for all dots it finds.
        Ftitle = "{} {} {} {} {}".format(Fhow, Fi, Fmet,Fyour, Fmother)
        FsNReNR = "S{}E{}".format(Fsnr, Fenr)
        new_name = "{}-{}{}".format(Ftitle, FFsNReNR, Fext)#example: Dexter - S01E03.1080P.BluRay.x264.mp4
        os.rename(i, new_name)
        
        print("Old name: "+i+"\nNew name: "+new_name) #Prints info for old name to new name.

    else:
        print("Failure!\n '"+i+"' does not have correct extension\n")
