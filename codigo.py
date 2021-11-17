import re


def arithmetic_arranger(problemas, resposta = False):
    
    if len(problemas) > 5:
        return 'Error: Too many problems.'
    
    operacao = ''
    numeros_iniciais = []
    numeros_finais_sinais = []
    todos_tracos = []
    resultados = []
    
    for calculo in problemas:
        calculo = calculo.strip()
        
        if re.search('^-*\d{1,4}\s*(\+|-)\s*\d{1,4}$', calculo) == None:
            retornado = ''
            
            if re.search('[a-zA-Z]', calculo) != None:
                retornado += 'Error: Numbers must only contain digits.\n'
            
            if re.search('[^+|\-|\w|\s]', calculo) != None:
                retornado += "Error: Operator must be '+' or '-'.\n"
            
            if re.search('\d{5,}', calculo) != None:
                retornado += 'Error: Numbers cannot be more than four digits.\n'
            
            if re.search('\d\s+\d', calculo) != None:
                retornado += 'Error: Coloque todos os números juntos.\n'
            
            if re.search('\+\s*\+|-\s*-|\+\s*-|-\s*\+', calculo) != None:
                retornado += 'Error: Não pode haver dois sinais seguidos.\n'
            
            return retornado
    
    for calculo in problemas:
        calculo = calculo.strip()
        numero_inicial = re.findall('^-*\d+', calculo)
        numero_inicial = numero_inicial[0]
        numero_final = re.findall('\d+$', calculo)
        numero_final = numero_final[0]
        sinal_list = list(calculo)
        
        for sinal_loop in sinal_list:
        
            if re.search('\D', sinal_loop) != None and re.search('\S', sinal_loop) != None:
                sinal = sinal_loop
        
        loop = 0
        espacamento = ''
        tracos = '--'
        
        if len(str(numero_inicial)) >= len(str(numero_final)):
            maior = len(numero_inicial)
            diferenca = maior - len(numero_final)
        else:
            maior = len(numero_final)
            diferenca = maior - len(numero_inicial)
        
        while(loop < diferenca):
            espacamento += ' '
            loop += 1
        
        loop_tracos = 0
        
        while(loop_tracos < maior):
            tracos += '-'
            loop_tracos += 1
        
        if sinal == '+':
            resultado = int(numero_inicial) + int(numero_final)
        else:
            resultado = int(numero_inicial) - int(numero_final)
        
        espacamento2 = ''
        loop = 0
        
        while(loop < (len(tracos) - len(f'{resultado}'))):
            espacamento2 += ' '
            loop += 1
        
        if len(numero_inicial) > len(numero_final):
            numeros_iniciais.append(f'  {numero_inicial}')
            numeros_finais_sinais.append(f'{sinal} {espacamento}{numero_final}')
            todos_tracos.append(f'{tracos}')
            resultados.append(f'{espacamento2}{resultado}')
        else:
            numeros_iniciais.append(f'  {espacamento}{numero_inicial}')
            numeros_finais_sinais.append(f'{sinal} {numero_final}')
            todos_tracos.append(tracos)
            resultados.append(f'{espacamento2}{resultado}')
        
        
    if resposta:
        return f'{"    ".join(numeros_iniciais)}\n{"    ".join(numeros_finais_sinais)}\n{"    ".join(todos_tracos)}\n{"    ".join(resultados)}'
    else:
        return f'{"    ".join(numeros_iniciais)}\n{"    ".join(numeros_finais_sinais)}\n{"    ".join(todos_tracos)}'
