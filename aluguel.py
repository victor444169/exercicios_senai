import streamlit as st
from random import choice

horario_entrega = ['12:00', '19:00']
#------------------------------------------------------------|
st.sidebar.image('movida_logo.png')
st.sidebar.title('Aluguel de carros ')

carros = ['BMW', 'MUSTANG', 'HB20', 'FUSCA', 'CIVIC']
carro = st.sidebar.selectbox('Selecione o carro alugado', carros)

valor_por_dia = 0 
if carro == 'BMW':
    valor_por_dia = 400
    
elif carro == 'MUSTANG':   
    valor_por_dia = 600

elif carro == 'HB20':   
    valor_por_dia = 100

elif carro == 'CIVIC':   
    valor_por_dia = 150

elif carro == 'FUSCA':   
    valor_por_dia = 50

#-------------------------------------------------------------|

st.title('Aluguel de carro ')
st.write('Seja bem vindo(a)')

st.write(f'Você selecionou carros: {carro}')
st.image(f'{carro}.png')

st.write('Preço por dia', valor_por_dia)


dias = st.text_input('Informe a quantidade de dias ')
km = st.text_input('Informe a quantidade de quilometros rodados ')

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias =  valor_por_dia* dias
    total_km = km * 0.15
    valor_total = total_dias + total_km

    st.warning(f"Você percorreu {km}km por {dias} dias, então o preço a pagar é R${valor_total}")
    entrega = choice(horario_entrega)
    st.error(f'Horário para a devolução: {entrega}')

