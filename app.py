import requests

# URL da API pública
url = "https://jsonplaceholder.typicode.com/posts"

# Fazendo a requisição GET
response = requests.get(url)
if response.status_code == 200:
    posts = response.json()  # Converte a resposta para JSON
    
    #for post in posts[:10]:  # Mostra apenas os 5 primeiros posts
    #    print(f"ID: {post['id']}")
    #    print(f"Título: {post['title']}")
    #    print(f"Conteúdo: {post['body']}")
    #    print(f"User ID: {post['userId']}")
    #    print("-" * 40)
    
    # Procurando o post com ID 10
    for post in posts:
        if post['id'] == 8:
            print("=== Post encontrado! ===")
            print(f"ID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Conteúdo: {post['body']}")
            print(f"User ID: {post['userId']}")
            break 
else:
    print("Erro ao buscar os dados da API")

    
