import cv2

if __name__ == '__main__':
    filepath = "img/ts.jpg"
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
    classifier = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt_tree.xml')
    x = y = 10  # 坐标
    w = 100  # 矩形大小（宽、高）
    color = (0, 0, 255)  # 定义绘制颜色
    faceRects = classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRects):  # 大于0则检测到人脸
        for faceRect in faceRects:  # 单独框出每一张人脸
            x, y, w, h = faceRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
            # 左眼
            cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                       color)
            # 右眼
            cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                       color)
            # 嘴巴
            cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                          (x + 5 * w // 8, y + 7 * h // 8), color)

    #cv2.rectangle(img, (x, y), (x + w, y + w), color, 1)  # 绘制矩形
    cv2.imshow("image", img)  # 显示图像
    c = cv2.waitKey(10)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

