import pandas as pd
import smtplib
import email.message

# importart base de dados
tab_vendas = pd.read_excel('vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento = tab_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# Obs: a tabela foi filtrada para mostrar 'ID Loja' e 'Valor Final'...
# no caso filtrar com a funçao tab_vendas[['ID Loja', 'Valor Final']]
# e somando com a funçao .groupby(ID Loja).sum()

# no fim mostramos a funçao faturamento

# quantidade de produtos vendidos por loja
quantidade = tab_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
# usando as mesmas funçoes posso saber a quantidade exata dos produtos vendidos

# ticket medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
# funçao .to_frame() faz com que divisao,soma ou algo parecido vire tabelap
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Medio'})


# renomeando coluna

# enviar email com relatorio
def enviar_email():
    corpo_email = f'''
    <p>Prezados,</p>
    
    <p>Segue o relatorio de Vendas de cada Loja</p> 
   
   <p>Faturamento:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R$: {:,.2f}'.format})}
    
    <p>Quantidade:</p>
    {quantidade.to_html(formatters={'Quantidade': 'Qtd: {:.0f}'.format})}
    
    <p>Ticket Dos Produtos Vendidos:</p>
    {ticket_medio.to_html(formatters={'Ticket Medio': 'R$: {:,.2f}'.format})}
    
    
    <p>Att.,</p>
    <p>Marcio Henrique</p>
    '''
    msg = email.message.Message()
    msg['Subject'] = "Relatorio de Vendas"
    msg['From'] = 'alphazx19@gmail.com'
    msg['to'] = 'vivian.vivicat@gmail.com'
    password = 'nzkkoogzrawdjnpg'
    msg.add_header('Content-Type', 'Text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Com credenciais
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))


enviar_email()

print('Email Enviado')
