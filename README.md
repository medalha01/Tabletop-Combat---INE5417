# Template de projeto py_netgames

## Para utilizar este template:

1. Realizar [download deste repositório](https://github.com/gabrielroza/py_netgames_template/archive/refs/heads/master.zip)
    * Também é possível [utilizar o próprio GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) para criar um repositório a partir deste template, dessa forma o desenvolvimento já pode ser iniciado com controle de versão. Se assim o fizer, realize git clone ao invés de download.
1. Se desejar, renomear a pasta project_name para o nome do jogo que será implementado
1. Certifique-se de que [pipenv está instalado](https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv) 
1.  A partir da pasta raiz do template, execute `python -m pipenv install` para criar um ambiente Python com as dependências descritas no [Pipfile](./Pipfile) já instaladas
1. A partir da pasta raiz do template, execute `python -m pipenv shell` para iniciar um terminal no contexto do interpretador Python criado no passo anterior. Então, execute `python -m project_name` para rodar o código partindo de [\_\_main\_\_.py](./project_name/__main__.py). 
    * Se houver renomeado a pasta project_name conforme o segundo passo, troque project_name nos comandos pelo novo nome da pasta.
1. A partir de agora é possível seguir com a implementação. Como sugestão, o pacote [game_logic](./project_name/game_logic/) pode ser utilizado para as classes da lógica do jogo em si. 

### Uso com IDEs

Para que IDEs visualizem corretamente a instalação de dependências realizadas dentro de um ambiente Pipenv, é necessário apontar para o interpretador correto, aquele criado pelo pipenv `pipenv install`.

-  No caso do VSCode isso pode ser feito, após a instalação do plugin de Python, através do fluxo [Select Interpreter](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
- No caso do PyCharm, através do [Setting an existing Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)
