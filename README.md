# Automação de Limpeza e Organização de Planilhas Excel

## 📌 Descrição
Automação desenvolvida em Python para **ler, limpar e organizar planilhas Excel** com dados despadronizados, gerando uma nova planilha pronta para uso profissional.
Ideal para planilhas de vendas, relatórios administrativos ou dados exportados de sistemas.

---

## 🎯 Problema Resolvido
Planilhas desorganizadas geralmente possuem:
- Colunas com nomes inconsistentes
- Linhas vazias
- Dados duplicados
- Valores e datas fora de padrão

Essa automação resolve esses problemas de forma **rápida, automática e reutilizável**.

---

## ⚙️ O que a automação faz
- Lê uma planilha Excel de entrada
- Padroniza os nomes das colunas
- Remove linhas vazias
- Remove dados duplicados
- Gera uma nova planilha limpa e organizada


---

## 📥 Entrada
- Arquivo Excel colocado em:
  `data/input/vendas_raw.xlsx`

---

## 📤 Saída
- Planilha limpa gerada em:
  `data/output/vendas_limpa.xlsx`

---

## ▶️ Como Executar
```bash
pip install -r requirements.txt
python src/main.py
```

---

## 🛠️ Tecnologias Utilizadas
- Python
- pandas
- openpyxl
- pathlib

---

## 👤 Indicado para
- Escritórios
- Pequenas empresas
- Freelancers
- Profissionais que lidam com Excel diariamente

---

> A automação pode ser facilmente adaptada para diferentes estruturas de planilhas conforme a necessidade do usuário.