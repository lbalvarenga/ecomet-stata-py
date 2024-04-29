<!-- by Lucas Alvarenga, with data from http://www.ipeadata.gov.br/ -->

# Trabalho Acadêmico - Tópicos Avançados em Econometria

```plaintext
                   (  )/
                    )(/
 ________________  ( /)
()__)____________)))))    hjw

Art by Hayley Jane Wakenshaw
```

`unify.py` unifica as bases em um único arquivo para facilitar a análise em softwares estatísticos. Para utilizar:

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 unify.py > csv/output.csv
```

## Objetivo Geral

Determinar correlação entre fabricação de produtos de fumo e nível de emprego na área de informação, finanças e administração.

Em outras palavras: pessoal de TI e economia fuma muito para trabalhar?

## fumo.csv

### Produção industrial - fabricação de produtos de fumo: índice de quantum (média 2022 = 100)

- **Frequência:** Mensal de 2002.01 até 2024.02
- **Fonte:** Instituto Brasileiro de Geografia e Estatística, Pesquisa Industrial Mensal - Produção Física (IBGE/PIM-PF)
- **Unidade:** -
- **Comentário:** A produção industrial da fabricação de fumo considera a fabricação de cigarros, cigarrilhas e outros derivados do fumo, além do fumo processado industrialmente (destalamento e outros beneficiamentos elaborados em unidades industriais) e a fabricação de filtros para cigarros. Esta classificação não compreende o cultivo do fumo, bem como o beneficiamento inicial. A base foi fixada como a média das observações no ano de 2022. Notas: A Pesquisa Industrial Mensal Produção Física têm por objetivo acompanhar a evolução do produto real da indústria no curto prazo, sendo necessário o levantamento de informações de volume físico de produtos selecionados e representativos de diferentes atividades industriais, como das indústrias extrativas e de transformação. A pesquisa vêm sendo feita desde 1970, com informações fornecidas todos os meses, até o dia 10 de cada mês posterior ao de referência. A partir de maio de 2014, a Pesquisa Industrial Mensal Produção Física, sofre reformulação e dá-se início a divulgação da nova série de índices mensais da produção industrial, com base nas novas classificações, de atividades e produtos, usadas pelas demais pesquisas da indústria a partir de 2007, quais sejam: a Classificação Nacional de Atividades Econômicas - CNAE 2.0 e a Lista de Produtos da Indústria - PRODLIST-Indústria. Segundo a classificação da CNAE 2.0, a Produção Industrial só identifica os serviços industriais mais importantes e somente quando são exercidos sob contrato. Em 2023, a pesquisa teve uma nova atualização e que foi feita a partir do cadastro de empresas e produtos produzidos pela Pesquisa Industrial Anual (PIA-Empresa e PIA-Produto) de 2019. Nesse processo, atualiza-se o ano base da pesquisa, a cesta de produtos investigados e a estrutura de ponderação. Mais informações: CNAE 2.0 ; Lista de Produtos da Indústria e Dicionário Brasileiro de Estatística.
- **Atualizado em:** 03/04/2024

## fumo_d.csv

### Produção industrial - fabricação de produtos de fumo: índice de quantum dessazonalizado(média 2022 = 100)

- **Frequência:** Mensal de 2002.01 até 2024.02
- **Fonte:** Instituto Brasileiro de Geografia e Estatística, Pesquisa Industrial Mensal - Produção Física (IBGE/PIM-PF)
- **Unidade:** -
- **Comentário:** A produção industrial da fabricação de fumo considera a fabricação de cigarros, cigarrilhas e outros derivados do fumo, além do fumo processado industrialmente (destalamento e outros beneficiamentos elaborados em unidades industriais) e a fabricação de filtros para cigarros. Esta classificação não compreende o cultivo do fumo, bem como o beneficiamento inicial. A base foi fixada como a média das observações no ano de 2022. O ajuste sazonal ou dessazonalização é o processo de remoção do fator ou componente sazonal de uma série temporal econômica, já que várias são baseadas em dados mensais ou trimestrais que possuem um movimento oscilatório regular (padrão sazonal). Normalmente, este padrão é gerado por estações climáticas ou eventos, como por exemplo Natal e férias de verão levando a um aumento da demanda em determinada indústria ou comércio, ou até mesmo um aumento de preço de um produto agrícola após período de colheita. Notas: A Pesquisa Industrial Mensal Produção Física têm por objetivo acompanhar a evolução do produto real da indústria no curto prazo, sendo necessário o levantamento de informações de volume físico de produtos selecionados e representativos de diferentes atividades industriais, como das indústrias extrativas e de transformação. A pesquisa vêm sendo feita desde 1970, com informações fornecidas todos os meses, até o dia 10 de cada mês posterior ao de referência. A partir de maio de 2014, a Pesquisa Industrial Mensal Produção Física, sofre reformulação e dá-se início a divulgação da nova série de índices mensais da produção industrial, com base nas novas classificações, de atividades e produtos, usadas pelas demais pesquisas da indústria a partir de 2007, quais sejam: a Classificação Nacional de Atividades Econômicas - CNAE 2.0 e a Lista de Produtos da Indústria - PRODLIST-Indústria. Segundo a classificação da CNAE 2.0, a Produção Industrial só identifica os serviços industriais mais importantes e somente quando são exercidos sob contrato. Em 2023, a pesquisa teve uma nova atualização e que foi feita a partir do cadastro de empresas e produtos produzidos pela Pesquisa Industrial Anual (PIA-Empresa e PIA-Produto) de 2019. Nesse processo, atualiza-se o ano base da pesquisa, a cesta de produtos investigados e a estrutura de ponderação. Mais informações: CNAE 2.0 ; Lista de Produtos da Indústria ; Dicionário Brasileiro de Estatística e Guajarati, Introdução à Econometria Básica, 4ª Edição, 2004.
- **Atualizado em:** 03/04/2024

## ocupa.csv

### Pessoas de 14 anos ou mais de idade, ocupadas na semana de referência no grupamento de atividade informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas

- **Frequência:** Mensal de 2012.03 até 2024.02
- **Fonte:** Instituto Brasileiro de Geografia e Estatística, Pesquisa Nacional por Amostra de Domicílios Contínua (IBGE/PNAD Contínua)
- **Unidade:** Pessoa (mil)
- **Comentário:** Pessoas que, na semana de referência, trabalharam pelo menos uma hora completa em trabalho remunerado em dinheiro, produtos, mercadorias ou benefícios (moradia, alimentação, roupas, treinamento etc.), ou em trabalho sem remuneração direta em ajuda à atividade econômica de membro do domicílio ou parente que reside em outro domicílio, ou, ainda, as que tinham trabalho remunerado do qual estavam temporariamente afastadas nessa semana. Consideram-se como ocupadas temporariamente afastadas de trabalho remunerado as pessoas que não trabalharam durante pelo menos uma hora completa na semana de referência por motivo de férias, folga, jornada variável ou licença remunerada (em decorrência de maternidade, paternidade, saúde ou acidente da própria pessoa, estudo, casamento, licença-prêmio etc.). Além disso, também foram consideradas ocupadas as pessoas afastadas por motivo diferente dos já citados, desde que o período transcorrido do afastamento fosse inferior a quatro meses, contados até o último dia da semana de referência. As informações dos indicadores são divulgados a cada mês referentes ao último trimestre móvel. Mais informações: Notas metodológicas - PNAD Contínua e Glossário - PNAD Contínua - mensal.
- **Atualizado em:** 28/03/2024
