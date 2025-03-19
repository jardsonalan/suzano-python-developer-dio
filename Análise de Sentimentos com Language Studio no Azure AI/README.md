# Análise de Sentimentos com Language Studio no Azure AI

Este repositório está destinado ao desafio da **Suzano - Python Developer**, bootcamp da **DIO**, onde o objetivo é criar um README.md explicando o processo prático da Análise de Sentimentos com Language Studio no Azure AI.

***Observação:*** Devido a um bug com minha conta da Microsoft, não conseguir realizar os testes dentro da ferramenta da Language Studio, porém, irei deixar uma espécie de resumo sobre como iria funcionar.

## Sentenças

A Language Studio classifica as sentenças em 3 tipos, que são: Positivas, Neutras ou Negativas. Onde, as mesmas podem ser utilizadas para avaliarem opiniões em textos, como: avaliações de pedidos, feedbacks e postagens em redes sociais.

Com isso, dentro da pasta **inputs**, para cada tipo de sentença, criei 3 frases diferentes, que seriam testadas dentro da Language Studio, para observar a análise de sentimentos:

- **Sentenças Positivas:**
    
    1. Estou extremamente satisfeito com o atendimento, foi rápido e eficiente!
    2. O produto superou minhas expectativas, recomendo a todos.
    3. A interface do aplicativo é intuitiva e muito fácil de usar.

- **Sentenças Neutras:**

    1. Recebi meu pedido hoje e ainda não testei o produto.
    2. O serviço funciona como descrito, nada de excepcional.
    3. A loja tem várias opções, mas os preços são medianos.

- **Sentenças Negativas:**

    1. Tive uma experiência péssima, o serviço demorou muito mais do que o prometido.
    2. O produto veio com defeito e o suporte não respondeu minhas mensagens.
    3. A interface do site é confusa e difícil de navegar.

Visto que, no Language Studio da Azure AI, a análise de sentimentos retorna três tipos principais de saída para cada sentença, que são:

1. Sentimento geral (positivo, neutro ou negativo);
2. Pontuação de confiança para cada sentimento (valores entre 0 e 1);
3. Classificação de trechos individuais dentro da sentença.

Como exemplo, podemos definir que as primeiras sentenças de cada tipo, apresentadas acima e que estão no arquivo **sentencas.txt**, seriam analisadas da seguinte forma:

- **Sentença Positiva:**
    
    1. Estou extremamente satisfeito com o atendimento, foi rápido e eficiente!

    **Exemplo de saída do Language Studio:**

    - **Sentimento geral:** Positivo
    - **Confiança:** Positivo: (0.98), Neutro: (0.01), Negativo (0.01)
    - **Trechos analisados:**

        "Estou extremamente satisfeito" - (Positivo)
        
        "o atendimento, foi rápido e eficiente" - (Positivo)

- **Sentença Neutra:**
    
    1. Recebi meu pedido hoje e ainda não testei o produto.

    **Exemplo de saída do Language Studio:**

    - **Sentimento geral:** Neutro
    - **Confiança:** Positivo: (0.15), Neutro: (0.80), Negativo (0.05)
    - **Trechos analisados:**

        "Recebi meu pedido hoje" - (Neutro)
        
        "ainda não testei o produto" - (Neutro)

- **Sentença Negativa:**
    
    1. Tive uma experiência péssima, o serviço demorou muito mais do que o prometido.

    **Exemplo de saída do Language Studio:**

    - **Sentimento geral:** Negativo
    - **Confiança:** Positivo: (0.02), Neutro: (0.05), Negativo (0.93)
    - **Trechos analisados:**

        "Tive uma experiência péssima" - (Negativo)
        
        "o serviço demorou muito mais do que o prometido" - (Negativo)

***Observação:*** São apenas exemplos de como seriam as saídas na Language Studio, ou seja, são dados genéricos criados apenas para exemplificação.

## Conclusão

A análise de sentimentos com o Language Studio no Azure AI é uma ferramenta poderosa para compreender opiniões e emoções em textos, classificando sentenças como positivas, neutras ou negativas. Apesar de não ter sido possível realizar os testes diretamente na ferramenta devido a um problema técnico, este README apresenta um resumo detalhado do processo, incluindo exemplos de sentenças e possíveis saídas geradas pela análise.

Com base nos exemplos fornecidos, é possível observar como o Language Studio avalia o sentimento geral, a pontuação de confiança e os trechos individuais de cada sentença. Essa funcionalidade pode ser aplicada em diversos contextos, como avaliações de produtos, feedbacks de clientes e interações em redes sociais, auxiliando na tomada de decisões e na melhoria de serviços.

Este projeto demonstra o potencial da análise de sentimentos e como ela pode ser utilizada para extrair insights valiosos a partir de dados textuais.