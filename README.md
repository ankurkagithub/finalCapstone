# Title - Shoes Inventory

# Project Description
This project provides inventory-management and stock-taking support using Python.
This will help to optimise your delivery time and improve stock organisation.

# Table of Content
1.  Installation
1. Usage
1. Credits

# 1. Installation
1. Download or fork "inventory.py" and "inventory.txt" files in a folder of your
 local computer.
1. Run this file in your chosen IDE and press on run button to execute
1. Alternatively after step 1,
    1. use your terminal > Navigate to directory where file is saved
    1. enter "python inventory.py" to run the program

# 2. Usage
1. Once you have open the terminal window, you will have options available as below.
![main options](/Pictures/menu.png) Format: ![Alt Text](url)
The file interacts with "inveontory.txt" file to save and retrive data.
Eg. on how the data is saved as below.
![Inventory File](/Pictures/inventory_txt_file.png)

1. There are 7 options to choose from in total. Name and Detail on each option is
as following.
  1. Capture new shoes data
  To add new shoes data in the databased located at _inventory.txt_
  ![Option 1](/Pictures/option_1.png)

  2. View all shoes stock
  Program reads from file _inventory.txt_ and renders data in readable format on
  terminal window. The formatting is achieved using 'tabulate' library in python.
  ![Option 2](/Pictures/option_2.png)

  3. Check low stock and restock
  This options checks the lowest stock in the database and gives you option to order
  more. You can specify the quantify you wish to order. This transverse through
  the all data saved in _inventory.txt_ file and fetches the first lowest stock count.
  If 2 stock items are lowest in the list than the first one is returned from 'inventory.txt'.
  ![Option 3](/Pictures/option_3.png)

  4. Search shoe
  Search a shoe product using appropriate shoe code. It transvere through all
  data from _inventory.txt_ file and returns the matched record.
  ![Option 4](/Pictures/option_4.png)

  If no data found, apppropriate message is printed out.
  ![Item not found](/Pictures/option_4a.png)

  5. Value per item
  It retreives all data from _inventory.txt_ and checks individual value and
  quantity for each product line. It uses this to calculate total value for each
  item.
  ![Option 5](/Pictures/option_5.png)


  6. Sale item
  Similarly to 'Check low stock', it searches for the item with highest quantity
  in '_inventory.txt' file and shows the item. Price change can be added to this feature.
  ![Option 6](/Pictures/option_6.png)

  7. Exit
  Exits the program.
![Option 7](/Pictures/option_7.png)


# 3. Credits
This project was completed by me -  Ankur Kaushal, as part of Software Engineering
Bootcamp under the supervison of HyperionDrive, part of Department of Education, UK.
