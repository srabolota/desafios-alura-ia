# 🚀 Desafios Imersão IA - Alura

Repositório dedicado às soluções e estudos desenvolvidos durante a Imersão de Inteligência Artificial da Alura.

---

## 📌 Desafio 1: Criando sua primeira aplicação com IA

* **Ferramenta utilizada:** Google AI Studio (Gemini)
* **Linguagem:** Python
* **Descrição:** Criação de uma calculadora de terminal funcional realizando as quatro operações básicas (`+`, `-`, `*`, `/`).

### 🔍 Respostas e Aprendizados do Desafio 1:

1. **Quais são os principais componentes do código gerado?**
   * **Variáveis (`num1`, `num2`, `operacao`, `resultado`):** Caixas na memória RAM que guardam os valores e escolhas do usuário.
   * **`input()`:** Função que interage com o usuário, pausando o terminal para receber o texto digitado via teclado.
   * **`float()`:** Conversor de tipos que transforma o texto capturado em um número decimal, permitindo cálculos matemáticos exatos.
   * **Estruturas Condicionais (`if`, `elif`, `else`):** O "cérebro" de decisão que direciona o fluxo do programa.

2. **Como a aplicação recebe os números e identifica a operação?**
   * Os números usam `float(input(...))` para garantir que entradas como `10` ou `5.5` virem dados numéricos. A operação usa apenas `input(...)` para preservar o caractere especial (`+`, `-`, `*`, `/`) em formato de texto, sendo comparada através do operador de igualdade dupla (`==`).

3. **Como a lógica de programação lida com os resultados e exceções?**
   * O fluxo opera em cascata (*if/elif/else*), executando apenas o bloco correspondente à escolha correta. Além disso, conta com uma proteção preventiva (`if num2 == 0`) para evitar que o programa sofra um fechamento abrupto (*Crash*) por divisão por zero.

* **Arquivo da solução:** [`desafio-1/calculadora.py](./desafio-1/calculadora.py)

---

## 📌 Desafio 2
*(Em breve)*

---

## 📌 Desafio 3
*(Em breve)*
