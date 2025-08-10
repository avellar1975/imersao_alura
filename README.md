# 📊 Imersão Dados com Python

Dashboard interativo em Python para análise de indicadores econômicos brasileiros, desenvolvido com Streamlit, utilizando dados do IPEA e Banco Central do Brasil.

---

## 🚀 Funcionalidades
- Visualização interativa de **PIB**, **IPCA** e **Taxa de Desocupação**.
- Filtros por ano e por tipo de indicador.
- Gráficos dinâmicos com Plotly.
- Publicação online via Streamlit Cloud.

---

## 📂 Estrutura do Repositório

```
data/ # Dados originais em CSV
notebooks/ # Jupyter Notebooks para análise e limpeza
notebooks/dados_normalizados.parquet # Base tratada para uso no Dashboard
app.py # Aplicação Streamlit
requirements.txt # Dependências do projeto

```
---

## 📊 Fonte de Dados

**Produto Interno Bruto (PIB)**
- **Código:** BM12_PIB12
- **Período:** 1990-01 a 2025-06
- **Fonte:** Banco Central do Brasil
- **Unidade:** R$ (milhões)
- **Arquivo:** `data/pib.csv`

**Índice Nacional de Preços ao Consumidor Amplo (IPCA)**
- **Código:** PRECOS12_IPCAG12
- **Período:** 1980-01 a 2025-06
- **Fonte:** IBGE / SNIPC
- **Unidade:** % a.m.
- **Arquivo:** `data/ipca.csv`

**Taxa de Desocupação**
- **Código:** PNADC12_TDESOCM12
- **Período:** 2012-01 a 2025-05
- **Fonte:** IPEA
- **Unidade:** %
- **Arquivo:** `data/desocupacao.csv`


---

| Indicador | Código | Período | Fonte | Unidade | Arquivo |
|-----------|--------|---------|-------|---------|---------|
| PIB       | BM12_PIB12 | 1990-01 a 2025-06 | BCB | R$ (milhões) | `data/pib.csv` |
| IPCA      | PRECOS12_IPCAG12 | 1980-01 a 2025-06 | IBGE | % a.m. | `data/ipca.csv` |
| Desocupação | PNADC12_TDESOCM12 | 2012-01 a 2025-05 | IPEA | % | `data/desocupacao.csv` |

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/seurepo.git
cd seurepo
```

### 2️⃣ Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar localmente
```bash
streamlit run app.py
```

# 🌐 Acesso Online

Acesse o dashboard publicado no Streamlit Cloud:
https://imersao-alura-indicadores.streamlit.app/


## Links:
- [Guia de Mergulho](https://alura.tv/guiademergulhodadoscompython)
- [Plataforma Imersão](https://cursos.alura.com.br/imersao/imersao-dados-python)

# 👨‍💻 Autor
### Evandro Avellar
Projeto desenvolvido durante a Imersão Dados com Python.
