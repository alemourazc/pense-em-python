# Capítulo 5: Condicionais e Recursão


def divisao_inteira_e_modulo():
    """
    Demonstra o uso dos operadores de divisão inteira (//) e módulo (%).
    """
    print("--- Divisão Inteira e Módulo ---\n")
    print(
        "Como já vimos, o operador de divisão inteira, '//', divide dois "
        "números e arredonda o resultado para o inteiro menor mais próximo. "
        "Por exemplo, suponhamos que o tempo de execução de um filme seja "
        "de 105 minutos. Talvez queiramos saber quantas horas isso "
        "representa. A divisão convencional devolve um número de ponto "
        "flutuante:"
    )
    print()
    minutes = 105
    print(minutes / 60)
    print()
    print(
        "No entanto, não é comum representar horas com pontos decimais. A "
        "divisão pelo piso nos fornece apenas o número inteiro de horas, "
        "arredondando para baixo:"
    )
    print()
    hours = minutes // 60
    print(hours)
    print()
    print(
        "Para calcular o resto (remainder), podemos subtrair uma hora, "
        "convertida em minutos:"
    )
    print()
    remainder = minutes - hours * 60
    print(remainder)
    print()
    print(
        "Uma alternativa é utilizar o 'operador de módulo', '%', que divide "
        "dois números e retorna o resto:"
    )
    print()
    remainder = minutes % 60
    print(remainder)
    print()
    print(
        "O operador de módulo é mais versátil do que aparenta. Por exemplo, "
        "podemos verificar se um número é divisível por outro -- se 'x % y' "
        "for igual a zero, então 'x' é divisível por 'y'.\n"
        "Além disso, é possível extrair o dígito ou dígitos mais à direita "
        "de um número. Por exemplo, 'x % 10' retorna o dígito mais à direita "
        "de 'x' (na base 10). Da mesma forma, 'x % 100' nos dá os dois "
        "últimos dígitos.\n"
        "Por fim, o operador de módulo também pode ser empregado para "
        "realizar 'aritmética de relógio'. Por exemplo, se um evento começa "
        "às 11h da manhã e dura três horas, podemos utilizar o operador de "
        "módulo para determinar a hora que ele termina:"
    )
    print()
    start = 11
    duration = 3
    end = (start + duration) % 12
    print(end)
    print()
    print("O evento terminaria às 2h da tarde:")
    print()
    a = 25 // 10
    b = 25 % 10
    print(a, b)


def expressoes_booleanas():
    """
    Demonstra o uso de expressões booleanas e operadores relacionais.
    """
    print("--- Expressões Booleanas ---\n")
    print(
        "Uma 'expressão booleana' é aquela que pode ser verdadeira ou falsa. "
        "Por exemplo, as expressões a seguir utilizam o operador de igualdade"
        ", '==', que compara dois valores e retorna 'True' (verdadeiro) se "
        "forem iguais, e 'False' (falso) se não forem:"
    )
    print()
    print(5 == 5)  # True
    print(5 == 7)  # False
    print()
    print(
        "Um erro comum é utilizar apenas um sinal de igual (=) em vez do "
        "sinal duplo (==). É importante ressaltar que '=' é utilizado para "
        "atribuir um valor a uma variável, enquanto '==' é utilizado para "
        "comparar dois valores:"
    )
    print()
    x = 5
    y = 7
    print(x == y)  # False
    print()
    print(
        "'True' e 'False' são valores especiais do tipo 'bool' (booleano). "
        "Eles não são strings:"
    )
    print()
    print(type(True))  # <class 'bool'>
    print(type(False))  # <class 'bool'>
    print()
    print(
        "O operador '==' é um dos 'operadores relacionais'; os outros são:"
    )
    print()
    print(x != y)  # x não é igual a y (True)
    print(x > y)  # x é maior que y (False)
    print(x < y)  # x é menor que y (True)
    print(x >= y)  # x é maior ou igual a y (False)
    print(x <= y)  # x é menor ou igual a y (True)


def operadores_logicos():
    """
    Demonstra o uso dos operadores lógicos (and, or, not).
    """
    print("--- Operadores Lógicos ---\n")
    print(
        "Para combinar valores booleanos em expressões, podemos utilizar "
        "'operadores lógicos'. Os mais comuns são 'and', 'or' e 'not'. O "
        "significado desses operadores é similar aos seus correspondentes "
        "em inglês. Por exemplo, a expressão a seguir será 'True' apenas se "
        "'x' for maior que '0' e menor que '10':"
    )
    print()
    x = 5
    y = 7
    print(x > 0 and x < 10)  # True
    print()
    print(
        "A expressão a seguir será 'True' se uma ou ambas as condições forem "
        "verdadeiras, ou seja, se o número for divisível por 2 ou por 3:"
    )
    print()
    print(x % 2 == 0 or x % 3 == 0)  # False
    print()
    print(
        "Por fim, o operador 'not' inverte o valor de uma expressão booleana; "
        "portanto, a expressão a seguir será 'True' se 'x > y' for False:"
    )
    print()
    print(not x > y)  # True
    print()
    print(
        "Tecnicamente, os operandos dos operadores lógicos deveriam ser "
        "expressões booleanas, mas o Python é bastante flexível. Qualquer "
        "número diferente de zero é interpretado como True:"
    )
    print()
    print(42 and True)  # True
    print()
    print(
        "Essa flexibilidade pode ser útil, mas há algumas sutilezas que podem "
        "causar confusão. Pode ser mais prudente evitá-la."
    )


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # divisao_inteira_e_modulo()
    # expressoes_booleanas()
    # operadores_logicos()
    pass
