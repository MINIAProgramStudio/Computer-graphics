import fractal_handler as fh

for i in range(10):
    fh.draw_nth_l_fractal("F++F++F", {
        "F":"F-F++F-F"
    }, 200/(i**3+1),60,i,"Сніжинка Коха")

for i in range(8):
    fh.draw_nth_l_fractal("F+XF+F+XF", {
        "X":"XF-F+F-XF+F+XF-F+F-X"
    }, 200/(i**2.2+1),90,i,"Хрестоподібний фрактал")

for i in range(8):
    fh.draw_nth_l_fractal("F+F+F+F", {
        "F":"FF+F++F+F"
    }, 200/(i**3+1),90,i,"Кристалоподібний фрактал")

for i in range(1,6):
    fh.draw_nth_l_fractal("X", {
        "X":"XFYFX+F+YFXFY-F-XFYFX",
        "Y":"YFXFY-F-XFYFX+F+YFXFY"
    }, 200/(i**3+1),90,i,"Фрактальна крива Пеано")