import fractal_handler as fh
# task 3
print("task 3")
for i in range(8):
    fh.draw_nth_l_fractal("F++F++F", {
        "F":"F-F++F-F"
    }, 200/(i**3+1),60,i,"Сніжинка Коха")

for i in range(6):
    fh.draw_nth_l_fractal("F+XF+F+XF", {
        "X":"XF-F+F-XF+F+XF-F+F-X"
    }, 200/(i**2.2+1),90,i,"Хрестоподібний фрактал")

for i in range(6):
    fh.draw_nth_l_fractal("F+F+F+F", {
        "F":"FF+F++F+F"
    }, 200/(i**3+1),90,i,"Кристалоподібний фрактал")

for i in range(1,6):
    fh.draw_nth_l_fractal("X", {
        "X":"XFYFX+F+YFXFY-F-XFYFX",
        "Y":"YFXFY-F-XFYFX+F+YFXFY"
    }, 200/(i**2.5+1),90,i,"Фрактальна крива Пеано")

for i in range(6):
    fh.draw_nth_l_fractal("F+F+F+F", {
        "F": "FF+F+F+F+FF"
    }, 200 / (i ** 2.7 + 1), 90, i, "Фрактальна дошка")

for i in range(7):
    fh.draw_nth_l_fractal("YF", {
        "X": "YF+XF+Y",
        "Y": "XF-YF-X"
    }, 200 / (i ** 1.7 + 1), 60, i, "Наконечник стріли Серпінського")

for i in range(7):
    fh.draw_nth_l_fractal("F++F++F++F++F", {
        "F": "F++F++F+++++F-F++F"
    }, 200 / (i ** 2.7 + 1), 36, i, "П'ятикутна фрактальна сніжинка")

for i in range(5):
    fh.draw_nth_l_fractal("XF", {
        "X": "X+YF++YF-FX--FXFX-YF+",
        "Y": "-FX+YFYF++YF+FX--FX-Y"
    }, 200 / (i ** 2.2 + 1), 60, i, "Гексагональна крива Госпера")

# task 4
print("task 4")
for i in range(5):
    fh.draw_nth_l_fractal("F++F++F", {
        "F":"F-F++F-F"
    }, 200/(i**3+1),30,i,"Сніжинка Коха з кутом 30")

for i in range(8):
    fh.draw_nth_l_fractal("F+XF+F+XF", {
        "X":"XF-F+F-XF+F+XF-F+F-X"
    }, 200/(i+1),120,i,"Хрестоподібний фрактал з кутом 120")

for i in range(5):
    fh.draw_nth_l_fractal("F+F+F+F", {
        "F":"FF+F++F+F"
    }, 200/(i**2+1),120,i,"Кристалоподібний фрактал з кутом 120")

for i in range(1,5):
    fh.draw_nth_l_fractal("X", {
        "X":"XFYFX+F+YFXFY-F-XFYFX",
        "Y":"YFXFY-F-XFYFX+F+YFXFY"
    }, 200/(5*i**2.5+1),45,i,"Фрактальна крива Пеано з кутом 45")

for i in range(5):
    fh.draw_nth_l_fractal("F+F+F+F", {
        "F": "FF+F+F+F+FF"
    }, 200 / (i ** 2 + 1), 120, i, "Фрактальна дошка з кутом 120")

for i in range(10):
    fh.draw_nth_l_fractal("YF", {
        "X": "YF+XF+Y",
        "Y": "XF-YF-X"
    }, 200 / (i ** 1.5 + 1), 90, i, "Наконечник стріли Серпінського з кутом 90")

for i in range(5):
    fh.draw_nth_l_fractal("F++F++F++F++F", {
        "F": "F++F++F+++++F-F++F"
    }, 200 / (i ** 2 + 1), 48, i, "П'ятикутна фрактальна сніжинка з кутом 48")

for i in range(5):
    fh.draw_nth_l_fractal("XF", {
        "X": "X+YF++YF-FX--FXFX-YF+",
        "Y": "-FX+YFYF++YF+FX--FX-Y"
    }, 200 / (i ** 3 + 1), 30, i, "Гексагональна крива Госпера з кутом 30")
# task 5
print("task 5")
fh.animate_nth_fractal("F++F++F",{
        "F":"F-F++F-F"
    }, 200/(5**3+1),30,60,5,0.1,0.1,"Анімована сніжинка Коха")