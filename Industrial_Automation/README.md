# 🏭 Sistema de Gestão de Peças Industrial

Sistema automatizado de controle de qualidade e armazenamento de peças industriais desenvolvido em Python.

## 📋 Descrição

Este sistema foi desenvolvido para automatizar o processo de inspeção e controle de qualidade em linhas de produção industrial. Ele recebe dados das peças produzidas, valida automaticamente segundo critérios pré-estabelecidos, armazena as peças aprovadas em caixas e gera relatórios completos.

### Funcionalidades Principais

✅ Cadastro de peças com validação automática de qualidade  
✅ Aprovação/reprovação baseada em critérios técnicos  
✅ Armazenamento inteligente em caixas (10 peças por caixa)  
✅ Fechamento automático de caixas ao atingir capacidade  
✅ Listagem de peças aprovadas e reprovadas  
✅ Remoção de peças cadastradas  
✅ Relatórios consolidados com estatísticas  

## 🎯 Critérios de Qualidade

Para uma peça ser aprovada, ela deve atender **todos** os seguintes critérios:

| Critério | Valor Aceitável |
|----------|----------------|
| **Peso** | 95g - 105g |
| **Cor** | Azul ou Verde |
| **Comprimento** | 10cm - 20cm |

## 🚀 Como Executar o Programa

### Pré-requisitos

- Python 3.7 ou superior instalado
- PyCharm (recomendado) ou qualquer IDE/terminal

### Passo a Passo

1. **Clone ou baixe o repositório**
```bash
git clone https://github.com/seu-usuario/sistema-gestao-pecas.git
cd sistema-gestao-pecas
```

2. **Execute o programa**

No terminal:
```bash
python main.py
```

Ou no PyCharm:
- Abra o arquivo `main.py`
- Clique em Run (▶️) ou pressione `Shift + F10`

3. **Interaja com o menu**

Use os números de 0 a 6 para navegar pelas opções.

## 📖 Menu do Sistema

```
1. Cadastrar nova peça
2. Listar peças aprovadas
3. Listar peças reprovadas
4. Remover peça cadastrada
5. Listar caixas fechadas
6. Gerar relatório final
0. Sair do sistema
```

## 💡 Exemplos de Uso

### Exemplo 1: Cadastrando uma Peça Aprovada

**Entrada:**
```
Escolha uma opção: 1
Peso (gramas): 100
Cor: azul
Comprimento (cm): 15
```

**Saída:**
```
✓ Peça P0001 cadastrada e APROVADA!
```

---

### Exemplo 2: Cadastrando uma Peça Reprovada

**Entrada:**
```
Escolha uma opção: 1
Peso (gramas): 120
Cor: vermelho
Comprimento (cm): 8
```

**Saída:**
```
✗ Peça P0002 cadastrada mas REPROVADA!
  Motivo: Peso fora do padrão (120g), Cor inválida (vermelho), Comprimento fora do padrão (8cm)
```

---

### Exemplo 3: Listando Peças Aprovadas

**Entrada:**
```
Escolha uma opção: 2
```

**Saída:**
```
============================================================
PEÇAS APROVADAS
============================================================
ID: P0001 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm | ✓ APROVADA
ID: P0003 | Peso: 98.0g | Cor: verde | Comprimento: 12.0cm | ✓ APROVADA
ID: P0005 | Peso: 102.0g | Cor: azul | Comprimento: 18.0cm | ✓ APROVADA
============================================================
```

---

### Exemplo 4: Relatório Final

**Entrada:**
```
Escolha uma opção: 6
```

**Saída:**
```
============================================================
RELATÓRIO FINAL DO SISTEMA
============================================================

Total de peças processadas: 15
  ✓ Aprovadas: 11
  ✗ Reprovadas: 4

Motivos de reprovação:
  • Peso fora do padrão (120g): 1 peça(s)
  • Cor inválida (vermelho): 2 peça(s)
  • Comprimento fora do padrão (8cm): 1 peça(s)

Caixas utilizadas: 2
  → Fechadas: 1
  → Em uso: 1
  → Caixa atual: #2 com 1/10 peças

Taxa de aprovação: 73.3%
============================================================
```

---

### Exemplo 5: Caixa Fechada Automaticamente

Ao cadastrar a 10ª peça aprovada:

**Saída:**
```
✓ Peça P0010 cadastrada e APROVADA!
  → Caixa #1 FECHADA (capacidade máxima atingida)!
  → Nova caixa #2 iniciada!
```

---

### Exemplo 6: Removendo uma Peça

**Entrada:**
```
Escolha uma opção: 4
Digite o ID da peça a remover (ex: P0001): P0005
```

**Saída:**
```
✓ Peça P0005 removida com sucesso!
```

## 🏗️ Estrutura do Código

```
sistema-gestao-pecas/
│
├── main.py                 # Arquivo principal com todo o código
├── README.md              # Este arquivo
└── .gitignore            # Arquivos a ignorar no Git
```

### Classes Principais

#### 1. `Peca`
Representa uma peça individual com seus atributos e validação automática.

**Atributos:**
- `id`: Identificador único (formato: P0001, P0002, etc.)
- `peso`: Peso em gramas
- `cor`: Cor da peça
- `comprimento`: Comprimento em centímetros
- `aprovada`: Status de aprovação (True/False)
- `motivo_reprovacao`: Descrição dos problemas encontrados

**Métodos:**
- `_validar_qualidade()`: Valida a peça segundo os critérios estabelecidos

---

#### 2. `Caixa`
Representa uma caixa de armazenamento com capacidade limitada.

**Atributos:**
- `numero`: Número identificador da caixa
- `capacidade`: Capacidade máxima (10 peças)
- `pecas`: Lista de peças armazenadas
- `fechada`: Status da caixa (aberta/fechada)

**Métodos:**
- `adicionar_peca()`: Adiciona uma peça à caixa
- `fechar()`: Fecha a caixa
- `esta_cheia()`: Verifica se atingiu a capacidade

---

#### 3. `SistemaGestao`
Gerencia todo o sistema de cadastro, validação e relatórios.

**Atributos:**
- `pecas_aprovadas`: Lista de peças aprovadas
- `pecas_reprovadas`: Lista de peças reprovadas
- `caixas`: Lista de caixas de armazenamento
- `contador_pecas`: Contador para gerar IDs únicos

**Métodos:**
- `cadastrar_peca()`: Cadastra e valida nova peça
- `_armazenar_peca()`: Armazena peça aprovada em caixa
- `listar_pecas_aprovadas()`: Lista peças aprovadas
- `listar_pecas_reprovadas()`: Lista peças reprovadas
- `remover_peca()`: Remove peça pelo ID
- `listar_caixas()`: Lista caixas fechadas
- `gerar_relatorio()`: Gera relatório completo

## 🔧 Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação
- **POO (Programação Orientada a Objetos)**: Paradigma utilizado
- **Type Hints**: Para melhor documentação do código
- **Bibliotecas nativas**: `typing`, `os`

## 📊 Fluxo de Funcionamento

```
┌─────────────────────────────────────┐
│  Usuário cadastra peça              │
│  (peso, cor, comprimento)           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Sistema cria objeto Peca           │
│  com ID único                       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Validação automática dos critérios │
│  (peso, cor, comprimento)           │
└──────────────┬──────────────────────┘
               │
          ┌────┴────┐
          │         │
          ▼         ▼
    APROVADA    REPROVADA
          │         │
          ▼         ▼
┌──────────────┐  ┌─────────────────────┐
│ Adiciona em  │  │ Adiciona em         │
│ caixa aberta │  │ lista reprovadas    │
└──────┬───────┘  │ + salva motivo      │
       │          └─────────────────────┘
       ▼
  ┌─────────────────┐
  │ Caixa tem       │
  │ 10 peças?       │
  └────┬─────┬──────┘
       │     │
     SIM   NÃO
       │     │
       ▼     └────────────┐
┌─────────────────┐       │
│ Fecha caixa     │       │
│ Abre nova caixa │       │
└─────────────────┘       │
       │                  │
       └──────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Dados prontos para relatórios      │
└─────────────────────────────────────┘
```

## 🎓 Conceitos de Programação Aplicados

### 1. Programação Orientada a Objetos (POO)
- **Encapsulamento**: Dados e métodos agrupados em classes
- **Abstração**: Complexidade escondida atrás de interfaces simples
- **Métodos privados**: Uso de `_` para métodos internos

### 2. Estruturas de Dados
- **Listas**: Para armazenar peças e caixas
- **Strings**: Para mensagens e IDs
- **Booleanos**: Para status de aprovação

### 3. Estruturas de Controle
- **Condicionais (if/elif/else)**: Para validações e decisões
- **Loops (for/while)**: Para iteração e menu
- **Try/Except**: Para tratamento de erros

### 4. Boas Práticas
- **Docstrings**: Documentação em todas as classes e métodos
- **Type Hints**: Indicação de tipos esperados
- **Nomes descritivos**: Variáveis e funções com nomes claros
- **Separação de responsabilidades**: Cada classe/método tem função específica
- **Formatação de código**: Seguindo PEP 8

## 🐛 Tratamento de Erros

O sistema possui tratamento para:
- ✅ Entrada de valores não numéricos
- ✅ Valores negativos ou fora de faixa
- ✅ Interrupção pelo usuário (Ctrl+C)
- ✅ Peça não encontrada ao remover
- ✅ Opções inválidas no menu

## 🔮 Possíveis Melhorias Futuras

- [ ] Persistência de dados (salvar em arquivo JSON ou banco de dados)
- [ ] Interface gráfica (GUI) com Tkinter ou PyQt
- [ ] Geração de relatórios em PDF
- [ ] Exportação de dados para Excel
- [ ] Sistema de autenticação de usuários
- [ ] Histórico de operações (log)
- [ ] Integração com sensores IoT
- [ ] Dashboard web com Flask ou Django
- [ ] API REST para integração com outros sistemas
- [ ] Notificações por email quando taxa de reprovação aumentar

## 👨‍💻 Autor

**Daniel Fernandes**
- GitHub: [https://github.com/bdancost]
- LinkedIn: [https://www.linkedin.com/in/daniel-fernandes1988/]
- Email: pr.danfc88@gmail.com



