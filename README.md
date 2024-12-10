# CalouroBot

*depois eu boto uma fotinha*

## Sobre

Este repositório tem como objetivo desenvolver uma **IA** utilizando a plataforma [**Rasa**](https://github.com/RasaHQ/rasa) para responder às perguntas mais frequentes de calouros de forma automatizada e eficiente. A base de conhecimento será o [Manual dos Calouros]((https://drive.google.com/file/d/1CsDc-PBksHCyYneYCpuDRfPPXHJSXNET/view)) da **UFC Quixadá** e o [site oficial da instituição](https://www.quixada.ufc.br/). Essas fontes serão organizadas e transformadas em um conjunto de regras, intenções e histórias para que a **IA** possa oferecer respostas claras facilitando a experiência dos novos estudantes.

**Link:** [Manual_dos_calouros.pdf](https://drive.google.com/file/d/1CsDc-PBksHCyYneYCpuDRfPPXHJSXNET/view)

## Como Executar o Projeto

### Pré-requisitos

- python 3.9.13 ([windows](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)/[linux])
- makefile
- venv

### Instalação Linux

1. Clone o repositório
```
git clone https://github.com/seu-usuario/CalouroBot.git
cd CalouroBot
```
2. Crie e ative um ambiente virtual
```sh
python3.9 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. instale as dependências
```sh
make install
```

### Execução

1. Para iniciar assistente:
```sh
make start
```

### Testes

1. Para executar os testes:
```sh
rasa test
```

### Instalação Codespace

## TODO List

- [X] Fazer o `makefile` das dependências
- [X] Separar `nlu.yml`, `rule.yml`, `domain.yml`, em pastas com nomes descritivos.
- [X] Implementar `chitchat` para não precisar criar os rule do projeto.
- [X] Criar pelo menos um teste
- [ ] Criar FAQ
    - [nlu](./data/nlu/faq.yml)/[response](./domain/faq.yml)

## Divisão da Equipe

- [X] Exemplo
    - [nlu](./data/nlu/__exemplo__.yml)/[response](./domain/__exemplo__.yml)

**Henrique** 
-  [ ] Perguntas sobre localização
    - [nlu](./data/nlu/localizacao.yml)/[response](./domain/localizacao.yml) (localizacao)
-  [ ] Perguntas sobre o \(campus/Quixadá/moradia\)
    - [nlu](./data/nlu/campus.yml)/[response](./domain/campus.yml) (campus)
    - [nlu](./data/nlu/quixada.yml)/[response](./domain/quixada.yml) (quixada)
    - [nlu](./data/nlu/moradia.yml)/[response](./domain/moradia.yml) (moradia)
-  [ ] Perguntas sobre os cursos
    - [nlu](./data/nlu/cursos.yml)/[response](./domain/cursos.yml) (cursos)

**Victor**
-  [ ] Perguntas sobre o RU
    - [nlu](./data/nlu/ru.yml)/[response](./domain/ru.yml) (ru)
-  [ ] Perguntas sobre os ônibus  
    - [nlu](./data/nlu/onibus.yml)/[response](./domain/onibus.yml) (onibus)
-  [ ] Perguntas sobre a biblioteca
    - [nlu](./data/nlu/biblioteca.yml)/[response](./domain/biblioteca.yml) (biblioteca)

**Sheiely**
-  [ ] Perguntas sobre os projetos
    - [nlu](./data/nlu/projetos.yml)/[response](./domain/projetos.yml) (projetos)
-  [ ] Perguntas sobre sistemas e serviços
    - [nlu](./data/nlu/sistemas.yml)/[response](./domain/sistemas.yml) (sistemas)
-  [ ] Perguntas sobre bolsas/assistência
    - [nlu](./data/nlu/bolsas.yml)/[response](./domain/bolsas.yml) (bolsas)
    - [nlu](./data/nlu/assistencia.yml)/[response](./domain/assistencia.yml) (assistencia)
-  [ ] Perguntas gerais
    - [nlu](./data/nlu/geral.yml)/[response](./domain/geral.yml) (geral)
