import streamlit as st

st.title("Banco Bosson")

with st.expander("Calculadora de Juros Simples"):
    st.write("Preencha os campos abaixo para calcular o juro simples:")

    juros = st.number_input("Digite os juros", value=0.0, key="juros_simples")
    capitalInicial = st.number_input("Digite o capital inicial", value=0.0, key="capital_inicial_simples")

    st.write(f"Juros: {juros}")
    st.write(f"Capital Inicial: {capitalInicial}")

    if capitalInicial is not None and juros is not None:
        capitalFinal = capitalInicial + juros
        st.write(f"Capital final: {capitalFinal}")
    else:
        st.write("Por favor, digite os valores de juros e capital inicial.")

with st.expander("Calculadora de Juros Compostos"):
    st.write("Preencha os campos abaixo para calcular o juro composto:")

    taxaDeJuros = st.number_input("Digite a taxa de juros ao mês", key="taxa_juros_compostos")
    capitalInicialC = st.number_input("Digite o capital inicial", key="capital_inicial_compostos")
    periodo = st.number_input("Digite o periodo em meses", key="periodoJuros")
    st.write(f"Juros: {taxaDeJuros}")
    st.write(f"Capital Inicial: {capitalInicialC}")
    st.write(f"Periodo: {periodo}")

    if capitalInicialC is not None and taxaDeJuros is not None and periodo is not None:
        taxaDeJuros = int(taxaDeJuros) / 100 
        variacaoEmJuros = capitalInicialC * taxaDeJuros
        capitalizacao = capitalInicialC + variacaoEmJuros
        for k in range(2, int(periodo)+1):
            variacaoEmJuros = capitalizacao * taxaDeJuros
            capitalizacao = capitalizacao + variacaoEmJuros
        st.write(capitalizacao)