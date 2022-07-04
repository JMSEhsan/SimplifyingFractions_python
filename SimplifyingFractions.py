# Customizing classes, special methods

x = int(input('Enter numerator: '))

y = int(input('Enter denominator: '))


class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return str(self.top)+'/'+str(self.bottom)   
        
    def __smplf__(self):
        i = 1
        k = 0
        j = 1
        while (i <= min(self.top,self.bottom)):
            
            if(self.top % i == 0 and self.bottom % i == 0):
                top_smplf = self.top/i
                bottom_smplf = self.bottom/i  
                j *= i
                k += 1
                print('Factor '+ str(k) +' = '+ str(i))
                
            i += 1   
        print('Multiplying factor',j)      
        return Fraction(top_smplf, bottom_smplf)

f = Fraction(x, y) 
g = Fraction.__smplf__(f)

print('The fraction is: ',f)   
print('The simplfied fraction is: ',g)     