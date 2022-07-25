Command line options
====================

The full list of the command line options for `nest` can be found below.
The options can also be displayed by running `nest -h`:


data_file
   Path to the csv file. The dataset if assumed to  
   be a csv file where there is one row per edge,   
   and each row consists of a set of columns        
   representing the source and destination, and     
   columns with the time and weight information.    

src
   Source Column(s) separated by commas (Default    
   Column 1). If multiple columns are given it will 
   construct the node ID with the combination of the
   columns                                          

dst
   Destination Column(s) separated by commas        
   (Default Column 2). If multiple columns are given
   it will construct the node ID with the           
   combination of the columns                       

weight 
   Weight Column (Default None). If this flag is set
   to None, the network is assumed to be unweighted 
   (all weights are set at 1).                      

time 
   Time Column (Default None) If this flag is set to
   None, the network is assumed to be static,       
   i.e. all no temporal information.                

output_type
   Specify the output type, current options are     
   reportlabPDF (default), pandocPDF and pandocHTML.
   The pandoc library needs to be installed to use  
   the pandoc options.                              

output_file
   Output file name, no extension needed

data_name
   Data set name (Used for presentation)      
