# Desafio 1 - Representação de Dados

## Problema
Gerar uma matriz de dados numéricos, a partir de um ou de ambos os textos anexo.

Temos que ser capazes de voltar ao texto a partir da matriz. 

Podemos abrir mão de caracteres especiais e pontuação.

Deve ser entregue a matriz, um texto explicando a estratégia e o código fonte utilizado para gerar a matriz (quando houver).

## Legenda
- Diretório **`data`**: Arquivos `txt` fontes para a transformação;
- Diretório **`res`**: Arquivos `txt` e `csv` com os resultados;
- Diretório **`src`**: Código fonte `main.py`

## Solução Proposta
Utilizando Python, a solução proposta foi importar os arquivos `txt` para o contexto do script, iterar pelo texto e converter cada caractere ASCII para um valor Unicode respectivo utilizando a função `ord()`, após isso salvá-los em uma lista de arquivos e exportar essa lista para um formato `csv`.

Para validar que a conversão foi correta deve-se carregar o `csv` e converter os números em uma matriz, em seguida iterar sobre a matriz e converter os valores em seu respectivo caractere ASCII utilizando a função `chr()`, após isso salvar o texto em um arquivo `txt` para posterior validação com os dados de origem.