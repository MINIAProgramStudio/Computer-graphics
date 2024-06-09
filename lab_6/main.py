import ImageContainer as IC

while True:
    #container = IC.ImageContainer(input("relative path of the container: "))
    #watermark = IC.ImageContainer(input("relative path of the watermark: "))
    container = IC.ImageContainer("img/InputImage.png")
    watermark = IC.ImageContainer("img/WM.png")
    text = input(">>>")

    watermark_mono = IC.IC_to_monochrome(watermark)
    watermark_binary = IC.monochrome_to_binary(watermark_mono)

    result_1 = IC.built_in_image(container, watermark)

    # result = IC.built_in_text(, text, 2, 2)

    watermark_binary.show()
    IC.monochrome_binary_slice(result_1).show()
    break
