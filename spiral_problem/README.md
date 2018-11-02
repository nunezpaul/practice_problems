# Spiral Problem

For this problem, we create a spiral as seen below. The objective is given a value, determine the coordinate of the value on a grid starting from position [0,0]. There's an algorithm to quickly determine the coord but I was emphasizing speed to write over efficiency.


      	   (-1,2)		    	(2,2)
	.    [9].------>.------>.------>.[12]
	^	^			|
	|	|	      	(1,1)	v
	.	.	.----->	.[2]	.
	^	^	^       |	|
	|	|	|	v	v
	.	.	.[0]	.	.
	^	^     	(0,0)	|	|
	|	|		v	v
	.    [6].<------.<------.[4]	.
	^ (-1,-1)	     	(1,-1)	|
	|				v
    [20].<------.<------.<------.<------.[16]
  (-2,-2)				(2,-2)
