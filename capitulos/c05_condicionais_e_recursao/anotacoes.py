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


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar
    # divisao_inteira_e_modulo()
    pass
