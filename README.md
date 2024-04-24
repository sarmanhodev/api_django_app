API Django App

Visão Geral
Este projeto consiste em uma API simples desenvolvida em Django, que realiza operações CRUD (Create, Read, Update, Delete) em um banco de dados. A API fornece endpoints para criar, recuperar, atualizar e excluir recursos do banco de dados de acordo com as necessidades do aplicativo. O principal objetivo é fornecer uma interface robusta e eficiente para interagir com os dados do sistema de forma programática, facilitando a manipulação e gerenciamento dos mesmos.

Tecnologias Utilizadas
Django, Django REST Framework

Configuração do Ambiente de Desenvolvimento
Para configurar o ambiente de desenvolvimento e começar a trabalhar neste projeto, você precisará ter instaladas as seguintes dependências:

1 -Django: Um framework web em Python para o desenvolvimento rápido de aplicativos web.
2 - Django REST Framework: Uma poderosa e flexível ferramenta para construir APIs web.
Você pode instalar essas dependências usando o pip, o gerenciador de pacotes padrão do Python. Certifique-se de estar em um ambiente virtual Python antes de instalar as dependências. Se você ainda não tem o pip instalado, você pode instalá-lo seguindo as instruções oficiais.
Para instalar as dependências, execute os seguintes comandos no terminal:
pip install django
pip install djangorestframework

Após a instalação bem-sucedida das dependências, você estará pronto para executar o projeto localmen

Executando o Projeto
Para iniciar o servidor Django e executar o projeto localmente, siga estas etapas:
1 - Navegue até o diretório raiz do projeto no seu terminal.
2 - Certifique-se de que seu ambiente virtual Python esteja ativado. Se você ainda não criou um ambiente virtual, pode fazê-lo utilizando virtualenv ou venv.
3 - Execute o seguinte comando para iniciar o servidor Django: python manage.py runserver
4 - Após executar este comando, você verá mensagens de saída indicando que o servidor foi iniciado com sucesso. Por padrão, o servidor será executado em http://127.0.0.1:8000/.
5 - Abra seu navegador da web e vá para o endereço http://127.0.0.1:8000/ para acessar o projeto.

Endpoints da API
Aqui você pode listar todos os endpoints da sua API, junto com uma breve descrição de sua funcionalidade.

Exemplo:

GET /produtos/: Retorna uma lista de todos os produtos.
POST produtos/criar/: Cria um novo produto.
GET /produtos/<int:pk>/: Retorna os detalhes de um produto específico.
PUT /produtos/<int:pk>/atualizar/: Atualiza os detalhes de um produto específico.
DELETE /produtos/<int:pk>/excluir/: Deleta um produto específico.
