class Planilha:
    def le_colunas(self, quant_cols):
        nome_cols = []
        for i in range(quant_cols):
            nome_col = input("Digite o nome da coluna: ")
            nome_cols.append(nome_col)
        return nome_cols

    def registros(self, quant_registros, quant_cols):
        quant_cols = le_colunas(quant_cols)
        planilha = []
        planilha.append(quant_cols)
        for i in range(quant_registros):
            registros = []
            for j in range(len(quant_cols)):
                registro = input("Digite os valores: ")
                registros.append(registro)
            planilha.append(registros)
        return planilha

    def planilha(col, lin):
        planilha = registros(lin, col)
        valor = 0
        for i in planilha:
            for j in planilha[valor]:
                print(j, end = '\t')
            valor += 1
            print()
