import requests,json,sys

config = {'api_sus':'http://dabsistemas.saude.gov.br/sistemas/sadab/js/buscar_cpf_dbpessoa.json.php?cpf=', 'cpf':sys.argv[1]}
req = requests.get(config['api_sus']+config['cpf'])
dados = json.loads(req.content.decode("utf-8"))
print ("Nome: ", dados['NO_PESSOA_FISICA'], "\nCPF: ", dados['NU_CPF'], "\nData de nascimento:", dados['DT_NASCIMENTO'], "\nNome da mãe: ", dados['NO_MAE'])