import requests

def consultar_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            dados = response.json()
            if "resultado" in dados:
                if isinstance(dados["resultado"], list):
                    if len(dados["resultado"]) > 0:
                        return dados["resultado"]
        except:
            return "Erro ao processar JSON" 
    return "Erro na requisição"

print(consultar_api("https://api.exemplo.com/dados"))