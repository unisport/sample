###Fork me and send back a pull request 

Write a commandline script that takes a file system path as the first argument and one or more keywords arguments. 
 
####Arguments

1.  Required: count=integer
2.  Optional Boolean keywords: women, kid 
3.  Optinal keyword: display which takes an array of field names, to be printed out (default is only name)
4.  Optional keyword: price=asc, price=desc  

**Usage**:
  
 
        python myscript.py data.json price=dsc kid=True display=[name, price, size]  count=10
        
        python myscript.py data.json women=True display=[name, color] count=5
    
**Remember to test  
Remember to document (why, not how)
**

####Bonus:
Extend to be a reusable module, that also accepts a URL
	
	import mymodule
	mymodule('http://localhost/data.json', price='dsc', kid='True', display=['name', 'price'], count=10)

