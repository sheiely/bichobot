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

## Testes

Para executar os testes:
```sh
rasa test
```

## TODO List

- [ ] Fazer o `makefile` das dependências
- [ ] Separar `nlu.yml`, `rule.yml`, `domain.yml`, em pastas com nomes descritivos.

## Divisão da Equipe

**Henrique** 
- [ ] PERGUNTAS SOBRE LOCALIZAÇÂO
- [ ] PERGUNTAS SOBRE O CAMPUS/QUIXADA/MORADIA
- [ ] PERGUNTAS SOBRE OS CURSOS

**Victor**
- [ ] PERGUNTAS SOBRE O RU
- [ ] PERGUNTAS SOBRE OS ONIBUS
- [ ] PERGUNTAS SOBRE A BIBLIOTECA

**Sheiely**
- [ ] PERGUNTAS SOBRE OS PROJETOS
- [ ] PERGUNTAS SOBRE SISTEMAS/SERVIÇOS
- [ ] PERGUNTAS BOLSAS/ASSISTENCIA
- [ ] PERGUNTAS GERAIS