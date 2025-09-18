import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("string")
  elif tipo == list:
    return["lista"]
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
def a ():
    return
print(diz_o_tipo("Alô"))
print(diz_o_tipo(8))
print(diz_o_tipo(2.5))
print(diz_o_tipo({"ovo" : 0.45,
          "goiaba" : 1.20,
           "rabanete" : 2.30,
            "azeite" : 1.50 }))
print(diz_o_tipo([9,8,7,0]))
print(diz_o_tipo(len))
print(diz_o_tipo(a))