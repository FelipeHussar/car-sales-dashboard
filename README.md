# car-sales-dashboard
# Projeto Streamlit - Dashboard de Carros Usados

Este projeto é um dashboard interativo criado com [Streamlit](https://streamlit.io) para visualizar dados de anúncios de carros usados nos Estados Unidos. A análise é baseada em um dataset com mais de 50 mil registros.

## 📊 Funcionalidades

- Visualização de histograma da quilometragem dos veículos
- Gráfico de dispersão entre quilometragem e preço
- Interface interativa com botões no navegador
- Deploy público na nuvem via Render

## 🚀 Como rodar localmente

```bash
git clone (https://github.com/FelipeHussar/car-sales-dashboard.git)
cd car-sales-dashboard
python -m venv venv
source venv/Scripts/activate   # (ou . venv/bin/activate no Mac/Linux)
pip install -r requirements.txt
streamlit run app.py
