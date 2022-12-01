# Author: Professor Candido
# This program displays a simple line graph for the
# average temp by month in Western Massachusetts for a year
import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point
    # for one year of temps for each month:

    # months:
    x_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
    # Average Temp in Fahrenheit:
    y_coords = [19, 28, 38, 55, 65, 73, 79, 85, 68, 55, 40, 33]
    
    # Build the line graph with a square marker
    plt.plot(x_coords, y_coords, marker='s')

    # Add a title.
    plt.title('Line Graph Sample by Prof. C')

    # Add labels to the axes.
    plt.xlabel('Months of the Year')
    plt.ylabel('Average Temp in Fahrenheit')

    # Set the axis limits.
    plt.xlim(xmin=-1, xmax=12)
    plt.ylim(ymin=-1, ymax=90)
    # Set the x axis tick marks:
    plt.xticks(
                [0,1,2,3,4,5,6,7,8,9,10,11],
                ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
              )
    

    # Add a grid.
    plt.grid(True)

    # Display the line graph.
    plt.show()

# Call the main function.
main()
