__author__ = 'linglin'

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        #break  #this will break the while true loop
        print "(never here if break before) if no break, you will see: ", x
        print "if run by IDE run , won't be stopped by Ctrl+C"
    except ValueError:
        print "Oops!  That was no valid numb er.  Try again..."
    finally:
        print "Finally....."