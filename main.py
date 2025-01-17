import os, sys, Tkinter, tkFileDialog

def dir(path):
    files = os.listdir(path)
    i = 1

    start = raw_input('Files start with: ')
    end = raw_input('\nFiles end with: ')

    for file in files:
        try:
            os.rename(path+'/'+file, path+'/'+start+str(i)+end)
        except Exception as e:
            print 'Error renaming ' + file + '\n'
            print e

        i+=1
        with open('recent.txt', 'at') as f:
            f.write(file+'\n')
    print 'Done'
    

def main():
    Tkinter.Tk().withdraw()
    fold_dir = tkFileDialog.askdirectory(initialdir=r"A:")
    dir(fold_dir)

if __name__ == '__main__':
    main()

