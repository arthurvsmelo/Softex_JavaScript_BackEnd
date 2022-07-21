import pandas as pd

df = pd.read_csv("notas_alunos.csv")                                      # abre o .csv
media = df["nota_1"] + df["nota_2"] / 2                                   # calcula a média (entre duas colunas na mesma linha) 
df["media"] = media                                                       # cria a coluna "media"
situacao = "indf"                                                         # inicializa a coluna
df["situacao"] = situacao                                                 # cria a coluna "situação"
df.loc[df["media"] >= 7 and df["faltas"] < 5, "situacao"] = "APROVADO"    # verifica se foi aprovado e atualiza nas linhas
df.loc[df["media"] < 7 or df["faltas"] >= 5, "situacao"] = "REPROVADO"    # verifica se foi reprovado e atualiza nas linhas
max_faltas = df["faltas"].max()                                           # salva o maior numero de faltas
media_geral = df["media"].median()                                        # salva a media das medias (media geral)
maior_media = df["media"].max()                                           # salva a maior media
df.to_csv("alunos_situacao.csv")                                          # salva o arquivo .csv novo

print(f"Maior número de faltas: {max_faltas}")
print(f"Média geral: {media_geral}")
print(f"Maior média: {maior_media}")