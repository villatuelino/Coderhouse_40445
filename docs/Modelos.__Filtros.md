# Filter

- Igualdad: campo="valor"
    > Filtra los objetos donde el campo sea igual al valor proporcionado.

- Desigualdad: campo`__ne`="valor"
    > Filtra los objetos donde el campo no sea igual al valor proporcionado.

## Comparación

- Mayor que: campo`__gt`=valor
    > Filtra los objetos donde el campo sea mayor que el valor proporcionado.

- Mayor o igual que: campo`__gte`=valor
    > Filtra los objetos donde el campo sea mayor o igual que el valor proporcionado.

- Menor que: campo`__lt`=valor
    > Filtra los objetos donde el campo sea menor que el valor proporcionado.

- Menor o igual que: campo`__lte`=valor
    > Filtra los objetos donde el campo sea menor o igual que el valor proporcionado.

## Búsqueda en cadenas de texto

- Contiene: campo`__contains`="valor"
    > Filtra los objetos donde el campo contenga el valor proporcionado.

- Comienza con: campo`__startswith`="valor"
    > Filtra los objetos donde el campo comience con el valor proporcionado.

- Termina con: campo`__endswith`="valor"
    > Filtra los objetos donde el campo termine con el valor proporcionado.

## Expresiones regulares: campo__regex="patrón"

Filtra los objetos donde el campo campo coincida con el patrón de expresión regular proporcionado.

## Consultas lógicas

- AND: Q(condición1) & Q(condición2)
    > Combina condiciones utilizando el operador lógico "AND".

- OR: Q(condición1) | Q(condición2)
    > Combina condiciones utilizando el operador lógico "OR".

- NOT: ~Q(condición)
    > Niega una condición.

## Campos relacionados

- Filtrado a través de una relación
    > campo_relacionado`__`campo="valor"
    Filtra los objetos basados en el valor de un campo relacionado.

## Nota

`filter()` devuelve un objeto QuerySet que puede ser iterado y utilizado en otras operaciones, como ordenamiento, agregación y más.
