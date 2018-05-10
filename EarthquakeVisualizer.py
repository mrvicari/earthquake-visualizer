#Author: Miguel Restrepo Vicari

import urllib.request
import csv

#define function get_datalist
def getDatalist(file_name = "earthquakedata.csv"):
    #make empty list   
    earthquake = [];
    #open the file with `with` statement
    with open(file_name) as file:
        #read the file
        reader = csv.reader(file);
        #read every row
        for row in reader:
            #exclude header information
            if (row[0] == 'time'):
                continue;
            else:
                #append to earthquake list
                earthquake.append(row);
    #return list to the function        
    return earthquake;            
  
#define function get_readable_datalist
def getReadableDatalist(reader):
    #read the file
    #reader = getDatalist(file_name = "earthquakedata.csv");
    #print new header        
    print("          Time          ", " Latitude ", " Longitude  ", " Depth ", "Magnitude");
    #read every row
    for row in reader:
        #exclude header information
        if (row[0] == 'time'):
            continue;
        else:
            #print out rows 0 trhough 4
            print(row[0].rjust(24), row[1].rjust(10), row[2].rjust(12), row[3].rjust(7), row[4].rjust(6));

#define function writeHTML
def writeHTML(data):
	with open("index.html","w") as html:
		html.write("<!DOCTYPE html>\n")
		html.write("<html>\n")
		html.write("<head>\n")
		html.write("<meta charset=\"UTF-8\">\n")
		html.write("<style>\n")
		html.write("table, th, td {\n")
		html.write("border: 1px solid black;\n")
		html.write("border-collapse: collapse;\n")
		html.write("}\n")
		html.write("</style>\n")
		html.write("<title>Earthquake Data</title>\n")
		html.write("</head>\n")
		html.write("<body>\n")
		html.write("<h2 align = 'center'>Earthquake Data</h2>\n")
		html.write("<table>\n")

		html.write("<tr>\n")
		html.write("<th> Number of Earthquakes </th>\n")
		html.write("<th> Average Depth </th>\n")
		html.write("<th> Maximum Magnitude </th>\n")
		html.write("<th> Minimum Magnitude </th>\n")
		html.write("</tr>\n")
		
		html.write("<tr>")
		html.write("<td align = 'right'>" + str(numberOfQuakes(data)) + "</td>")
		html.write("<td align = 'right'>" + str(averageDepth(data)) + "</td>\n")
		html.write("<td align = 'right'>" + str(maxMagnitude(data)) + "</td>\n")
		html.write("<td align = 'right'>" + str(minMagnitude(data)) + "</td>\n")
		html.write("</tr>")
		#separate tables with blank line
		html.write("</table>\n")
		html.write("<br>&nbsp</br>\n")
		html.write("<table>\n")
		#format the header
		html.write("<tr>\n")
		html.write("<th> Time </th>\n")
		html.write("<th> Latitude </th>\n")
		html.write("<th> Longitude </th>\n")
		html.write("<th> Depth </th>\n")
		html.write("<th> Magnitude </th>\n")
		html.write("<th> Magnitude Type </th>\n")
		html.write("<th> Nst </th>\n")
		html.write("<th> Gap </th>\n")
		html.write("<th> Dmin </th>\n")
		html.write("<th> Rms </th>\n")
		html.write("<th> Net </th>\n")
		html.write("<th> ID </th>\n")
		html.write("<th> Updated </th>\n")
		html.write("<th> Place </th>\n")
		html.write("<th> Type </th>\n")
		html.write("</tr>\n")
	 
		#iterate over the rows in the data set
		for row in data:
			#exclude the header
			if (row[0] == 'time'):
				continue;
			else:
				#write the table data
				html.write("<tr>\n")            
				for i in range (0, 15):                    
					html.write("<td align = 'right'>" + row[i] + "</th>\n")
				html.write("</tr>\n")    
		#close remaining tags	
		html.write("</table>\n")
		html.write("</body>\n")
		html.write("</html>\n")


#define function numberOfQuakes
def numberOfQuakes(earthquake):
    #counter for earthquakes
    counter = 0;
    #get earthquake list with function getDatalist
    #earthquake = getDatalist("earthquakedata.csv");
    #loop over list
    for row in earthquake:
        #skip header row
        if (row[0] == "time"):
            continue;
        else:
            #if it is an earthquake
            if (row[14] == "earthquake"):
                #addd to counter
                counter += 1;
    #return counter to the function
    return counter;                

#define function averageDepth
def averageDepth(earthquake):
    #variable to keep track of depth sum
    totalDepth = 0;
    #get earthquake list with function getDatalist
    #earthquake = getDatalist("earthquakedata.csv");
    #iterate over elements in earthquake
    for each in earthquake:
        if (each[14] == "earthquake"):
            #add each depth to variable totalDepth
            totalDepth += float(each[3]);
    #averageDepth is totalDepth over numberOfQuakes
    averageDepth = totalDepth/numberOfQuakes(earthquake);
    #return average to the function
    return averageDepth;

#define function maxMagnitude
def maxMagnitude(earthquake):
    #empty lis to store all the magnitudes    
    magnitudes = [];
    #get earthquake list with function getDatalist
    #earthquake = getDatalist("earthquakedata.csv");
    #iterate over elements in earthquake
    for each in earthquake:
        if (each[4] == "mag"):
            continue;
        else:
            #append every magnitude to `magnitudes` list
            magnitudes.append(float(each[4]));
    #find maximum magnitude
    maxMagnitude = max(magnitudes);
    #iterate over elements in earthquake again
    
    return maxMagnitude;
           
#define function minMagnitude
def minMagnitude(earthquake):
    #empty lis to store all the magnitudes    
    magnitudes = [];
    #get earthquake list with function getDatalist
    #earthquake = getDatalist("earthquakedata.csv");
    #iterate over elements in earthquake
    for each in earthquake:
        if (each[4] == "mag"):
            continue;
        else:
            #append every magnitude to `magnitudes` list
            magnitudes.append(float(each[4]));
    #find minimum magnitude
    minMagnitude = min(magnitudes);
    
    return minMagnitude;

#define funcion readDataFromURL
def readDataFromURL():
    try:
        #empty list to store data  
        lines = [];
        #URL where the information is   
        url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv';
        response = urllib.request.urlopen(url);
        reader = response.read().decode('utf-8').splitlines();
        listOfLists = csv.reader(reader);
        #loop over variable
        for row in listOfLists:
            #append to empty list
            lines.append(row);
        #return list to the function         
        return lines;
    #error handling 
    except (Exception):
        print("Unable to get data from website");


#textMenu

#print title
print("Earthquake Data");
#keep list of data
data = getDatalist();
#make infinite loop
while (1):
    #print visual break
    print(" ");
    #print options
    print("Select one of the following options:");
    print("1. View earthquake data");
    print("2. View Earthquake statistics");
    print("3. Create an HTML document");
    print("4. Get latest earthquake data");
    print("5. Exit the program");
    #print visual break
    print(" ");
    #get user input and assign it to a variable
    userInput = int(input("Enter your choice: "));
    print(" ");        
    #if 1 call function getReadableDatalist to get earthquake data
    if (userInput == 1):
        getReadableDatalist(data);
    #if 2 print title and call previous functions to get statistics    
    elif (userInput == 2):
        print("Number of earthquakes:", numberOfQuakes(data));
        print("Average depth:", averageDepth(data));
        print("Maximum magnitude:", maxMagnitude(data));
        print("Minimum magnitude:", minMagnitude(data));
    #if 3 call writeHTML to create HTML document
    elif (userInput == 3):
        writeHTML(data);
        print("File `index.html` created.");
    #if 4 call getDataFromURL to retrieve latest dataset
    elif (userInput == 4):
        data = readDataFromURL();
        print("Latest dataset retrieved.");
    #if 5 break infinite loop to exit the program
    elif (userInput == 5):
        break;
    #if any other option print out error
    else:
        print("Invalid option, try again.");
