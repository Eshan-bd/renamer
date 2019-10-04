import os, sys, Tkinter, tkFileDialog

def dir(path):
    folders = os.listdir(path)
    print path
    i = 0
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    start = raw_input('Files start with: ')
    end = raw_input('\nFiles end with: ')
    
    for folder in folders:
        files = os.listdir(path+'/'+folder)
        for n in range(10, len(files)+1): files.remove(str(n)+'.jpg')

        for file in files:
            try:
                print file
                os.rename(path+'/'+folder+'/'+file, path+'/'+folder+'/'+'0'+file+end)
            except Exception as e:
                print 'Error renaming ' + file + '\n'
                print e

            i+=1
            with open('recent.txt', 'at') as f:
                f.write(file+'\n')
        i = 0
        print 'Done'
    

def main():
    Tkinter.Tk().withdraw()
    fold_dir = tkFileDialog.askdirectory(initialdir=r"A:")
    dir(fold_dir)

if __name__ == '__main__':
    main()

