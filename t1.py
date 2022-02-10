# Задание 1
from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        def out_red(text):
            print(text)

        def out_yellow(text):
            print(text)

        def out_green(text):
            print(text)

        while True:
            out_red("Traffic light is red")
            sleep(7)
            out_yellow("Traffic light is yellow")
            sleep(2)
            out_green("Traffic light is green")
            sleep(7)


light_1 = TrafficLight()
light_1.running()