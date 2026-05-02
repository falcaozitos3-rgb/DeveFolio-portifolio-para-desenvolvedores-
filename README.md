## 🚀 DevFolio - Portfólio System
O DevFolio é um sistema de gerenciamento de portfólio desenvolvido em Python, focado em proporcionar uma experiência segura e fluida para desenvolvedores compartilharem seus projetos.

## 🛠️ Tecnologias UtilizadasPython:
 PYTHON: Linguagem principal do Back-end.Flask: Framework web para criação de rota.
 JSON: Utilizado como banco de dados NoSQL.
 HTML5/CSS3: Estruturação e estilização da interface.
 JavaScript: Lógica de interface (como o botão de visualizar senha 👁️).
 
 ## 🌟 Funcionalidades ImplementadasSistema de Cadastro:
  Captura de Nome, E-mail, Telefone e Senha.Validação de Segurança: Uso de Expressões Regulares (Regex) para garantir senhas fortes e formatos de telefone corretos diretamente no Front-end.
  
  ## Persistência de Dados:
   Armazenamento automático de novos usuários em um arquivo usuarios.json.Navegação Inteligente: Rotas dinâmicas utilizando url_for para evitar links quebrados.Páginas de Suporte: Inclusão de Política de Privacidade e página de Manutenção técnica.UX (User Experience): Funcionalidade de ver/esconder senha para facilitar o login.📁 Estrutura do Projetotext.

├── main.py              # Cérebro do projeto (Rotas e Lógica)├── usuarios.json        # Nosso Banco de Dados├── static/              # Arquivos CSS e Imagens└── templates/           # Arquivos HTML (Páginas)

 Como rodar o projetoInstale o Flask: pip install flaskExecute o servidor: python main.pyAcesse: http://127.0.0.1:5000

 ## coisas que vem por ai:
 iremos implementar o CSS e terminar de estruturar o HTMl, e tambem fazer o resto  o Back-en.
 dito isso vamos adicionar criptografia nas senhas feitas juntamente com coreções de bugs
