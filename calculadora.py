import pandas as pd
import numpy as np

def calculadora_de_montante_a_cada_periodo_de_juros_compostos(valor_inicial, taxa,
                                                              tempo_total_investimento, aporte = 0):
  
    montante_acumulado_por_periodo = []

    tempo_investido = 0

    montante_acumulado_por_periodo.append(pd.DataFrame(data = {"Acumulado": valor_inicial}, index = [0]))

    while tempo_investido < tempo_total_investimento:
        
        if tempo_investido == 0:
            
            valor_final_periodo = valor_inicial * (1 + taxa/100) + aporte

            tempo_investido = tempo_investido + 1

            montante_acumulado_por_periodo.append(pd.DataFrame(data = {"Acumulado": valor_final_periodo},
                                                               index = [tempo_investido]))
          
        else:
            
            valor_final_periodo = valor_final_periodo * (1 + taxa/100) + aporte

            valor_final_periodo = round(valor_final_periodo, 0)

            tempo_investido = tempo_investido + 1

            montante_acumulado_por_periodo.append(pd.DataFrame(data = {"Acumulado": valor_final_periodo},
                                                               index = [tempo_investido]))
            
    return pd.concat(montante_acumulado_por_periodo)



investimento_teste = calculadora_de_montante_a_cada_periodo_de_juros_compostos(valor_inicial = 5000,
                                                                               taxa = 10,
                                                                               tempo_total_investimento = 12,
                                                                               aporte = 5000)

print(investimento_teste)