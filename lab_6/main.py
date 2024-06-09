import ImageContainer as IC

while True:
    container = IC.ImageContainer(input("relative path of the container: "))
    watermark = IC.ImageContainer(input("relative path of the watermark: "))
    text = input(">>>")

    watermark_mono = IC.IC_to_monochrome(watermark)
    watermark_binary = IC.monochrome_to_binary(watermark_mono)

    result_1 = IC.built_in_image(container, watermark_binary)

    result = IC.built_in_text(result_1, text, 1, bit = 1)

    IC.monochrome_binary_slice(result_1).show()
    IC.monochrome_binary_slice(result, channel=1, bit = 1).show()
    result.show()
    result.path = "output/result.png"
    result.save()
    break
