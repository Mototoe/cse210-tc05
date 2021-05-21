
#life total
#Lose conditions
#draw jumper

class Jumper:
    
    
    def get_parachute(self):
        '''Draw Jumper and subtract Lines for loss of life'''
        self.lives = 4
    
        message =  (" __ \n" +

                    "/__\ \n" +

                    "\  / \n" +

                    " \/ \n" +

                    "  0 \n" +

                    " /|\ \n" +

                    " / \ \n" +

                      "\n" +

                    "^^^^^^^^ \n")
        return message

       

    def cutline(self, lives,message):
        '''remove lines from jumper based on lives left'''
        if lives == 4:
            pass



        
        