# CalouroBot

*depois eu boto uma fotinha*

## Sobre

Este repositório tem como objetivo desenvolver uma **IA** utilizando a plataforma [**Rasa**](https://github.com/RasaHQ/rasa) para responder às perguntas mais frequentes de calouros de forma automatizada e eficiente. A base de conhecimento será o [Manual dos Calouros]((https://drive.google.com/file/d/1CsDc-PBksHCyYneYCpuDRfPPXHJSXNET/view)) da **UFC Quixadá** e o [site oficial da instituição](https://www.quixada.ufc.br/). Essas fontes serão organizadas e transformadas em um conjunto de regras, intenções e histórias para que a **IA** possa oferecer respostas claras facilitando a experiência dos novos estudantes.

**Link:** [Manual_dos_calouros.pdf](https://drive.google.com/file/d/1CsDc-PBksHCyYneYCpuDRfPPXHJSXNET/view)

## Como Executar o Projeto

### Pré-requisitos

- python 3.9.13
- venv

### Instalação

1. Clone o repositório
```
git clone https://github.com/seu-usuario/CalouroBot.git
cd CalouroBot
```
2. Crie e ative um ambiente virtual
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. instale as dependências
```sh
make install
```

### Execução

1. Para treinar o modelo:
```sh
rasa train
```

2. Para iniciar o bot:
```sh
rasa shell
```

### Testes

1. Para executar os testes:
```sh
rasa test
```

## TODO List

- [ ] Fazer o `makefile` das dependências
- [X] Separar `nlu.yml`, `rule.yml`, `domain.yml`, em pastas com nomes descritivos.
- [ ] Implementar `chitchat` para não precisar criar os rule do projeto.

## Divisão da Equipe

**Henrique** 
-  [ ] Perguntas sobre [localização](./data/nlu/nlu_localizacao.yml)
-  [ ] Perguntas sobre o [campus][localização](./data/nlu/nlu_campus.yml)/[Quixadá]/moradia\)
-  [ ] Perguntas sobre os cursos

**Victor**
-  [ ] Perguntas sobre o RU
-  [ ] Perguntas sobre os ônibus  
-  [ ] Perguntas sobre a biblioteca  

**Sheiely**
-  [ ] Perguntas sobre os projetos  
-  [ ] Perguntas sobre sistemas/serviços  
-  [ ] Perguntas sobre bolsas/assistência  
-  [ ] Perguntas gerais  