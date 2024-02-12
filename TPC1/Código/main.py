import csv_to_list
import sys
import funcs

def main():
    
    ficheiro = input("Introduza o nome do ficheiro -> ")
    #ficheiro = "emd.csv"
    print("\n")
    
    sys.stdin = open(ficheiro, 'r')
    
    dados = csv_to_list.to_list()
    
    sys.stdin = sys.__stdin__
    
    saida = -1
    
    # Ciclo de construção do menu e execução das funções
    while saida != 0:
        
        print("MENU:")
        print("1 - Lista ordenada alfabeticamente das modalidades desportivas")
        print("2 - Percentagens de atletas aptos e inaptos para a prática desportiva")
        print("3 - Distribuição de atletas por escalão etário")
        print("0 - Sair\n")
        
        saida = int(input("Introduza a sua opção -> "))
        print("-----------------------------------------------")

        if saida == 0:
            print("Saindo.......")
            
        elif saida == 1:
            print(funcs.modalidades(dados))
            print("-----------------------------------------------")
            print("\n")

        elif saida == 2:
            print("Aptos: " + funcs.aptos_e_inaptos(dados)[0])
            print("Inaptos: " + funcs.aptos_e_inaptos(dados)[1])
            print("-----------------------------------------------")
            print("\n")
        
        elif saida == 3:
            for key, value in funcs.intervalos(dados).items():
                print(f"{key}: {value}\n")
            print("-----------------------------------------------")
            print("\n")
        
        else:
            print("Opção inválida.")
            l = input("prima enter para continuar")
            
            
            
if __name__ == "__main__":
    main()