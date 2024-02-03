import os
path = '/Users/pintojav/Downloads/dataset1/train/engineer/'
files = os.listdir(path)
print(len(files))
i=1
for file in files:
    text = str(file)
    punto=text.find(".png")
    print(text[punto+1:])
    if text[punto+1:] == "jpg" or text[punto+1:] == "png" or text[punto+1:] == "jpeg":
        if text[punto+1:] == "png":
            os.rename('/Users/pintojav/Downloads/dataset1/train/engineer/'+file,'/Users/pintojav/Downloads/dataset1/train/engineer/'+"picture_"+str(i)+".jpg")
        else:
            os.rename('/Users/pintojav/Downloads/dataset1/' + file,
                      '/Users/pintojav/Downloads/dataset1/' + str(i) + text[punto:])

    i += 1



    #os.rename(os.path.join(path, file), os.path.join(path, 'xyz_' + file + '.csv'))