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
  
`<square size>` is a number of cells on each axis  
    
To build Gann square based on date:

```  
python gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark>
```  

Input date format: "dd/MM/yyyy"      
To highlight cells provide .json file with structure:    

``` json
[
    {
        "description": "<description>",
        "color": "<color>",
        "data_path": "<path to dates>"
    },
    {
        "description": "<description>",
        "color": "<color>",
        "data_path": "<path to dates>"
    }
]
```  

`<path to dates>` should be replaced with a path to .txt file with dates to highlight.   
Format: 

```  
<date1>  
<date2>  
...

```  

The last row should be empty.  
  
To avoid performance issues it is recommended to build large square by chunks.  
Each cell can be determined only by its position and previous cells are not required.  

To build Gann sub square based on date:  

```  
python gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark> -l <left bottom pos> -r <right up pos>
```  

Gann square has the following coordinate system inside the program:  

```  
 ____ ____ ____
|-1 1|0  1|1  1|
|-1 0|0  0|1  0|
|-1-1|0 -1|1 -1|

```  
  
So when you specify -5 for 'l' flag and 5 for 'r' flag, that will cut the center square with size: 11x11.  


### Example  

Run cmd:

```  
$ python gann.py -o "example/proton-m-launches.html" -a "07/04/2001" -b "19/03/2015" -m "example/data.json"
```  

`proton-m-launches.html` will show you successful and unsuccessful launches of 'Proton-M' for the last 14 years. 


# LICENSE
This project is licensed under the terms of the MIT license. (see LICENSE.txt in the root)
    
