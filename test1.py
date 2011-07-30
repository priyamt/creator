import re,subprocess,shlex,os,sys
from subprocess import call

choice = '1'
while(choice == '1' or choice == '2' or choice == '3'):
    print "Select your option\n1.New article\n2.Update existing\n3.View an article\n4.Exit"
    choice = raw_input()
    if choice == '1':
        print "Enter the article title"
        head = raw_input()
        print "Enter article"
        article = raw_input()
        saved_file = open(head + '.text','w')
        saved_file.write(article)
        saved_file.close()
        print "File successfully created"

    elif choice == '2':
        dirname = os.path.dirname(os.path.realpath('test1.py'))
        paths = os.listdir(dirname)
        print "Articles available for editing are : "
        for fname in paths:
            if fname == 'test1.py':
                continue
            else:
                print fname
        print "Enter the article title which is listed above"
        head = raw_input()
        for fname in paths:
            if fname == head :
                print "Enter article"
                article = raw_input()
                update_file = open(head,'w')
                update_file.write(article)
                update_file.close()
                print "Successfully updated"
                break
        else:
            print "No such file"
            break

    elif choice == '3':
        dirname = os.path.dirname(os.path.realpath('test1.py'))
        paths = os.listdir(dirname)
        print "Articles available for viewing are : "
        for fname in paths:
            if fname == 'test1.py':
                continue
            else:
                print fname
        print "Enter the article title which is listed above"
        head = raw_input()
        for fname in paths:
            if fname == head :
                call(["cat",head])
                break
        else:
            print "No such file"
            sys.exit(0)

    elif choice == '4':
        print"Thank You"
        sys.exit(0)

    else:
        print "Wrong choice!!!"
