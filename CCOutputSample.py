
# main function
def main():

    outfile = open('PythonCodeCamp04172020.txt', 'w')

    fMooseAge = 13.95
    outfile.write("Mas" + "\n")
    outfile.write("Robert\n")
    outfile.write("Brianna\n")
    outfile.write("James\n")
    outfile.write("Lennox\n")
    outfile.write("Cory\n")
    outfile.write("Prof C\n")
    outfile.write("Adam" + "\n")
    outfile.write("Moose is: " + format(fMooseAge,"10.2f") + " years old\n")

    outfile.close()


# Call the main function.
main()


