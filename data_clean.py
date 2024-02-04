import os
path = '/Users/pintojav/Downloads/personas/'
files = os.listdir(path)
print(len(files))
i=1
for file in files:
    text = str(file)
    punto=text.find(".")
    print(text[punto+1:])
    if text[punto+1:] == "jpg" or text[punto+1:] == "png" or text[punto+1:] == "jpeg":
        os.rename('/Users/pintojav/Downloads/personas/'+file,'/Users/pintojav/Downloads/personas/'+"picture_"+str(i)+".jpg")
    else:
        os.rename('/Users/pintojav/Downloads/personas/' + file,
                      '/Users/pintojav/Downloads/personas/' + str(i) + text[punto:])

    i += 1



    #os.rename(os.path.join(path, file), os.path.join(path, 'xyz_' + file + '.csv'))