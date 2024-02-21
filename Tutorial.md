# Funcionamento do programa

  Para a extração do preço, o robô está configurado com a tabela mais atualizada da GOINFRA, portanto, essa é a composição de custos base utilizada neste programa. 

  Em relação ao funcionamento, o programa realiza uma busca utilizando o código "ID GOINFRA" na planilha de quantitativos e no banco de dados da GOINFRA. Considerando que o sistema opera com o conceito de chave primária, cada serviço no banco de dados possui um ID único. Com esse ID, o sistema utiliza o valor do preço unitário para calcular o montante financeiro final.
  
  Posteriormente, o sistema permite a exportação de uma nova planilha com colunas adicionais preenchidas com esses dados. Dessa forma, o orçamento dos serviços em questão estará disponível em um arquivo do tipo "xls", possibilitando ao usuário formatá-lo conforme sua preferência.


# Cálculo do orçamento

  Ao acessar a plataforma, o usuário pode utilizar o menu "browse files" para fazer o *upload* da sua tabela de referência. Conforme mencionado anteriormente, o *software* reconhece automaticamente o tipo de levantamento e realiza a precificação correspondente. Após a precificação, a tela é modificada e exibe a tabela de quantitativos com o orçamento calculado e pronta para realizar o *download*, para isso, basta clicar em “Baixar arquivo”. Em caso de dúvidas, acesse o tutorial detalhado [aqui](https://drive.google.com/file/d/1gMEWhPDDRS-byXOuDA97melv1H9PpRsp/view?usp=sharing).
