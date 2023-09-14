import requests

def BuscaFilme(nome_filme, api_key):
    base_url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": api_key,
        "query": nome_filme,
        "language": "pt-BR"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        dados = response.json()

        if dados["total_results"] > 0:
            resultado = dados["results"][0]

            nome = resultado["title"]
            descricao = resultado["overview"]
            ano = resultado["release_date"].split("-")[0]

            print(f"Nome do Filme: {nome}")
            print(f"Ano: {ano}")
            print(f"Descrição: {descricao}")
        else:
            print("Nenhum resultado encontrado para este filme. Revise o texto e digite novamente!")
    else:
        print(f"Errro na solicitação: status {response.status_code}")

if __name__ == "__main__":
    api_key = "ca2f7d89d43b8e1199ab5e7b51b55b99"
    nome_filme = input("Digite o nome do filme: ")
    BuscaFilme(nome_filme, api_key)
