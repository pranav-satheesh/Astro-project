#Luca Frez-Albrecht 2016
import os



#input file path goes here
rpath = '/home/pranav/Grad Classes/Astro Project/Data/Isochrones/tmp.txt'
#rpath = '/Users/Luca/Documents/Yerkes 2016/HR Diagram Expedition/iso/dartmouth_neg2p4/tmp.txt'

#separator/header goes here
#this is sensitive to tabs and other special characters, so the exact syntax should be found by manually using readline()
#make sure that the same text is written verbatim between each isochrone, or else the program will fail
#header = '#      Z\tlog(age/yr)\tM_ini   \tM_act\tlogL/Lo\tlogTe\tlogG\tmbol    u       g       r       i       z\tint_IMF\tstage\n'
#header = '#EEP   M/Mo    LogTeff  LogG   LogL/Lo sdss_u  sdss_g  sdss_r  sdss_i  sdss_z\n'
header = '#EEP   M/Mo    LogTeff  LogG   LogL/Lo F218W   F255W   F300W   F336W   F439W   F450W   F555W   F606W   F622W   F675W   F791W   F814W   F850LP'


#output file path, name, and extension
wpath = '/home/pranav/Grad Classes/Astro Project/Data/Isochrones/'
wname = 'cmd'
ext = '.txt'



#this is the code that actually runs; hopefully you should not need to touch it
#set up
rfile = open(rpath)
indices = []
maxchar = len(rfile.read())

#reads through the rfile to create a list of indices
rfile.seek(0)
for x in range(maxchar):
    s = rfile.readline()
    if s == header:
        indices.append(rfile.tell()-len(s))
indices.append(maxchar)

#writes output files between indices
rfile.seek(indices[0])
os.chdir(wpath)
for i in range(len(indices) - 1):
    sp = rfile.read(indices[i+1] - indices[i])
    wfile = open(wname + str(i+1) + ext, 'x')
    wfile.write(sp)

print('done!')
