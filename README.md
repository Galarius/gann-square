# gann-square

Tool to build Gann square.

### Features

* Large sizes

* Despite of regular usage in economic sphere, this program could also provide the date sequence instead of numbers. It allows to analyze the distribution of important dates.

* Visualization support (basic Gann visualization and cells highlighting)


### How to use  

To build classic Gann square:  
 
```
python gann.py -o <output file name> -s <square size>
```  
  
To build Gann square based on date:

```  
python gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark>
```  

Input date format: "dd/MM/yyyy"  
Square size = number of cells on each axis    
To highlight cells provide txt file with structure:    

```  
<date1>  
<date2>  
...
```  


### Example  

Run cmd:

```  
python gann.py -o "example/proton-m-launches.html" -a "07/04/2001" -b "19/03/2015" -m "example/marks.txt"
```  

`proton-m-launches.html` will show you all launches of 'Proton-M' for the last 14 years.


### Notes

To avoid performance issues it is recommended to build large square by chunks.
Each cell can be determined only by its position and previous cells are not required.    