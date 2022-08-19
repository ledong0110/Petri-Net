# Petri-Net
*******************************************************************************************************************************************************************************************************
To run the library, please constructing dictionary like below.												<br>					      
In key "Place", add your places with following syntax:<br> <b>"[your_named_place]": [number of holding tokens]</b> <br>												      
In key "Transitions", add your transitions with following syntax: <br> <b>"[your_named_transition]": {"in" : [list your places is preset of transitions], "out": [list your places is postset of transitions]} </b><br>
In key "Fire", this is the number of firing in sequence you wants, the model will generate the firing sequence randomly.									      <br>
*******************************************************************************************************************************************************************************************************
Here is the sample construct Petri net (The sample image in the output_image folder, or in page 21 of assignment)
<br>
```Python
{
  	"Places":{	
			"p1": 3, 
			"p2": 1, 
			"p3": 0, 
			"p4": 0  
		},
	"Transitions": { 
			"t1":{"in": ["p1", "p2"], "out": ["p3"]},
			"t2":{"in": ["p3"],"out": ["p2","p4"]},  
			}, 
	"Fire": 10
}
```
<br>

More detail, please reading file named "sample_run.py" and run it !!!
Have a wonderful time with my package :DDDDDDDDDDDDD
![Alt text](https://github.com/ledong0110/Petri-Net-HCMUT/blob/main/output_image/sample_petri_net.png?raw=true "Output")	
![Alt text](https://github.com/ledong0110/Petri-Net-HCMUT/blob/main/output_image/sample_output.png?raw=true "Output")
