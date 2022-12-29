# Main app file used for consolidation and readability purposes
# Program will run without this file
from ui import mainUI, main_func


try:
    mainUI()
    main_func()

except:
    print("Program execution failure")
    exit(1)

