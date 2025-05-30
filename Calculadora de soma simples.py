num1= int (input ("Digite um número: "))
num2= int ( input ("Digite outro número:"))
operacao= str (input ("escolha uma operação: "))

if operacao == "soma":
   result = int (num1) + int  (num2)
   
if operacao == "subtracao" :
    result = int (num1) - int (num2)
    
if  operacao =="multiplicacao":
    result = int (num1) * int (num2)
    
if  operacao == "divisao":
    result = int (num1) / int  (num2)
    
print  ("o resultado é " + str (result))

  
