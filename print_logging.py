import logging

# Настройка логирования
logging.basicConfig(filefname='tsp_solver.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log(name, result, current, peak, elapsed_time):
    logging.info(f"\n{name} - {elapsed_time}")
    logging.info(f"Минимальное расстояние для обхода всех городов: {result}")
    logging.info(f"Время выполнения: {elapsed_time}")
    logging.info(f"Текущая память: {current:.2f} KB; Пиковая память: {peak:.2f} KB")
    print(f"\n{name} - {elapsed_time}")
    print(f"Минимальное расстояние для обхода всех городов: {result}")
    print(f"Время выполнения: {elapsed_time}\n")
    print(f"Текущая память: {current:.2f} KB; Пиковая память: {peak:.2f} KB")
