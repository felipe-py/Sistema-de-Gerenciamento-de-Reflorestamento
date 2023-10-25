import matplotlib.pyplot as plt

def graficoestados(quant_areaba, quant_areaal, quant_areace, quant_areama, quant_areapb, quant_areape, quant_areapi, quant_arearn, quant_arease,tot_estadoba, tot_estadoal, tot_estadoce, tot_estadoma, tot_estadopb, tot_estadope, tot_estadopi, tot_estadorn, tot_estadose):
    x = ["BA", "AL", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    y1 = [tot_estadoba, tot_estadoal, tot_estadoce, tot_estadoma, tot_estadopb, tot_estadope, tot_estadopi, tot_estadorn, tot_estadose]
    y2 = [quant_areaba, quant_areaal, quant_areace, quant_areama, quant_areapb, quant_areape, quant_areapi, quant_arearn, quant_arease]
    
    plt.figure(figsize=(10,5))

    plt.subplot(121)  # ARGUMENTO => GRÁFICOS POR LINHAS, GRÁFICOS POR COLUNA E ORDEM EM RELAÇÃO AO OUTRO
    plt.bar(x,y1)
    plt.ylabel("Total area")
    plt.title("Total area reflorestada por estado")

    plt.subplot(122)
    plt.bar(x,y2)
    plt.ylabel("Numeros de areas")
    plt.title("Numero total de areas reflorestdadas por estados")

    plt.show()
