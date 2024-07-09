# Simulação de página web
## Scripts para simular acessos a determinadas páginas e indicar se houve ou não conversão de um cliente
#### Este é um projeto simples para exercitar os conhecimentos de manipulação de arquivos Python, linguagem SQL e criação de páginas utilizando HTML, CSS e Javascript.

O primeiro passo é executar o arquivo `dbCreate.sql` para criar o banco de dados.
<img width="602" alt="Captura de Tela 2024-07-08 às 21 22 09" src="https://github.com/exclerosado/webpage-simulation/assets/89822415/bda46e7c-01ba-48e2-be9f-1ade53a8917b">

Após ter o banco de dados criado, execute o arquivo `generateData.py` para começar as inserções no banco de dados. Durante a inserção, podemos executar o comando `select` para verificar se está sendo executado corretamente.
<img width="1366" alt="Captura de Tela 2024-07-08 às 21 24 36" src="https://github.com/exclerosado/webpage-simulation/assets/89822415/a2b9b2af-b161-4545-a5f7-18ff3241c910">

Depois de finalizado, deve-se executar o arquivo `dbSelect.py`, ele será responsável por criar uma consulta no banco de dados e criar um aquivo `.csv` que irá alimentar o gráfico do HTML.

## Gráfico final
<img width="1163" alt="Captura de Tela 2024-07-08 às 21 33 38" src="https://github.com/exclerosado/webpage-simulation/assets/89822415/9b2372d1-d7c6-44c5-826d-7f7908e467cf">
