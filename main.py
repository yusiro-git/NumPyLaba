import numpy as np
import pandas as pd
import argparse

def open_file(path):
    data = np.loadtxt(path, skiprows=1, delimiter=',', dtype='int32')
    return data

def first_task(data):
    df = pd.DataFrame(data[:5])
    print("Первые 5 рецептов:\n", df)

def second_task(data):
    stats = {
        'Column 1': [data[:, 1].mean(), data[:, 1].min(), data[:, 1].max(), np.median(data[:, 1])],
        'Column 2': [data[:, 2].mean(), data[:, 2].min(), data[:, 2].max(), np.median(data[:, 2])]
    }
    df = pd.DataFrame(stats, index=['Mean', 'Min', 'Max', 'Median'])
    print(df)

def third_task(data):
    q_75 = np.quantile(data[:, 1], 0.75)
    filtered_data = data[data[:, 1] <= q_75]
    df = pd.DataFrame(filtered_data)
    print(f"Квантиль: {q_75}")
    print("Отсортированная таблица:")
    print(df)

def fourth_task(data):
    print("Количество рецептов с продолжительностью ноль:", len(data[data[:, 1] == 0]))
    data[data[:, 1] == 0, 1] = 1
    df = pd.DataFrame(data[data[:, 1] == 1])
    print("\nРецепты с измененной продолжительностью:\n", df)

def fifth_task(data):
    print("Колиечество уникальный рецептов:", len(np.unique(data, axis=1)))

def sixth_task(data):
    print("Количество уникальных количеств ингредиентов:", len(np.unique(data[:, 2])))
    df = pd.DataFrame(np.unique(data[:, 2]), columns=['Уникальное количество ингредиентов'])
    print("\nУникальное количество ингредиентов:\n", df)

def seventh_task(data):
    df = pd.DataFrame(data[data[:, 2] <= 5])
    print("Рецепты состоящие из 5 и меньше ингредиентов:\n", df)

def eighth_task(data):
    data[data[:, 1] == 0, 1] = 1 # что бы не делить на 0
    print("Максимальное значение отношения ингредиентов на минуту:", np.max(data[:, 2] / data[:, 1]))
    for i in range(10):
        print(f"Рецепт: {data[i, 0]}, Значение: {data[i, 2] / data[i, 1]}")

def ninth_task(data): 
    top_100 = (data[data[:, 1].argsort()][-100:])
    print("Среднее значение ингредиентов топ 100 рецептов:", top_100[:, 2].mean())

def tenth_task(data):
    df = pd.DataFrame(data[np.random.randint(0, len(data), (10))])
    print("Информация о 10 рандомных рецептах:\n", df)   

def eleventh_task(data):
    print("Процент рецептов с количеством ингредиентов меньше среднего: "\
          , len(data[data[:, 2] < data[:, 2].mean()]) / len(data) * 100, "%", sep="")

def twelth_task(data):
    a = np.array([(data[:, 1] <= 20)] and [(data[:, 2] <= 5)], dtype='int32').transpose()
    data3 = np.append(data, a, axis=1)
    df = pd.DataFrame(data3)
    print("Новая таблица:\n", df)


def thirteenth_task(data):
    a = np.array([(data[:, 1] <= 20)] and [(data[:, 2] <= 5)], dtype='int32').transpose()
    data3 = np.append(data, a, axis=1)
    print("Количество простых рецептов: ", sum(data3[:, 3]) / len(data3) * 100, "%", sep="")

def fourteenth_task(data):
    short_recipes = data[data[:, 1] < 10]
    standard_recipes = data[(data[:, 1] >= 10) & (data[:, 1] < 20)]
    long_recipes = data[data[:, 1] >= 20]

    max_index = max(data[:, 0]) + 1
    arr = np.empty((3, max_index, 2), dtype='int32')

    arr[0, short_recipes[:, 0], :] = short_recipes[:, 1:]
    arr[1, standard_recipes[:, 0], :] = standard_recipes[:, 1:]
    arr[2, long_recipes[:, 0], :] = long_recipes[:, 1:]

    print("Форма массива:", arr.shape)


def main():
    parser = argparse.ArgumentParser(description='Process some recipes.')
    parser.add_argument('--path', type=str, required=True, help='Path to the data file')
    args = parser.parse_args()

    if not args.path:
        print("Error: Укажите путь к таблице.")
        exit(1)

    try:
        data = open_file(args.path)
    except Exception as e:
        print("Error: Не удалось открыть файл.")
        exit(1)

    print("Задание 1:")
    first_task(data)
    print("Задание 2:")
    second_task(data)
    print("Задание 3:")
    third_task(data)
    print("Задание 4:")
    fourth_task(data)
    print("Задание 5:")
    fifth_task(data)
    print("Задание 6:")
    sixth_task(data)
    print("Задание 7:")
    seventh_task(data)
    print("Задание 8:")
    eighth_task(data)
    print("Задание 9:")
    ninth_task(data)
    print("Задание 10:")
    tenth_task(data)
    print("Задание 11:")
    eleventh_task(data)
    print("Задание 12:")
    twelth_task(data)
    print("Задание 13:")
    thirteenth_task(data)
    print("Задание 14:")
    fourteenth_task(data)


if __name__ == '__main__':
    main()
