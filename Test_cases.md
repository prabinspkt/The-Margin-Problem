## Test case 1:
Left Margin: 10
Right Margin: 15
Input Text: 
Helena, the daughter of a famous doctor, has been the ward of the Countess of Rousillon, a wise and kindly old noblewoman, since her father's death. The Countess' husband has also recently died, and her son Count Bertram, a brave, handsome, but callow young man, is sent to serve the King of France, his liege lord. (The King, we learn, is dying).

Bertram arrives at the King's court, where the cautious monarch has recently decided to stay out of a war involving Austria and the Duke of Florence--with the caveat that any French noblemen who wish to involve themselves in the conflict are free to go. Greeting Bertram, the King laments the loss of the young man's father, and then remarks that he wishes Helena's father were still living, because only such a great doctor could now save his life.

Output Text:
          Helena, the daughter of a famous doctor, has been the                 
          ward of the Countess of Rousillon, a wise and kindly                  
          old noblewoman, since her father's death.  The                        
          Countess' husband has also recently died, and her son                 
          Count Bertram, a brave, handsome, but callow young man,               
          is sent to serve the King of France, his liege lord.                  
          (The King, we learn, is dying).
          
          Bertram arrives at the King's court, where the cautious               
          monarch has recently decided to stay out of a war                     
          involving Austria and the Duke of Florence--with the                  
          caveat that any French noblemen who wish to involve                   
          themselves in the conflict are free to go.  Greeting                  
          Bertram, the King laments the loss of the young man's                 
          father, and then remarks that he wishes Helena's father               
          were still living, because only such a great doctor                   
          could now save his life. 


## Test case 2:
Left Margin: 5
Right Margin: 25
Input Text: 
An          ongoing      challenge      within     the     Python       3     series     has      been    determining      a     sensible       default    strategy for handling the “7-bit ASCII” text encoding assumption     currently implied by the use of the default C or POSIX locale on       non-Windows platforms.

PEP 538 updates the default interpreter command line interface to automatically coerce that locale to an available UTF-8 based locale as described in the documentation of the new PYTHONCOERCECLOCALE environment variable.

Output Text:
     An ongoing challenge within the Python 3 series                            
     has been determining a sensible default strategy                           
     for handling the “7-bit ASCII” text encoding                               
     assumption currently implied by the use of the                             
     default C or POSIX locale on non-Windows                                   
     platforms.
     
     PEP 538 updates the default interpreter command                            
     line interface to automatically coerce that locale                         
     to an available UTF-8 based locale as described in                         
     the documentation of the new PYTHONCOERCECLOCALE                           
     environment variable.


## Test case 3:
Left Margin: 15
Right Margin: 10
Input Text: <empty file name sent as input>
Some text.

Output (Console):
Please enter non-empty values.


## Test case 4:
Left Margin: -10
Right Margin: 15
Input Text: 
Some Text.

Output (Console):
Please enter positive margins.

## Test case 4:
Left Margin: 40
Right Margin: 35
Input Text: 
Some Text.

Output (Console)):
Please decrease your margins. 