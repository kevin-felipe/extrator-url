url = "http://bytebank.com/cambio?moedaOrigem=real"



indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]

url_parametro = url[indice_interrogacao+1:]
print(url_parametro)


parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor=  url_parametro[indice_valor:]
print(valor)
