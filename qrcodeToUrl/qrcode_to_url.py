import cv2
import qrcode

def read_qrcode(image_path):
    # 读取二维码图片
    img = cv2.imread(image_path)
    # 创建二维码解析器
    qr_code_detector = cv2.QRCodeDetector()
    # 解析二维码
    retval, decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(img)

    # 检查是否解析成功
    if retval:
        print("解析成功！")
        print("解析结果：", decoded_info)
    else:
        print("解析失败，请确认输入的是二维码图片。")

if __name__ == "__main__":
    # 输入你二维码文件的地址
    image_path = "filepath.png"
    read_qrcode(image_path)
