class Gerar_Tabela():
    
    def __init__(self):
        self.nome = input("Nome da tabela: ")
        self.__nome_tabela = 'CREATE TABLE {}'.format(self.nome)
    
    def salvar(self):
        import sqlite3
        conn = sqlite3.connect('{}.db'.format(self.nome))
        c = conn.cursor()
        texto = self.nome_tabela
        try:
            c.execute(texto)
        except: 
            print('A tabela já foi criada.')
        conn.close()        
        
        
    def __criar_coluna(self):
        # alterar nome_tabela
        self.nome_coluna = input('Qual campo \x1b[6;30;44m COLUNA \x1b[0m você deseja \x1b[6;30;44m CRIAR \x1b[0m: ')
        self.nome_tabela +=  ', {}'.format(self.nome_coluna.lower().capitalize())

    def __tipo_variavel(self):

        print('Qual tipo de dado é adequado para a coluna \x1b[7;30;46m {} \x1b[0m: '.format(self.nome_tabela.split()[-1]))

        nome_tipo = input('1:INTEGER\n2:REAL\n3:TEXT\n4:DATE\n\n')

        dicionario = {'1':'INTEGER','2':'REAL','3':'TEXT','4':'DATE'}

        if nome_tipo in ['1','2','3','4']:

            self.nome_tabela += ' {}'.format(dicionario[nome_tipo])

        else:
            print('## Tipo não disponível.')
            print()
            self.__tipo_variavel()        

    def __add_linha(self):
        self.__criar_coluna()
        print()
        self.__tipo_variavel()    
        
    def __imprimir_colunas(self):
        
        lista = []
        for i, c in enumerate(self.nome_tabela):
            if c == ',':
                lista.append(i)
        for i in range(len(lista)-1):
            print(self.nome_tabela[lista[i]+2: lista[i+1]])
        if self.nome_tabela.rfind(',') == -1:
            print('Algo errado aconteceu.')
            pass
        else:
            print(self.nome_tabela[self.nome_tabela.rfind(',')+2:])
       

    def criar_tabela(self):
        
        from unidecode import unidecode
#         nome_tabela = input("Nome da tabela: ")
#         nome_tabela = 'CREATE TABLE {}'.format(nome_tabela)
#         add id
        self.nome_tabela = self.__nome_tabela
        self.nome_tabela = self.nome_tabela + '( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'

        nova_linha = True
        while nova_linha:
            criar_nova_linha = input('\x1b[5;30;43m CRIAR \x1b[0m nova coluna? ')
            
            print()
            
            if criar_nova_linha.lower() == 's' or criar_nova_linha.lower() == 'sim':
                
                # adicionando colunas ao SQL
                self.__add_linha()

                # imprimir colunas
                print()
                print("Colunas criadas até o momento:")
                self.__imprimir_colunas()

            elif criar_nova_linha.lower() == 'n' or unidecode(criar_nova_linha.lower()) == 'nao':
                
                # fechando a string SQL
                self.nome_tabela += ' );'
                nova_linha = False
            
            else:
                
                print()
                print("Não entendi o que você digitou:")
                self.__imprimir_colunas()
                
        return self.nome_tabela
    