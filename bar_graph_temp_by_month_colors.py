# Author: Professor Candido
# This program displays a barr graph for the
# average temp by month in Western Massachusetts for a year
import matplotlib.pyplot as plt

def main():
    # Create lists for one year of temps for each month:

    # months along the bottom:
    bottom = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
    # Average Temp in Fahrenheit:
    heights = [19, 28, 38, 55, 65, 73, 79, 85, 68, 55, 40, 33]
    
    # Build the bar graph and colors for each of the 12 months:
    plt.bar(bottom, heights, color=('darkblue','blue','lightblue','salmon','orange','yellow','pink','red','wheat','green','lightgreen','cyan'))

    # Add a title.
    plt.title('Bar Graph Sample by Prof. C')

    # Add labels to the axes.
    plt.xlabel('Months of the Year')
    plt.ylabel('Average Temp in Fahrenheit')
  
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
