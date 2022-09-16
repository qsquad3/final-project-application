# APLICAÇÃO QUODE

Aplicação utilizada como docker container no servidor kubernetes
Ao dar um PUSH na main, um CI/CD é executado via GitHub Action para gerar uma nova versão da imagem e publicar no DockerHUB

O mesmo serve para branch "dev"

Durante o CI/CD, há um teste da imagem gerada, efetuando um teste em um banco similar ao utilizado na aplicação oficial

