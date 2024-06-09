import ImageContainer as IC

while True:
    #container = IC.ImageContainer(input("relative path of the container: "))
    #watermark = IC.ImageContainer(input("relative path of the watermark: "))
    container = IC.ImageContainer("img/InputImage.png")
    watermark = IC.ImageContainer("img/WM.png")

    watermark_mono = IC.IC_to_monochrome(watermark)
    watermark_binary = IC.monochrome_to_binary(watermark_mono)

    result = IC.built_in_image(container, watermark)
    watermark_binary.show()
    result.show()
    IC.monochrome_binary_slice(result).show()
    break
