import cv2

def apply_gray_filter(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("images/output/gray.png", gray)

if __name__ == "__main__":
    apply_gray_filter("images/input/sample.jpg")
