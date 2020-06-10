# ******************************************************************************
"""
Detects or extracts a face(s) from an image with Haarcascades decoder.


Private Functions:
    . none,


Public Class:
    .  Haar                     a class to detect or extract a face from an image,


Private Methods:
    . __detect_face             detects the face(s) on the passed-in image,


Public Methods:
    . get_face                  extracts the face from the passed-in image,
    . get_image_with_faces      detects and highlights the face(s) on the image,


@namespace      -
@author         <author_name>
@since          0.0.0
@version        0.0.0
@licence        MIT. Copyright (c) 2020 Mobilabs <contact@mobilabs.fr>
"""
# ******************************************************************************
import cv2

HAAR_FRONTFACE = './resources/haarcascades/haarcascade_frontalface_default.xml'
RECT_COLOR = (0, 255, 255)
RECT_THICKNESS = 2


# -- Public --------------------------------------------------------------------

class Haar:
    """A class to detect or extract a face from an image with Haarcascades.

    ### Attributes:
        classifier (obj):       the Haarcascades decoder object.

    ### Methods:
        get_face(image):
            extracts the face from the passed-in image.

        get_image_with_faces(image):
            detects and highlights the face(s) on the passed-in image.

    ### Raises:
        none
    """

    def __init__(self):
        """Creates the Haarcascades decoder."""
        self.classifier = cv2.CascadeClassifier(HAAR_FRONTFACE)

    def __detect_face(self, img):
        """Detects the face(s) on the passed-in image.

        ### Parameters:
            param1 (str):   the path of the input image.

        ### Returns:
            (arr):          returns the coordinates of the detected face(s).

        ### Raises:
            -
        """
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
        return self.classifier.detectMultiScale(gray, 1.3, 5)

    def get_face(self, image):
        """Extracts the face from the passed-in image.

        ### Parameters:
            param1 (arr):   the input image.

        ### Returns:
            (arr):          returns the extracted face.

        ### Raises:
            -
        """
        x, y, w, h = self.__detect_face(image)[0]
        return image[y:y + h, x:x + w, :]

    def get_image_with_faces(self, image):
        """Detects and highlights the face(s) on the passed-in image.

        ### Parameters:
            param1 (arr):   the input image.

        ### Returns:
            (arr):          returns the input image with highlighted face(s).

        ### Raises:
            -
        """
        img = image.copy()
        faces = self.__detect_face(img)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), RECT_COLOR, RECT_THICKNESS)
        return img

# -- o ---
