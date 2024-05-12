# Main-Control-Work
Developer - Final control work on the main block

Скрипт реализует алгоритм перебора элементов исходного массива и возвращает
новый массив на основании условий фильтра.
<br> Критерий фильтра - длина строкового элемента массива меньше, либо равна 3 символам.

## Псевдокод программы
### Основная функция
```
    // Инициализация исходного массива строк;
    initial_array = user_input();
    // Формирование нового массива из строк длиной до 3 символов;
    new_array = [];
    for string_element in initial_array:
        if length of string_element <= 3:
            append string_element to new_array;
    // Вывод результата;
    print new_array;
```

### Функция инициализации массива
```
    interrupt_keys = ["quit", "exit"];
    user_interrupt = False;
    while not user_interrupt:
        // Спросить пользователя ввести новый элемент или "quit"/"exit" для завершения ввода;
        new_element = input();
        if new_element in interrupt_keys:
            user_interrupt = True;
        else:
            append new_element to initial_array;
```
<details>
<summary><code>Функциональная блок-схема</code></summary>
<p>![функциональная схема](static/flowchart.png?raw=true "functional_scheme")
</details>

</br></br>

#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_
