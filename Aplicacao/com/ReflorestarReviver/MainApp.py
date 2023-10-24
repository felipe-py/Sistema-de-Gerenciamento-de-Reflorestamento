'''/**********************************************************************************
Autor: Luis Felipe Cunha Silva
Componente Curricular: MI algoritmos 
Concluido em:25/09/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum 
trecho de código de colega ou de outro autor, tais como provindos de livros e apostilas
, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra
autoria que não a minha está destacado com uma citação do autor e a fonte do código, e estou 
ciente que estes trechos não serão considerados para fins de avaliação.
/*************************************************************************************'''

#Variáveis que realizarão a contagem da área replantada por estado, sendo descrita como
#total estado + sigla do estado nordestino.
tot_estadoba = 0;tot_estadose = 0;tot_estadoal = 0;tot_estadope = 0;tot_estadopb = 0;tot_estadorn = 0;tot_estadoce = 0;tot_estadoma = 0;tot_estadopi = 0

#Variável que fará a contagem da área total replantada em toda a região nordeste.
tot_nordeste = 0

#Variáveis que realizarão a contagem da área total replantada para cada tipo de árvore
#sendo descrita como total + árvore selecionada.
tot_cajueiro = 0;tot_mangueira = 0;tot_dende = 0;tot_coqueiro = 0;tot_bambugigante = 0;tot_ipe = 0

#Variáveis que realizarão a contagem da quantidade de vezes que um tipo de árvore foi utilizada
#para replantar uma área.
quant_cajueiro = 0;quant_mangueira = 0;quant_dende = 0;quant_coqueiro = 0;quant_bambugigante = 0;quant_ipe = 0

#Grupo de variáveis que armazenam as informações da maior área cadastrada.
maior_area = 0;cidade_maior = 0;estado_maior = 0;codigo_maior = 0;arvore_maior = 0

#Variáveis que realizarão a contagem da quantidade de áreas replantadas por estado, sendo descrita como
#quantidade de áreas + sigla do estado selecionado.
quant_areaba = 0;quant_areace = 0;quant_arearn = 0;quant_areaal = 0;quant_areapb = 0;quant_areape = 0;quant_arease = 0;quant_areapi = 0;quant_areama = 0

#Apresentação do programa, com início do menu de opções onde o usuário poderá escolher entre cadastrar uma
#área, visualizar relatório(Caso não exista um relatório pronto, o usuário será avisado), além da opção de 
#saída do programa.
print('===PROGRAMA PARA CADASTRO DE AREAS REFLORESTADAS NO NORDESTE===')
print(" "*20,"'REFLORESTAR E REVIVER!'")
print(" "*19,'SELECIONE UMA OPCAO ABAIXO')

cadastro = 1

#O while abaixo permite que o usuário rotacione o cadastro enquanto desejar, além de não permitir que seja
#escolhida uma opção que não foi apresentada no menum, como opção de saída caso o usuário digite 3, o 
#programa será encerrado.
while cadastro != '3':
    
    print('\n1',  "- CADASTRAR UMA AREA\n2 - ACESSAR RELATORIO\n3 - FECHAR PROGRAMA\n" )
    cadastro = input('escolha uma opcao:\n')

#Caso o usuário escolha a opção 1 ele será redirecionado para a aba de cadastro da área reflorestada.
    if cadastro == '1':
        print('==REALIZAREMOS AGORA O CADASTRO DA AREA REFLORESTADA==')
        print(" "*5,'==CADASTRAREMOS A DIMENSAO DA AREA==\n')
        
#As variáveis abaixo servem para iniciar o while que rotaciona o cadastro das medidas da área, escolha do estado 
#e da árvore.
        lado1 = 0;lado2 = 0;estado = 0;arvore = 0
        
#O while abaixo controla o menu de cadastro da dimensão da área, funcionando de forma que o usuário permaneça
#no mesmo ponto caso escolha uma opção inválida.
        while lado1 <= 0 or lado2 <= 0:
            print("\nAVISO:CASO DIGITE UMA MEDIDA INVALIDA, OU SEJA, MENORES OU IGUAIS A ZERO O PROGRAMA RETORNARA A PERGUNTA.\n")
            lado1 = float(input("Digite o comprimento da area: "))
            lado2 = float(input("Digite a largura da area: "))
        print("\n"," "*10,'ESCOLHA O ESTADO\n')
        print('1-BAHIA\n2-SERGIPE\n3-ALAGOAS\n4-PERNAMBUCO\n5-PARAIBA\n6-RIO GRANDE DO NORTE\n7-CEARA\n8-MARANHAO\n9-PIAUI\n')
        
#Abaixo, está presente o while responsável por controlar o menu de escolha do estado onde a área reflorestada 
#está localizada, permitindo apenas que o usuário passe para a próxima etapa do cadastro caso escolha uma opção
#válida.
        while estado != '1' and estado != '2' and estado != '3' and estado != '4' and estado != '5' and estado != '6' and estado != '7' and estado != '8' and estado != '9':
            print("\nAVISO:CASO ESCOLHA UMA OPCAO NAO LISTADA ACIMA, O PROGRAMA RETORNARA A PERGUNTA\n")
            estado = input('Escolha a opcao que representa o estado desejado:\n')
        
#caso o usuário tecle enter deixando a entrada da cidade em branco, um while o retornará para a pergunta, evitando
#falhas no relatório.
        cidade = input("\nEm qual cidade a area cadastrada esta localizada: ")
        while cidade == "":
            cidade = input("(NAO DEIXE O ESPACO EM BRANCO)-Em qual cidade a area cadastrada esta localizada: \n")
        print(' '*10,'\nESCOLHA A ARVORE USADA NO REPLANTIO\n')
        print('1-CAJUEIRO\n2-MANGUEIRA\n3-DENDE\n4-COQUEIRO\n5-BAMBU GIGANTE\n6-IPE\n')
        
#Abaixo, está presente o while responsável por controlar o menu de escolha do estado onde a área reflorestada 
#está localizada, permitindo apenas que o usuário passe para a próxima etapa do cadastro caso escolha uma opção
#válida.
        while arvore != '1' and  arvore != '2' and arvore != '3' and arvore != '4' and arvore != '5' and arvore != '6':
            print("AVISO:CASO ESCOLHA UMA OPCAO NAO LISTADA ACIMA, O PROGRAMA RETORNARA A PERGUNTA")
            arvore = input('\nEscolha a opcao que representa a arvore desejado:\n')
        
#caso o usuário tecle enter deixando a entrada da cidade em branco, um while o retornará para a pergunta, evitando
#falhas no relatório.
        codigo = input("\nCrie um codigo para a area cadastrada: ")
        while codigo == '':
            codigo = input("(NAO DEIXE O ESPACO EM BRANCO)-Crie um codigo para a area cadastrada: ")

#Após a finalização do cadastro, o programa realizará todas as somas e comparações necessárias para a criação
#do relatório, iniciando com a variavel tot_nordeste recebendo os valores das áreas replantadas, além de 
#adcionar este valor ao total de área replantada do estado e árvore selecionados no menu, tambem será adcionado
#um contador +1 contabilizando a quantidade de área cadastradas no estado e árvore selecionados.
        area_replantada = lado1 * lado2
        tot_nordeste += area_replantada
        if estado == '1':
                tot_estadoba += area_replantada
                quant_areaba += 1
        elif estado == '2':
                tot_estadose += area_replantada
                quant_arease += 1
        elif estado == '3':
                tot_estadoal += area_replantada
                quant_areaal += 1
        elif estado == '4':
                tot_estadope += area_replantada
                quant_areape += 1
        elif estado == '5':
                tot_estadopb += area_replantada
                quant_areapb += 1
        elif estado == '6':
                tot_estadorn += area_replantada
                quant_arearn += 1
        elif estado == '7':
                tot_estadoce += area_replantada
                quant_areace += 1
        elif estado == '8':
                tot_estadoma += area_replantada
                quant_areama += 1
        elif estado == '9':
                tot_estadopi += area_replantada
                quant_areapi += 1
        if arvore == '1':
                quant_cajueiro +=1
                tot_cajueiro += area_replantada
        elif arvore == '2':
                quant_mangueira +=1
                tot_mangueira += area_replantada
        elif arvore == '3':
                quant_dende +=1
                tot_dende += area_replantada
        elif arvore == '4':
                quant_coqueiro +=1
                tot_coqueiro += area_replantada
        elif arvore == '5':
                quant_bambugigante +=1
                tot_bambugigante += area_replantada
        elif arvore == '6':
                quant_ipe +=1
                tot_ipe += area_replantada

#Condicional que realiza a comparação para armazenar as informações da maior área cadastrada, como limitação 
#do código caso exista duas ou mais áreas empatadas com o maior valor, apenas uma será selecionada para 
#registro no relatório.
        if area_replantada > maior_area:
                maior_area = area_replantada
                codigo_maior = codigo
                estado_maior = estado
                cidade_maior = cidade
                arvore_maior = arvore

#Caso a opção de cadastro no menu pricipal seja a visualização do relatório, uma condicional fará a verificação
#da existência de áreas cadastradas pelo total de área reflorestda no nordeste, se esta for igual a zero, o 
#usuário será avisado.
    elif cadastro == '2':
        if tot_nordeste == 0:
            print('Nenhuma area foi cadastrada para gerar o relatorio.')

#Com a existência de áreas cadastradas o relatório será gerado normalmente.
#Para deixar a visualização mais agradável os prints que mostram a área total de uma árvore ou estado, estão 
#formatados com uma limitação de duas casas decimais.
        else:
            print('\nAREA TOTAL POR ESTADO:\n')
            print('{:.2f} m² na Bahia\n{:.2f} m² no Alagoas\n{:.2f} m² no Ceara'.format(tot_estadoba,tot_estadoal,tot_estadoce))
            print('{:.2f} m² no Maranhao\n{:.2f} m² na Paraiba\n{:.2f} m² no Pernambuco'.format(tot_estadoma,tot_estadopb,tot_estadope))
            print('{:.2f} m² no Piaui\n{:.2f} m² no Rio Grande do Norte\n{:.2f} m² no Sergipe'.format(tot_estadopi,tot_estadorn,tot_estadose))
            print('\nAREA REFOLRESTADA EM TODA REGIAO NOREDESTE: {:.2f} m²\n'.format(tot_nordeste))
            print('AREA TOTAL POR ARVORE:\n')
            print('{:.2f} m² de cajueiro\n{:.2f} m² de mangueira\n{:.2f} m² de dende'.format(tot_cajueiro, tot_mangueira, tot_dende))
            print('{:.2f} m² de coqueiro\n{:.2f} m² de bambu gigante\n{:.2f} m² de ipe\n'.format(tot_coqueiro, tot_bambugigante, tot_ipe))
            
#Em caso de empate na quantidade de uso das árvores, será feira uma verificação com todas as variáveis contadoras 
#das árvores para evitar uma informação repetida na parte do relatório que contempla as árvores mais e menos 
#utilizadas.
            if  quant_cajueiro == quant_mangueira and quant_cajueiro == quant_bambugigante and quant_cajueiro == quant_ipe and quant_cajueiro == quant_dende and quant_cajueiro == quant_coqueiro:
                if quant_mangueira == quant_cajueiro and quant_mangueira == quant_dende and quant_mangueira == quant_coqueiro and quant_mangueira == quant_bambugigante and quant_mangueira == quant_ipe:
                    if quant_dende == quant_cajueiro and quant_dende == quant_ipe and quant_dende == quant_bambugigante and quant_dende == quant_coqueiro and quant_dende == quant_mangueira:
                        if quant_coqueiro == quant_cajueiro and quant_coqueiro == quant_mangueira and quant_coqueiro == quant_bambugigante and quant_coqueiro == quant_ipe and quant_coqueiro == quant_dende:
                            if quant_bambugigante == quant_cajueiro and quant_bambugigante == quant_mangueira and quant_bambugigante == quant_ipe and quant_bambugigante == quant_dende and quant_bambugigante == quant_coqueiro:
                                if quant_ipe == quant_cajueiro and quant_ipe == quant_mangueira and quant_ipe == quant_bambugigante and quant_ipe ==quant_dende and quant_ipe == quant_coqueiro:
                                    print("HOUVE EMPATE NO USO DAS ARVORES:\n")
                                    print('-Cajueiro foi usado em {} areas.'.format(quant_cajueiro))
                                    print('-Mangueira foi usado em {} areas.'.format(quant_mangueira))
                                    print('-Dende foi usado em {} areas.'.format(quant_dende))
                                    print('-Coqueiro foi usado em {} areas.'.format(quant_coqueiro))
                                    print('-Bambu Gigante foi usado em {} areas.'.format(quant_bambugigante))
                                    print('-Ipe foi usado em {} areas.'.format(quant_ipe))
#Caso não ocorra um empate entre todas as árvores a informação de uso será gerada normalmente inclusive em caso de 
#quantidade igual de uso entre cinco árvores ou menos.
            else:
                print('ARVORE(S) MAIS USADA(S) NO REFLORESTAMENTO:\n')

                if quant_cajueiro >= quant_mangueira and quant_cajueiro >= quant_bambugigante and quant_cajueiro >= quant_ipe and quant_cajueiro >= quant_dende and quant_cajueiro >= quant_coqueiro:
                                print('-Cajueiro foi usado em {} areas.'.format(quant_cajueiro))
                                
                if quant_mangueira >= quant_cajueiro and quant_mangueira >= quant_dende and quant_mangueira >= quant_coqueiro and quant_mangueira >= quant_bambugigante and quant_mangueira >= quant_ipe:
                                print('-Mangueira foi usado em {} areas.'.format(quant_mangueira))
                                
                if quant_dende >= quant_cajueiro and quant_dende >= quant_ipe and quant_dende >= quant_bambugigante and quant_dende >= quant_coqueiro and quant_dende >= quant_mangueira:
                                print('-Dende foi usado em {} areas.'.format(quant_dende))
                                
                if quant_coqueiro >= quant_cajueiro and quant_coqueiro >= quant_mangueira and quant_coqueiro >= quant_bambugigante and quant_coqueiro >= quant_ipe and quant_coqueiro >= quant_dende:
                                print('-Coqueiro foi usado em {} areas.'.format(quant_coqueiro))
                                
                if quant_bambugigante >= quant_cajueiro and quant_bambugigante >= quant_mangueira and quant_bambugigante >= quant_ipe and quant_bambugigante >= quant_dende and quant_bambugigante >= quant_coqueiro:
                                print('-Bambu Gigante foi usado em {} areas.'.format(quant_bambugigante))
                                
                if quant_ipe >= quant_cajueiro and quant_ipe >= quant_mangueira and quant_ipe >= quant_bambugigante and quant_ipe >=quant_dende and quant_ipe >= quant_coqueiro:
                                print('-Ipe foi usado em {} areas.'.format(quant_ipe))

                print('\nARVORE(S) MENOS USADA(S) NO REFLORESTAMENTO:\n')
                                
                if quant_cajueiro <= quant_mangueira and quant_cajueiro <= quant_bambugigante and quant_cajueiro <= quant_ipe and quant_cajueiro <= quant_dende and quant_cajueiro <= quant_coqueiro:
                                print('-Cajueiro foi usado em {} areas.'.format(quant_cajueiro))
                                
                if quant_mangueira <= quant_cajueiro and quant_mangueira <= quant_dende and quant_mangueira <= quant_coqueiro and quant_mangueira <= quant_bambugigante and quant_mangueira <= quant_ipe:
                                print('-Mangueira foi usado em {} areas.'.format(quant_mangueira))
                                
                if quant_dende <= quant_cajueiro and quant_dende <= quant_ipe and quant_dende <= quant_bambugigante and quant_dende <= quant_coqueiro and quant_dende <= quant_mangueira:
                                print('-Dende foi usado em {} areas.'.format(quant_dende))
                                
                if quant_coqueiro <= quant_cajueiro and quant_coqueiro <= quant_mangueira and quant_coqueiro <= quant_bambugigante and quant_coqueiro <= quant_ipe and quant_coqueiro <= quant_dende:
                                print('-Coqueiro foi usado em {} areas.'.format(quant_coqueiro))
                                
                if quant_bambugigante <= quant_cajueiro and quant_bambugigante <= quant_mangueira and quant_bambugigante <= quant_ipe and quant_bambugigante <= quant_dende and quant_bambugigante <= quant_coqueiro:
                                print('-Bambu Gigante foi usado em {} areas.'.format(quant_bambugigante))
                                
                if quant_ipe <= quant_cajueiro and quant_ipe <= quant_mangueira and quant_ipe <= quant_bambugigante and quant_ipe <=quant_dende and quant_ipe <= quant_coqueiro:
                                print('-Ipe foi usado em {} areas.'.format(quant_ipe))
            
            print('\nINFORMACOES DA MAIOR AREA CADASTRADA:\n')
            print('AREA TOTAL {:.2f}\nCODIGO: {}\nCIDADE: {}'.format(maior_area, codigo_maior, cidade_maior))

#No menu os estados estão definidos por strings, onde cada estado é representado por um número, neste momento é
#necessário realizar uma tradução, transformando estes números nos seus estados correspondentes.
            if estado_maior == '1':
                estado_maior = 'BAHIA'
            
            elif estado_maior == '2':
                estado_maior = 'SERGIPE'
            
            elif estado_maior == '3':
                estado_maior = 'ALAGOAS'
            
            elif estado_maior == '4':
                estado_maior = 'PERNAMBUCO'
            
            elif estado_maior == '5':
                estado_maior = 'PARAIBA'
            
            elif estado_maior == '6':
                estado_maior = 'RIO GARNDE DO NORTE'
            
            elif estado_maior == '7':
                estado_maior = 'CEARA'
            
            elif estado_maior == '8':
                estado_maior = 'MARANHAO'
            
            elif estado_maior == '9':
                estado_maior = 'PIAUI'
            print('ESTADO: {}'.format(estado_maior))

#No menu as árvores estão definidas por strings, onde cada árvore é representada por um número, neste momento é
#necessário realizar uma tradução, transformando estes números nas árvores correspondentes.
            if arvore_maior == '1':
                arvore_maior = 'CAJUEIRO'
            
            elif arvore_maior == '2':
                arvore_maior = 'MANGUEIRA'
            
            elif arvore_maior == '3':
                arvore_maior = 'DENDE'
            
            elif arvore_maior == '4':
                arvore_maior = 'COQUEIRO'
            
            elif arvore_maior == '5':
                arvore_maior = 'BAMBU GIGANTE'
            
            elif arvore_maior == '6':
                arvore_maior = 'IPE'
            print('ARVORE: {}'.format(arvore_maior))
            
            print('\nQUANTIDADE DE AREAS REFOLRESTADAS POR ESTADO:\n')
            print('{} na Bahia\n{} no Alagoas\n{} no Ceara'.format(quant_areaba,quant_areaal,quant_areace))
            print('{} no Maranhao\n{} na Paraiba\n{} no Pernambuco'.format(quant_areama,quant_areapb,quant_areape))
            print('{} no piaui\n{} no Rio Grande do Norte\n{} no Sergipe\n'.format(quant_areapi,quant_arearn, quant_arease))
            
#No momento final do relatório, o estado menos reflorestado será exibido, comparações serão feitas para que
#em caso de empate a informaçao seja mostrada corretamente.
            print('ESTADO(S) MENOS REFLORESTADO(S):\n')
            if tot_estadoal <= tot_estadoba and tot_estadoal <= tot_estadoce and tot_estadoal <= tot_estadoma and tot_estadoal <= tot_estadopb and tot_estadoal <= tot_estadope and tot_estadoal <= tot_estadorn and tot_estadoal <= tot_estadose and tot_estadoal <= tot_estadopi:
                print('Alagoas com {:.2f} m²'.format(tot_estadoal))
            
            if tot_estadoba <= tot_estadoal and tot_estadoba <= tot_estadoce and tot_estadoba <= tot_estadoma and tot_estadoba <= tot_estadopb and tot_estadoba <= tot_estadope and tot_estadoba <= tot_estadorn and tot_estadoba <= tot_estadose and tot_estadoba <= tot_estadopi:
                print('Bahia com {:.2f}'.format(tot_estadoba))

            if tot_estadoce <= tot_estadoal and tot_estadoce <= tot_estadoba and tot_estadoce <= tot_estadoma and tot_estadoce <= tot_estadopb and tot_estadoce <= tot_estadope and tot_estadoce <= tot_estadorn and tot_estadoce <= tot_estadose and tot_estadoce <= tot_estadopi:
                print('Ceara com {:.2f} m²'.format(tot_estadoce))
            
            if tot_estadoma <= tot_estadoal and tot_estadoma <= tot_estadoba and tot_estadoma <= tot_estadoce and tot_estadoma <= tot_estadopb and tot_estadoma <= tot_estadope and tot_estadoma <= tot_estadorn and tot_estadoma <= tot_estadose and tot_estadoma <= tot_estadopi:
                print('Maranhao com {:.2f} m²'.format(tot_estadoma))
            
            if tot_estadopb <= tot_estadoal and tot_estadopb <= tot_estadoba and tot_estadopb <= tot_estadoce and tot_estadopb <= tot_estadoma and tot_estadopb <= tot_estadope and tot_estadopb <= tot_estadorn and tot_estadopb <= tot_estadose and tot_estadopb <= tot_estadopi:
                print('Paraiba com {:.2f} m²'.format(tot_estadopb))
            
            if tot_estadope <= tot_estadoal and tot_estadope <= tot_estadoba and tot_estadope <= tot_estadoce and tot_estadope <= tot_estadoma and tot_estadope <= tot_estadopb and tot_estadope <= tot_estadorn and tot_estadope <= tot_estadose and tot_estadope <= tot_estadopi:
                print('Pernambuco com {:.2f} m²'.format(tot_estadope))
            
            if tot_estadorn <= tot_estadoal and tot_estadorn <= tot_estadoba and tot_estadorn <= tot_estadoce and tot_estadorn <= tot_estadoma and tot_estadorn <= tot_estadopb and tot_estadorn <= tot_estadope and tot_estadorn <= tot_estadose and tot_estadorn <= tot_estadopi:
                print('Rio Grande do Norte com {:.2f} m²'.format(tot_estadorn))

            if tot_estadose <= tot_estadoal and tot_estadose <= tot_estadoba and tot_estadose <= tot_estadoce and tot_estadose <= tot_estadoma and tot_estadose <= tot_estadopb and tot_estadose <= tot_estadope and tot_estadose <= tot_estadorn and tot_estadose <= tot_estadopi:
                print('Sergipe com {:.2f} m²'.format(tot_estadose))

            if tot_estadopi <= tot_estadoal and tot_estadopi <= tot_estadoba and tot_estadopi <= tot_estadoce and tot_estadopi <= tot_estadoma and tot_estadopi <= tot_estadopb and tot_estadopi <= tot_estadope and tot_estadopi <= tot_estadorn and tot_estadopi <= tot_estadose:
                print('Piaui com {:.2f} m²'.format(tot_estadopi))
#FIM DO PROGRAMA            
