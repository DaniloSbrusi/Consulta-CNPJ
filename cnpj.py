import basedosdados as bd

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_me_cnpj',
table_id='socios',
billing_project_id='cnpj-377823',
limit=100)

# print(df.columns)
# 'data', 'cnpj_basico', 'tipo', 'nome', 'documento', 'qualificacao',
# 'data_entrada_sociedade', 'id_pais', 'cpf_representante_legal',
# 'nome_representante_legal', 'qualificacao_representante_legal','faixa_etaria'
print()
print(df.nome.head())

query = input('Nome para pesquisar: ')
query = query.strip().upper()
result = df[df.nome.str.contains(query)]
print(f'Foram encontrados {result.count()} resultados!')
print(result)

# Para enviar 
# df[df.nome.str.contains('ANDRE')].to_json(orient='split')

# View na página
# | Nome          | CPF         | CNPJ    | Data Entrada | Ver mais
# | Danilo Sbrusi | ***010989** | 8197292 | 2017-11-01   | [Detalhar]


# Melhorias:
# - Usar easyautocomplete
# - Detalhar
# - Exibir nome da empresa na consulta inicial (requisição paralela)
# 

# dicionario = bd.read_table(dataset_id='br_me_cnpj',
#                             table_id='dicionario',
#                             billing_project_id="cnpj-377823")
# dicionario[dicionario.id_tabela.str.contains('socios')].to_dict(orient='split')['data']